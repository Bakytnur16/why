from django.shortcuts import render
from django.http import HttpResponseRedirect
#from django.http import HttpResponse
from . import models
# Create your views here.
def index(request):
	return render(request,'home/index.html')

def main(request):
	return render(request,'home/main.html')
#def register(request):
#	return Htt pResponse('Registration success !')

def message(request):
  messages = models.Message.objects.all()
  return render(request, 'home/message.html', {'messages' : messages})


	


	#return render(request, )