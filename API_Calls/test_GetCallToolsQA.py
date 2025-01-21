
import requests

def test_getCall():
        resp = requests.get("https://demoqa.com/BookStore/v1/Books")
        print("This is status code :",resp.status_code)
        print("This is text code :", resp.text)
        print("This is header code :", resp.headers['Content-Type'])
        print("This is cookies code :", resp.cookies)
        print("This is json response code :", resp.json())
        print("This is connection code :", resp.connection)
