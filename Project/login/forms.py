

class ImageUploadForm(forms.Form):
	image = forms.ImageField()

class RegisterForm(forms.Form):
			username_text = forms.CharField(max_length=100)
			password_text = forms.CharField()
			first_name_text = forms.CharField()
			last_name_text  =forms.CharField()
			email_text = forms.EmailField()
			'''
			<input type="date" name="bday_text">
			<textarea name='description_text' id = 'id_descrpt'>Short Description</textarea>
			<input type="file" name="profile_pic" accept="image/*">
			<input type='submit' value='REGISTER' />'''
