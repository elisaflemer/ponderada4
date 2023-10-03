import pandas as pd
import json
import pickle

model = pickle.load(open('services/model', 'rb'))

with open('services/input.json', 'r') as json_file:
    data = json.load(json_file)

df = pd.DataFrame([data])

predictions = model.predict(df)

with open('services/output.txt', 'w') as file:
    file.write(str(predictions[0]))