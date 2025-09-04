# Use DataFrame.from_dict() to Convert JSON to DataFrame
import pandas as pd
import json
from pandas import json_normalize

json_string = '{ "Courses": "Spark", "Fee": 22000,"Duration":"40Days"}'
data = json.loads(json_string)

# Use pandas.DataFrame.from_dict() to Convert JSON to DataFrame
df2 = pd.DataFrame.from_dict(data, orient="index")
print(df2)
with open("data.json", 'r', encoding="utf-8") as json_file:
    
    
    data = json.load(json_file)