import pandas as pd
from pycaret.classification import load_model
import json

# Load the saved PyCaret model
model = load_model('services/model')

with open('services/input.json', 'r') as json_file:
    data = json.load(json_file)


df = pd.DataFrame([data])

predictions = model.predict(df)

with open('services/output.txt', 'w') as file:
    file.write(str(predictions[0]))