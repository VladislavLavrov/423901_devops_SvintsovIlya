from django.shortcuts import render
from .utils import predict_stub
from .models import Prediction


def index(request):
    return render(request, 'steel_predictor/index.html')


def result_view(request):
    return render(request, 'steel_predictor/result.html')


def predict_view(request, steel_type):
    steel_names = {
        'carbon': 'углеродистой стали',
        'stainless': 'нержавеющей стали'
    }
    steel_name = steel_names.get(steel_type, 'стали')

    if request.method == 'POST':
        data = request.POST
        result = predict_stub(data, steel_type)

        Prediction.objects.create(
            steel_type=steel_type,
            C=float(data['C']),
            Mn=float(data['Mn']),
            Si=float(data['Si']),
            P=float(data['P']),
            S=float(data['S']),
            Ni=float(data.get('Ni') or 0),
            Cr=float(data.get('Cr') or 0),
            Mo=float(data.get('Mo') or 0),
            Ti=float(data.get('Ti') or 0),
            UTS=result['UTS (MPa)'],
            YS=result['YS (MPa)'],
            Elongation=result['Elongation (%)'],
            Hardness=result['Hardness (HB)'],
            Reduction=result['Reduction (%)']
        )

        return render(request, 'steel_predictor/result.html', {
            'result': result,
            'data': data,
            'steel_name': steel_name,
            'steel_type': steel_type
        })

    return render(request, 'steel_predictor/predict.html', {
        'steel_name': steel_name,
        'steel_type': steel_type
    })


def history_view(request, steel_type):
    predictions = Prediction.objects.filter(
        steel_type=steel_type).order_by('-created_at')
    steel_names = {
        'carbon': 'углеродистой стали',
        'stainless': 'нержавеющей стали'
    }
    steel_name = steel_names.get(steel_type, 'стали')

    return render(request, 'steel_predictor/history.html', {
        'predictions': predictions,
        'steel_name': steel_name,
        'steel_type': steel_type
    })
