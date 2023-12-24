import requests
from datetime import datetime
endpoint_pixela="https://pixe.la/v1/users"

params_pixela={
    "token":"djnwkfkjcdfv4345ty566",
    "username":"kubratest",
    "agreeTermsOfService": "yes",
    "notMinor":"yes"
}

USERNAME="kubratest"
TOKEN="djnwkfkjcdfv4345ty566"
GRAPH_ID="graph11"

# response= requests.post(url=endpoint_pixela, json=params_pixela)
# print(response.text)

endpoint_graph=f"{endpoint_pixela}/{USERNAME}/graphs"

graph_config={
    "id":"graph11",
    "name":"Work",
    "unit":"Hours",
    "type":"float",
    "color":"sora"
}

header={
    "X-USER-TOKEN":TOKEN
}
# response = requests.post(url=endpoint_graph,json=graph_config, headers=header)
# print(response.text)

# create endpoint

pixel_creation_endpoint=f"{endpoint_pixela}/{USERNAME}/graphs/{GRAPH_ID}"

today=datetime.now()

pixel_data={
    "date": today.strftime("%Y%m%d"),
    "quantity":input("How many hours did you work today?:"),
}

# response= requests.post(url=pixel_creation_endpoint,json=pixel_data,headers=header)
# print(response.text)

# http request: get,post,put,delete

# put request
update_endpoint=f"{endpoint_pixela}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixel_data={
    "quantity":"9"
}

response= requests.put(url=update_endpoint, json=pixel_data, headers=header)
print(response.text)

# delete request
delete_endpoint=f"{endpoint_pixela}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

response= requests.put(url=delete_endpoint, headers=header)
print(response.text)
