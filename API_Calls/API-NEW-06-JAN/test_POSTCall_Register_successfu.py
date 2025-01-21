import jsonpath
import requests
import json

def test_PostCall():
            url = "https://reqres.in/api/users"
            file = open("C:\\Nishant_Study\\nopcommerce\\nopcommerceAdmin\\TestData\\PostCallRegisterSuccessful.json", 'r')
            json_input = file.read()  # data is read in string format
            request_json = json.loads(json_input)
            print(request_json)
            response = requests.post(url, request_json)
            assert response.status_code == 201
            # Fetch header from response
            print(response.headers.get("Content-Length"))
            # Parse the response to json format
            response_json = json.loads(response.text)  # parse response converting into json format
            print(response_json)
            print("------------------------------------------------------------")
            id = jsonpath.jsonpath(response_json, 'id')
            print(id[0])