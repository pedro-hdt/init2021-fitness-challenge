from dotenv import load_dotenv
import os
import requests

load_dotenv()
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
REFRESH_TOKEN = os.getenv('REFRESH_TOKEN')
USER_ID = os.getenv('USER_ID')

weight_to_log = 65

# POST weight to the Fitbit API
res = requests.post(
    f'https://api.fitbit.com/1/user/{USER_ID}/body/log/weight.json',
    headers={
        'Authorization': 'Bearer ' + ACCESS_TOKEN,
    },
    data={
        'weight': weight_to_log,
        'date': '2021-06-29'
    }
)
res.raise_for_status()

print(res.json())