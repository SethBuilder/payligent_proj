from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import json
from django.core.mail import send_mail, BadHeaderError

# INDEX PAGE
def index(request):
	return render(request, 'payligent/index.html', {})


# EMAIL SENDING FUNCTION
def send_me_email(subject, message, to_email):
	"""Used so I receive emails when a new user signs up or does other things like send feedback"""
	try:
		send_mail(subject,  message, '', to_email)
	except BadHeaderError:
		return HttpResponse('Invalid header found.')

# contact form view
def send_message(request):
	""" sends data filled in the contact form via ajax  """
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

# subscribe view (in the footer)
def subscribe(request):
	""" when users subscribe this view sends their email address as an email """
	email = request.POST.get('sub_email','')
	response_data = {}
	response_data['message'] = "We have received your email!"
	message = "subscribed email: " + email
	send_me_email("New subscription from Payligent.com" , message, ['moghrabi@gmail.com'])
	return HttpResponse(json.dumps(response_data), content_type='application/json')

# subscribe to gold/silver/bronze package
def signup(request, level):
	""" when users subscribe to a package """
	context_dict = {}
	response_data = {}
	context_dict['level'] = level
	if request.method == 'POST':
		phone = request.POST.get('phone', '')
		email = request.POST.get('email','')
		lname = request.POST.get('lname','')
		fname = request.POST.get('fname','')
		comname = request.POST.get('comname','')
		comurl = request.POST.get('comurl','')
		comemail = request.POST.get('comemail','')
		address = request.POST.get('address','')
		level = request.POST.get('level','')
		

		response_data['message'] = "We have received your email!"
		whole_message = "first name: " + fname + "\nlast name: " + lname + "\nemail: " + email + "\nphone: " + \
	phone + "\ncompany name: " + comname + '\ncompany email: ' + comemail + '\nlevel: ' + level + "\naddress: " + address
		send_me_email("New " + level  + " package signup!", whole_message, ['moghrabi@gmail.com'])
		return HttpResponse(json.dumps(response_data), content_type='application/json')

	return render(request, 'payligent/signup.html', context_dict)


