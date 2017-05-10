import requests
import time

while 1:
	lat = raw_input()
	lon = raw_input()
	ts = time.time()

	payload = {'time_stamp' : str(ts), 'latitude' : str(lat), 'long' : str(lon)}
	r = requests.post("http://127.0.0.1:8000/set_cords/", data = payload)
	print r