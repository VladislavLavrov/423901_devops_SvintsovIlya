from django.shortcuts import render
from .utils import predict_stub


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
