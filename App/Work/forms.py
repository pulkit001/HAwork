from django import forms
from .models import Lost , Found

class LostForm(forms.ModelForm):
  class Meta:
    model = Lost
    fields = ['HostelN' , 'Article' , 'Date' , 'PlaceLost' , 'Name' , 'LDAP' , 'Contact' , 'AddressItem' , 'ImageLost']

    labels = { 'LDAP' : 'Official LDAP' , 'HostelN' : 'Hostel ' , 'Date': 'Date When Item Was Lost' , 'PlaceFound' : 'Place Where Item was Lost' , 'Name' : 'Your Name' ,'AddressItem': 'Your Address'}

    widgets = {'HostelN':forms.TextInput(attrs={'class':'form-control'}  ),'Article':forms.TextInput(attrs={'class':'form-control'}), 'Date':forms.TextInput(attrs={'class' : 'form-control' ,  'placeholder' : 'DD/MM/YYYY  HH:MM(in 24 Hour Format)' }),
    'PlaceLost':forms.TextInput(attrs={'class':'form-control'}),
    'Name':forms.TextInput(attrs={'class':'form-control'}) ,
    'LDAP':forms.TextInput(attrs={'class':'form-control'}) ,
    'Contact':forms.TextInput(attrs={'class':'form-control'}) ,
    'AddressItem':forms.TextInput(attrs={'class':'form-control'}) }

class FoundForm(forms.ModelForm):
  class Meta:
    model = Found
    fields = ['LDAP', 'HostelN' , 'Article' , 'Date' , 'PlaceFound' , 'Name' ,  'Contact' , 'AddressItem' ,'ImageFound']

    labels = { 'LDAP' : 'Official LDAP' , 'HostelN' : 'Hostel ' , 'Date': 'Date When Item Was Found' , 'PlaceFound' : 'Place Where Item was found' , 'Name' : 'Your Name' ,'AddressItem': 'Your Address'}

    widgets ={'LDAP':forms.TextInput(attrs={'class':'form-control'}) ,
    'HostelN':forms.TextInput(attrs={'class':'form-control'}),'Article':forms.TextInput(attrs={'class':'form-control'}), 'Date':forms.TextInput(attrs={'class':'form-control' , 'placeholder' : 'DD/MM/YYYY  HH:MM(in 24 Hour Format)' }),
    'PlaceFound':forms.TextInput(attrs={'class':'form-control'}),
    'Name':forms.TextInput(attrs={'class':'form-control'}) ,
    'Contact':forms.TextInput(attrs={'class':'form-control'}) ,
    'AddressItem':forms.TextInput(attrs={'class':'form-control'})}
