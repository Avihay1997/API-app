import requests

def fetch_parts_data():
    url = "https://api.pcpartpicker.com/v1/parts"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Unable to fetch data from API"}
