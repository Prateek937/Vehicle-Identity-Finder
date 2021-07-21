import requests
import json

BASE = 'http://127.0.0.1:5000/'


data = [{'Registration': 'KA05NB1786', 
        'Owner': 'WASIM AHMAD', 
        'Maker': 'SELTOS/ KIS', 
        'Vehicle': 'MOTOL CAR ', 
        'Fuel_Type': 'DEIESEL', 
        'Chassis': 'MZBEN813LLN16XXXXX', 
        'Engine_Number': 'D4FALM08XXXXX', 
        'Registration_Date': '23-10-2020', 
        'Insurance_Valid_Upto': '21-OCT-2023'
    }
]

for i in range(len(data)):
    response = requests.put(BASE + "vehicle/" + data[i]['Registration'], data[i])
    print(response.json())

input()

response = requests.get(BASE + "vehicle/"+ data[0]['Registration'])

print(json.dumps(response.json(), indent=1))
