import json

import requests

def test_getCall():
        response = requests.get("https://reqres.in/api/users?page=2")
        print(response.json()) # it is return the response in the form of json

def test_singleUser():
    resp = requests.get("https://reqres.in/api/users/2")
    output = resp.json()
    print(output)
    print("Decoded JSON Data From File")
    for key, value in output.items():
        print(key, ":", value)
    print("Done reading json file")

    keylist = output.keys()
    print(keylist)

    values_list = output.values()
    print(values_list)
    for value in values_list:
        #print("this is output ",value['email'])
           if value['email']=="janet.weaver@reqres.in":
               print(value['email'])
               break

def test_getCallFail():
    resp = requests.get("https://reqres.in/api/unknown/23")
    assert resp.status_code == 200
