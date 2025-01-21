import configparser

import requests
from Utilities.Configurations import *


uti_Response = requests.get(getConfig()['API']['endpoint'] + "?key=qaclick123&place_id=d2922b270ca63d84d6750a312a2a90a2")
print(uti_Response.status_code)
print(uti_Response.json())

