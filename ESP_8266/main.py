"""

import time


import urequests as requests
import ujson
import json

mac_adress = "255.255.255.1";

while True:
  import random
  rand_num = random.getrandbits(5)
  get_user_request_header = {'Authorization': 'Token 852501d5336397bfe0be496236bd016b6f402436','Content-Type': 'application/json'}
  data = {'value': rand_num, 'mac' : mac_adress}
  request_url = 'http://192.168.1.28:8000/devicelogs/'
  res = requests.post(request_url, headers = get_user_request_header, data = ujson.dumps(data))
  print(res.text)
  led.value(0)
  time.sleep(1)
  led.value(1)
  time.sleep(10)





"""

