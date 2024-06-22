from django import forms
from testapp.models import User
from django.contrib.auth.forms import UserChangeForm ,PasswordChangeForm




class signupform(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'first_name','last_name','password','mobile']


class EditProfileForm(UserChangeForm):  
    email = forms.EmailField(disabled=True,widget=forms.EmailInput(attrs={'class':'form-control' }))
    first_name = forms.CharField(max_length=240,widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=240,widget=forms.TextInput(attrs={'class':'form-control'}))
    mobile = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control'}))
    password =  forms.CharField(max_length=250,widget=forms.TextInput(attrs={'class':'form-control','type':'hidden'}))

    class Meta:
        model = User
        fields = ('email','first_name','last_name','mobile','password')

class PasswordChangingForm(PasswordChangeForm):  
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','type':'password' }), required=True)
    new_password1 = forms.CharField(max_length=240,widget=forms.PasswordInput(attrs={'class':'form-control','type':'password'}), required=True)
    new_password2 = forms.CharField(max_length=240,widget=forms.PasswordInput(attrs={'class':'form-control','type':'password'}), required=True)
    def clean_new_password1(self):
       old_password = self.cleaned_data.get('old_password')
       new_password1 = self.cleaned_data.get('new_password1')
        
       if old_password == new_password1:
            raise forms.ValidationError("New password should not be the same as the old password.")
        
       return new_password1

    class Meta:
        model = User
        fields = ('old_password','new_password1','new_password2')        


class UserChangePass(forms.Form):
    old_pass = forms.CharField(widget=forms.PasswordInput),
    new_pass1 = forms.CharField(max_length=240,widget=forms.PasswordInput, required=True),
    new_pass2 = forms.CharField(label='Password(again)',widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        valpwd=self.cleaned_data['new_pass1']
        valpwds=self.cleaned_data['new_pass2']

        if valpwd != valpwds:
            raise forms.ValidationError('password does not match')