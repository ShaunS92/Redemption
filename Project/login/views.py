from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.sessions.models import Session
from django.utils import timezone




def home_view(request):
	try:
		if request.user.is_active: #MUST USE ON EVERY PAGE
				current_user = request.session['user_id']
				current_status = request.session['logged_in']
				return HttpResponse('User ID: ' + str(current_user) + ' Online: ' + str(current_status)) #+ 'LAST_LOGGED: ' + lastlogged.last_logged)
		else:
				return HttpResponse('Please Login')
	except KeyError:
		return HttpResponse("Not Logged In")

	



def login_view(request):
	
	if request.method == 'POST':

		try:
			#RETRIEVES INPUT VALUES FROM TEMPLATE
			username = request.POST['username_text']
			password = request.POST['password_text']
			current_user = User.objects.get(username=username)

			#AUTHENTICATES USER
			user = authenticate(username = username, password = password)

			#IF THE USER EXISTS AND IS ACTIVE, LOG USER IN
			if user is not None:
				if user.is_active:
					login(request,user)
					request.session.set_expiry(0) #SETS THE SESSION TO EXPIRE ON BROWSER CLOSE
					request.session['user_id'] = user.id #SESSION VALUE COBTAINING ID OF USER
					request.session['logged_in'] = True #SESSION VALUE INDICATING IF A USER IS LOGGED IN
					last_logged = timezone.now() 
					
					#METHOD FOR STORING LATEST IP ADDRESSES OF USER
					n = User.objects.get(username=user.username)
					ip_ad = request.META.get('REMOTE_ADDR')	
					n.profile.ip_address = str(ip_ad)
					n.profile.save()
   					
   			

					return HttpResponse('User: ' + user.username + '  ID:' + str(request.session['user_id']) + '  LOGGED_ON: ' + str(request.session['logged_in'])+' TIME: ' + str(last_logged) )
					#return render(request, 'home.html')
				return HttpResponse('Disabled Account')
			else:
				return HttpResponse('Invalid Login')
		except:
			return HttpResponse("ERROR")
	return render(request, 'login_page.html')



def logout_view(request):
	
	if request.user.is_active:
		current_user = User.objects.filter(pk=request.session['user_id'])[0]
		session_response = ''
		try:
			if request.session['logged_in'] == True:
				session_response = request.session['user_id']
				request.session.flush()
				logout(request)
				return HttpResponse("Logged out USER:" + current_user.username + ' '+ str(session_response))
			else:
				return HttpResponse("You are not logged in")
		except KeyError:
			pass
		return render(request, 'home.html') 
	else:
		return HttpResponse("You are not logged in")
	

def register_view(request):
	if request.method == 'POST':
		#method for testing if another username like that exists for adding a user
		count =0
		check_user_name = request.POST['username_text']
		#iterates through USER objects and compares input
		for user in User.objects.all():
			if (check_user_name == user.username): 
				count=count+1
				return HttpResponse("ERROR: USERNAME ALREADY EXISTS, DO YOU WANT TO USE: " +user.username +  str(count))


		#GET THE USERs NEW INFORMATION
		new_password = request.POST.get('password_text')
		new_firstname = request.POST.get('first_name_text')
		new_lastname = request.POST.get('last_name_text')
		new_email = request.POST.get('email_text')
		new_bday = request.POST.get('bday_text')
		new_description = request.POST.get('description_text')
		


		#CREATES NEW USER OBJECT
		new_user = User.objects.create_user(username=check_user_name, password = new_password, first_name = new_firstname, last_name = new_lastname, email = new_email)
		
		#Fetches the new user object and adds additional information
		n = User.objects.get(username=check_user_name)
		n.profile.description = new_description


		#NEEDS VALIDATION NB!!!!!
		n.profile.birthdate = new_bday


		n.profile.save()
		testsave = User.objects.get(username=check_user_name)
		

		return HttpResponse('RATING:' + testsave.profile.description+  "  Name:" + new_user.first_name+ "  " + new_user.last_name + " USERNAME:"  + new_user.username + " PWORD: " + new_user.password + " email: " + new_user.email +"// SUCCESSFULLY ADDED TO THE DB")

	return render(request, 'register_page.html')
