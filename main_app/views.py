# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

time_stamp = 0
latitude = 10.7905
longitude = 78.7047

# def json_response(func):
#     """
#     A decorator thats takes a view response and turns it
#     into json. If a callback is added through GET or POST
#     the response is JSONP.
#     """
#     def decorator(request, *args, **kwargs):
#         objects = func(request, *args, **kwargs)
#         if isinstance(objects, HttpResponse):
#             return objects
#         try:
#             data = simplejson.dumps(objects)
#             if 'callback' in request.REQUEST:
#                 # a jsonp response!
#                 data = '%s(%s);' % (request.REQUEST['callback'], data)
#                 return HttpResponse(data, "text/javascript")
#         except:
#             data = json.dumps(str(objects))
#         return HttpResponse(data, "application/json")
#     return decorator

# def index(request):
# 	return HttpResponse("Index")

@csrf_exempt
def set_cords(request):
	global time_stamp
	global longitude
	global latitude
	if request.method == "POST":
		time_stamp = request.POST.get("time_stamp")
		longitude = request.POST.get("long")
		latitude = request.POST.get("latitude")
	print time_stamp, latitude, longitude
	return HttpResponse("Done!")

def index(request):
	#return HttpResponse("Index")
	return render(request, 'index.html', 
{"latitude" : latitude, "timestamp" : time_stamp, "longitude" : longitude})

# @json_response
def get_cords(request):
	global time_stamp
	global longitude
	global latitude
	if request.method == "GET":
		response_data = {}
		response_data['timestamp'] = time_stamp
		response_data['latitude'] = latitude
		response_data['longitude'] = longitude
		return HttpResponse(json.dumps(response_data), content_type="application/json")
	return HttpResponse("Not valid")