from django.shortcuts import render
import requests,json
from .models import Contact

# Create your views here.
def index(request):
	if request.method == 'POST':
		firstname = request.POST.get('fname')
		lastname = request.POST.get('lname')
		print(firstname)

		r=requests.get('http://api.icndb.com/jokes/random?firstName='+ firstname +'&lastName='+ lastname)
		
		json_data = json.loads(r.text)
		joke = json_data.get('value').get('joke')
		context = {'joker':joke}


		return render(request, 'mysite/index.html',context)
	else:
		firstname = 'Abeed'
		lastname= 'Ahsan'
		print(firstname)

		r=requests.get('http://api.icndb.com/jokes/random?firstName='+ firstname +'&lastName='+ lastname)
		
		json_data = json.loads(r.text)
		joke = json_data.get('value').get('joke')
		context = {'joker':joke}

		return render(request, 'mysite/index.html',context)


def portfolio(request):

	return render(request, 'mysite/portfolio.html')

def contact(request):
	if request.method == 'POST':
		email_r = request.POST.get('email')
		subject_r = request.POST.get('subject')
		message_r = request.POST.get('message')

		c = Contact(Email=email_r,Subject=subject_r,Message=message_r)

		c.save()
		return render(request, 'mysite/thanks.html')

	else:
		return render(request, 'mysite/contact.html')

	
