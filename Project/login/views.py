from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.sessions.models import Session
from django.utils import timezone
from django.core.exceptions import ValidationError
import datetime
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage
import Image
import imghdr
import os
import os.path


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
					request.session['fullname'] = user.get_full_name()
					
					request.session['auth'] = '1'

					last_logged = timezone.now() 
					
					#METHOD FOR STORING LATEST IP ADDRESSES OF USER
					n = User.objects.get(username=user.username)
					ip_ad = request.META.get('REMOTE_ADDR')	
					n.profile.ip_address = str(ip_ad)
					n.profile.save()

					userid = request.session['user_id']
   					fullname = user.get_full_name()

   					userauth = str(user.profile.user_auth)

   					userimage = 'wiki/images/' + user.username + '.jpeg'
   					testimage = 'wiki/static/' + userimage

   					#VALIDATES FILE EXISTS
   					if os.path.isfile(testimage) == False:
   						userimage = 'wiki/images/guest.gif'

   					context = {'userauth': userauth,'userid': userid, 'fullname':fullname, 'userimage': userimage}
					return render(request, 'wiki/wiki.html', context)
  				error = 'DISABLED ACCOUNT'
				context = {'error': error}
				return render(request, 'wiki/wiki.html', context)
			else:
				error = 'INVALID USER'
				context = {'error': error}
				return render(request, 'wiki/wiki.html', context)
		
		except:
			error = 'INVALID USER'
			context = {'error': error}
			return render(request, 'wiki/wiki.html', context)
	return render(request, 'wiki/wiki.html')


def guest(request):

	ip_ad = request.META.get('REMOTE_ADDR')
	username = str(ip_ad)
	password = '12345'

	#AUTHENTICATES USER
	user = authenticate(username = username, password = password)
	userimage = 'wiki/images/guest.gif'
	#IF THE USER EXISTS AND IS ACTIVE, LOG USER IN
	if user is not None:
		user.profile.ip_address = ip_ad
		login(request,user)
		request.session['user_id'] = user.id #SESSION VALUE COBTAINING ID OF USER
		request.session['logged_in'] = True #SESSION VALUE INDICATING IF A USER IS LOGGED IN
		request.session['fullname'] = user.profile.ip_address
		request.session['auth'] = str(user.profile.user_auth)
		userauth = str(user.profile.user_auth)
		userid = user.id
		fullname = user.profile.ip_address
		context = {'userauth':userauth,'userid': userid, 'fullname':fullname, 'userimage': userimage}
		return render(request, 'wiki/wiki.html', context)


	else:
		new_user = User.objects.create_user(username=username, password = '12345', first_name = 'Guest', last_name = 'Guest', email = 'guest@wiki.com')
		new_user.profile.user_auth = 0
		new_user.profile.ip_address = ip_ad
		new_user.profile.save()
		return guest(request)
		









def logout_view(request):
		try:
			current_user = User.objects.filter(pk=request.session['user_id'])[0]
			session_response = ''
			
			if request.session['logged_in'] == True:
				session_response = request.session['user_id']
				request.session.flush()
				logout(request)
				return render(request, 'wiki/wiki.html')
			else:
				error = "Not logged in"
				context = { 'error': error}
				return render(request, 'wiki/wiki.html',context)
		except KeyError:
			return render(request,'wiki/wiki.html')



def register_view(request):
	if request.method == 'POST':
		#method for testing if another username like that exists for adding a user
		count =0
		check_user_name = request.POST['username_text']
		#iterates through USER objects and compares input
		for user in User.objects.all():
			if (check_user_name == user.username): 
				count=count+1
				error = "USERNAME ALREADY EXISTS"
				context = { 'error': error}
				return render(request, 'register_page.html',context)

				

		#GET THE USERs NEW INFORMATION
		new_password = request.POST.get('password_text')
		new_firstname = request.POST.get('first_name_text')
		new_lastname = request.POST.get('last_name_text')
		new_email = request.POST.get('email_text')
		new_bday = request.POST.get('bday_text')
		new_description = request.POST.get('description_text')
		
		if validate_bday(new_bday) == 0:
			error = "INVALID BIRTHDAY"
			context = { 'error': error}
			return render(request, 'register_page.html',context)

		if validate_pic(request) == 'nofile':
			load_file =True
		else:
			if validate_pic(request) == 'noimage':
				error = 'INVALID BIRTHDAY'
				context = { 'error': error}
				return render(request, 'register_page.html',context)
			else:
				remove_path = 'wiki/static/wiki/images/' + str(user.username) + '.jpeg'
				if os.path.isfile(remove_path):
					os.remove(remove_path)
				new_pic = request.FILES['profilepic']
				default_storage = FileSystemStorage(location='wiki/static/wiki/images/')
				path = default_storage.save(user.username +'.jpeg', ContentFile(new_pic.read()))	
							
		

		#CREATES NEW USER OBJECT
		new_user = User.objects.create_user(username=check_user_name, password = new_password, first_name = new_firstname, last_name = new_lastname, email = new_email)
		
		#Fetches the new user object and adds additional information
		n = User.objects.get(username=check_user_name)
		n.profile.description = new_description
		n.profile.birthdate = validate_bday(new_bday)
		
		#SAVE THE PATH FOR THE USER
		n.profile.save()
		return render(request, 'wiki/wiki.html')
		
		

	return render(request, 'register_page.html')


