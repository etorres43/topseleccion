from django.contrib.auth.models import User
from .models import Main_post
from django import forms

class SearchForm(forms.Form):
	search_field = forms.CharField(label="search", max_length=20, widget=forms.TextInput(attrs={'placeholder':'Search','class':'form-control',"style":'width:120%'}))

class PcommentForm(forms.Form):
	name = forms.CharField(label="username", max_length=20,widget=forms.TextInput(attrs={'style': 'width:100%', 'placeholder':'Nombre (requerido)'}))
	email = forms.EmailField(label="email", max_length=50,widget=forms.EmailInput(attrs={'style': 'width:100%', 'placeholder':'Email (requerido)'}))
	website = forms.CharField(label="website", max_length=20,widget=forms.TextInput(attrs={'style': 'width:100%', 'placeholder':'Website'}))
	p_comment = forms.CharField(label="p_comment", widget=forms.TextInput(attrs={'style': 'width:100%; Height:80px', 'placeholder':'Ingrese su comentario aqui','id':'p_comment'}))
	RADIO_CHOICES = (
		('1','Si',),('0','No',))
	subscribe = forms.ChoiceField(widget=forms.RadioSelect(attrs={'type':'button',}), choices=RADIO_CHOICES)
	
class ScommentForm(forms.Form):
	name = forms.CharField(label="username", max_length=20,widget=forms.TextInput(attrs={'style': 'width:100%', 'placeholder':'Nombre (requerido'}))
	email = forms.EmailField(label="email", max_length=50,widget=forms.EmailInput(attrs={'style': 'width:100%', 'placeholder':'Email (requerido)'}))
	website = forms.CharField(label="website", max_length=20,widget=forms.TextInput(attrs={'style': 'width:100%', 'placeholder':'Website'}))
	s_comment = forms.CharField(label="s_comment", widget=forms.TextInput(attrs={'style': 'width:100%; Height:80px', 'placeholder':'Ingrese su comentario aqui','id':'s_comment'}))
	RADIO_CHOICES = (
		('1','Si',),('0','No',))
	subscribe = forms.ChoiceField(widget=forms.RadioSelect(attrs={'type':'button',}), choices=RADIO_CHOICES)
