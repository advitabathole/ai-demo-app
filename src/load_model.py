import joblib

def load():
    model = joblib.load("model/model.pkl")
    vectorizer = joblib.load("model/vectorizer.pkl")
    return model, vectorizer

