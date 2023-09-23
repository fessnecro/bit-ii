from sklearn.metrics import accuracy_score
from joblib import load

modelAnswer = load("answers.joblib")
vectorizerAnswer = load("vector-answers.joblib")

def get_answer(question):

    vector = vectorizerAnswer.transform([question.lower()])

    predictions = modelAnswer.predict(vector)
    answer = predictions[0]

    return {"answer": answer}
