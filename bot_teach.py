import openpyxl

from joblib import dump
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC


INTENTS = {}

# Define variable to load the wookbook
wookbook = openpyxl.load_workbook("data.xlsx")
# Define variable to read the active sheet:
worksheet = wookbook.active
# Iterate the loop to read the cell values
for row in range(2, worksheet.max_row):
    intent = worksheet.cell(row=row, column=2).value.lower()
    question = worksheet.cell(row=row, column=3).value.lower()
    answer = worksheet.cell(row=row, column=4).value.lower()
    if (not INTENTS.get(intent)):
        INTENTS[intent] = []
    
    INTENTS[intent].append({"question": question, "answer": answer})


XIntension = []
YIntension = []

XAnswer = []
YAnswer = []

for intent in INTENTS:
    for data in INTENTS[intent]:
        XIntension.append(data['question'] + " " + data['answer'])
        YIntension.append(intent)

for intent in INTENTS:
    for data in INTENTS[intent]:
        XAnswer.append(data['question'] + " " + data['answer'])
        YAnswer.append(data['answer'])

vectorizer = TfidfVectorizer(analyzer='char_wb', ngram_range=(2,3), max_df=0.8)
vectorizer.fit(XIntension)
dump(vectorizer, 'vector-intents.joblib')

vecX = vectorizer.transform(XIntension)

vectorizer = TfidfVectorizer(analyzer='char_wb', ngram_range=(2,3), max_df=0.8)
vectorizer.fit(XAnswer)
dump(vectorizer, 'vector-answers.joblib')

vecXanswer = vectorizer.transform(XAnswer)

modelIntent = LinearSVC()
modelIntent.fit(vecX, YIntension)

modelAnswer = LinearSVC()
modelAnswer.fit(vecXanswer, YAnswer)

dump(modelIntent, "intents.joblib")
dump(modelAnswer, "answers.joblib")


