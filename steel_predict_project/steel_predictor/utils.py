import random


def predict_stub(data, steel_type):
    return {
        "UTS (MPa)": round(random.uniform(300, 800), 2),
        "YS (MPa)": round(random.uniform(200, 600), 2),
        "Elongation (%)": round(random.uniform(10, 40), 2),
        "Hardness (HB)": round(random.uniform(100, 300), 2),
        "Reduction (%)": round(random.uniform(30, 70), 2)
    }
