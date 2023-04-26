from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
tax_rate= 0.15
"""
def index(inputN):
	return HttpResponse(f"the tax rate is : {tax_rate*100}%")
def index2(inputN):
	return HttpResponse("this is a site to calculate tax")

def index3(inputN,number):

	x = tax_rate*number


	return HttpResponse(f"the number after tax is:{x+number}")
	"""
def index2(request):
	return render (request, "hello/defult.html")

def index(inputN):
	return render (inputN, "hello/taxrateDis.html",{"taxRate":(tax_rate*100)})
def index3(inputN,number):
	number = float(number)
	return render (inputN, "hello/number.html",{"number":(number+(number*tax_rate))})
	