def edit_profile(request):
	uauth = request.session['auth']
	profilepage = True

	##
	userid = request.session['user_id']
	fullname = request.session['fullname']
	myuser = User.objects.get(pk=userid)
	userauth = str(myuser.profile.user_auth)
	userimage = 'wiki/images/' + myuser.username + '.jpeg'
	remove_path = 'wiki/static/wiki/images/' + str(myuser.username) + '.jpeg'
	if os.path.isfile(remove_path):
		os.remove(remove_path)
	else:
		userimage = 'wiki/images/guest.gif'


	if (uauth == '1') or (uauth == '2'):
		edit_user = User.objects.get(pk=request.user.id)
		username = edit_user.username
		firstname = edit_user.first_name
		lastname = edit_user.last_name
		email = edit_user.email

		birthdate = str(edit_user.profile.birthdate)
		
		description = edit_user.profile.description
		if request.method == 'POST':
			password = request.POST.get('password_text')
			user = authenticate(username = username, password = password)
			if user is not None:
				if user.is_active:
					new_firstname = request.POST.get('first_name_text')
					new_lastname = request.POST.get('last_name_text')
					new_email = request.POST.get('email_text')
					new_bday = request.POST.get('bday_text')
					new_description = request.POST.get('description_text')
					new_password = request.POST.get('new_password_text')

					edit_user.first_name = new_firstname
					edit_user.last_name = new_lastname
					edit_user.email = new_email


					if validate_bday(new_bday) == 0:
						error = 'INVALID BIRTHDAY'
						context = { 'error': error}
						return render(request, 'profile.html',context)

					if validate_pic(request) == 'nofile':
						load_file =True
					else:
						if validate_pic(request) == 'noimage':
							error = 'INVALID IMAGE'
							context = { 'error': error}
							return render(request, 'profile.html',context)
						else:
							remove_path = 'wiki/static/wiki/images/' + str(user.username) + '.jpeg'
							if os.path.isfile(remove_path):
								os.remove(remove_path)
							new_pic = request.FILES['profilepic']
							default_storage = FileSystemStorage(location='wiki/static/wiki/images/')
							path = default_storage.save(user.username +'.jpeg', ContentFile(new_pic.read()))	
							

					edit_user.profile.birthdate = validate_bday(new_bday)
					edit_user.profile.description = new_description
					
					if new_password != '':
						edit_user.set_password(new_password)

					edit_user.save()
					edit_user.profile.save()
					logout_view(request)
					return render(request, 'wiki/wiki.html')
					
			else:
				return render(request, 'wiki/wiki.html')
		else:

			context = {'userimage':userimage,'fullname':fullname,'profilepage': profilepage,'username': username, 'firstname': firstname, 'lastname': lastname, 'email': email, 'birthdate': birthdate, 'description': description}
			return render(request, 'profile.html', context)
	else:
		return render(request, 'wiki/wiki.html')
	




#VALIDATES BIRTHDAY FIELD INPUT
def validate_bday(bday):
		date=''
		for char in bday:
			if char.isdigit():
				date = date + char


		if len(date) != 8:
			return 0
		
		else:
			
			year = date[:4]
			month = date[4:6]
			day = date[6:]
			now = datetime.datetime.now()

			#VALIDATE YEAR
			now_year = now.year
			if (int(year) > int(now_year)):
				return 0
			else:
				if int(month) > 12:
					return 0
				else:
					short_months = ['04', '06', '09' , '11']
					long_months = ['01','03','05','07','08','10','12']
					if month in long_months:
						if int(day) > 31:
							return 0
					else:
						if month in short_months:
							if int(day) > 30:
								return 0
						else:
							#LEAP YEAR VALIDATOR
							if (int(year) % 4) == 0:
								if (int(year) % 100) == 0:
									if (int(year) % 400 )== 0:
										leap_year =True
									else:
										leap_year = 0
								else:
									leap_year = True
							else:
								leap_year = 0

							if leap_year == 0:
								if (int(day) > 29):
									return 0
							else:
								if (int(day) > 28):
									return 0
			#RETURN CLEAN DATE FOR DB STORAGE
			clean_date = year +'-'+month+'-'+day								
		return 	clean_date							
				

def validate_pic(request):
	try:
		pic =request.FILES['profilepic']  #REQUEST FILE
		file_type = imghdr.what(pic)	#GET IMAGE FILE TYPE
		if file_type == None: #VALIDATE FILE IS AN IMAGE
			return 'noimage'
		else:
			return 'valid'	
	except:
		return 'nofile'






			
				

