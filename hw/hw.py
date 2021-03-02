import sys
import json

with open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'map.json')) as fp:
  jsonData = json.load(fp)

data = jsonData['mydata']

def data_to_str(data=data):
  return str(data)
