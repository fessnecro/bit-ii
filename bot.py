import sys
import random
from joblib import dump, load

from sklearn.model_selection import train_test_split  
from sklearn.metrics import accuracy_score, f1_score
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import GradientBoostingClassifier

INTENTS = {
    "news": {
        "examples": ['новости', 'что нового', 'погода', 'курс доллара'],
        'response': ['Новости: нового ничего, погода класс, курс доллара гавно!', 'Не стоит интересоваться новостями!']
    },
    "hello": {
        "examples": ['Привет', 'прив', 'здарова'],
        'response': ['Ну здарова']
    },
    "how_are_u": {
        "examples": ['Как', 'дела', 'ты как', 'что нового'],
        'response': ['Супер', 'Круто', 'огонь']
    }
}



X = []
Y = []


for intent in INTENTS:
    examples = INTENTS[intent]['examples']
    for example in examples:
        X.append(example)
        Y.append(intent)


vectorizer = CountVectorizer()
vectorizer.fit(X)
#dump(vectorizer, 'vector.joblib')
vecX = vectorizer.transform(X)


model = GradientBoostingClassifier()
model.fit(vecX, Y)

#dump(model, "intents.joblib")


#model = load("intents.joblib")
#vectorizer = load("vector.joblib")

if __name__ == "__main__":
    if len (sys.argv) > 1:
        predictions = model.predict(vectorizer.transform([sys.argv[1]]))
        print (random.choice(INTENTS[predictions[0]]["response"]))