from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def post_create(self):
	return HttpResponse("<h1>Create</h1>")

def post_detail(self):
	return HttpResponse("<h1>Detail</h1>")

def post_list(self):
	return HttpResponse("<h1>List</h1>")

def post_update(self):
	return HttpResponse("<h1>Update</h1>")

def post_delete(self):
	return HttpResponse("<h1>Delete</h1>")	
