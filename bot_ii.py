
from sklearn.metrics import accuracy_score
from joblib import load

modelIntent = load("intents.joblib")
modelAnswer = load("answers.joblib")

vectorizerIntent = load("vector-intents.joblib")
vectorizerAnswer = load("vector-answers.joblib")

xy = load("xy.joblib")


def get_answer(question):

    vector = vectorizerAnswer.transform([question.lower()])

    predictions = modelIntent.predict(vector)
    category = predictions[0]

    predictions = modelAnswer.predict(vector)
    answer = predictions[0]

    return {"category": category, "answer": answer}
