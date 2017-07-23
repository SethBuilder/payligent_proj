from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import json
from django.core.mail import send_mail, BadHeaderError

def index(request):
	return render(request, 'payligent/index.html', {})



def send_me_email(subject, message, to_email):
	"""Used so I receive emails when a new user signs up or does other things like send feedback"""
	try:
		send_mail(subject,  message, '', to_email)
	except BadHeaderError:
		return HttpResponse('Invalid header found.')


def send_message(request):
	fullname = request.POST.get('fullname','')
	email = request.POST.get('email','')
	phone = request.POST.get('phone','')
	message = request.POST.get('message','')
	whole_message = "fullname: " + fullname + "\nemail: " + email + "\nphone: " + \
	phone + "\nmessage: " + message
	response_data = {}
	# try:
	response_data['message'] = "We have received your message!"
	send_me_email("New client message from Payligent.com" , whole_message, ['moghrabi@gmail.com', 'mughrabi@gmail.com'])
	# except:
	# 	response_data['message'] = 'Oh Snap! message was not sent correctly,'
	return HttpResponse(json.dumps(response_data), content_type='application/json')

def subscribe(request):
	email = request.POST.get('sub_email','')
	response_data = {}
	response_data['message'] = "We have received your email!"
	message = "subscribed email: " + email
	send_me_email("New subscription from Payligent.com" , message, ['moghrabi@gmail.com'])
	return HttpResponse(json.dumps(response_data), content_type='application/json')