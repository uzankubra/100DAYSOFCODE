import requests

def get_iss_location():
    api_url = "http://api.open-notify.org/iss-now.json"


    response = requests.get(api_url)

    # check
    if response.status_code == 200:
        data = response.json()
        latitude = data['iss_position']['latitude']
        longitude = data['iss_position']['longitude']
        print(f"ISS'nin güncel konumu: Enlem {latitude}, Boylam {longitude}")
    else:
        print(f"Hata: {response.status_code}")


get_iss_location()
