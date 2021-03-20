from django import forms
from .models import Post,Category, Donation, BedRequest

choices = Category.objects.all().values_list('name','name')

choice_list =[]
symptom_list=[]
tested_list=['yes','no']
centre_list=[]
scheme_list=[]
mobidity_list=[]
gender_list=['Male','Female','others']
city_list=[]

GENDER=[('male','Male'),('female','Female'),('others','Others'),]
BLOODGROUP=[('O+','O+'),('A+','A+'),('B+','B+'),('AB+','AB+'),('O-','O-'),('A-','A-'),('B-','B-'),('AB-','AB-'),]
PREGNANT=[('yes','Yes'),('no','No')]
ANEMIA=[('yes','Yes'),('no','No')]

for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model= Post
        fields=('title','category','content')

        widgets = {

            'title' : forms.TextInput(attrs={'class':'form-control'}),
            'category': forms.Select(choices=choice_list,attrs={'class':'form-control'}),
            'content': forms.Textarea(attrs={'class':'form-control'})
        
        }

class Form(forms.ModelForm):
    quantity= forms.IntegerField()
    class Meta:
        model= Donation
        fields=('quantity',)

# class BedForm(forms.ModelForm):
#     class Meta:
#         model= BedRequest
#         fields=('aadhar_number','phone_number','name', 'address' , 'proof', 'city', 'pin_code', 'gender', 'age'
#         ,'co_mobidity', 'ambulance_required', 'scheme','preferance','health_centre','tested','symptoms')

#         widgets = {

            
#             # 'aadhar_number' : forms.TextInput(attrs={'class':'form-control'})
#             # 'phone_number' : forms.IntegerField(attrs={'class':'form-control'})
#             'name': forms.TextInput(attrs={'class':'form-control'}),
#             'address' : forms.TextInput(attrs={'class':'form-control'}),
#             # 'proof': forms.ImageField()
#             'city': forms.Select(choices=city_list,attrs={'class':'form-control'}),
#             # 'pin_code':forms.IntegerField(attrs={'class':'form-control'})
#             'gender': forms.Select(choices=gender_list,attrs={'class':'form-control'}),
#             # 'age': forms.IntegerFiled(attrs={'class':'form-control'})
#             'co_mobidity' : forms.Select(choices=mobidity_list,attrs={'class':'form-control'}),
#             'ambulance_required' : forms.Select(choices=tested_list,attrs={'class':'form-control'}),
#             'scheme' : forms.Select(choices=scheme_list,attrs={'class':'form-control'}),
#             'preferance' : forms.Textarea(attrs={'class':'form-control'}),
#             'health_centre' : forms.Select(choices=centre_list,attrs={'class':'form-control'}),
#             'tested' : forms.Select(choices=tested_list,attrs={'class':'form-control'}),
#             'symptoms' : forms.Select(choices=symptom_list,attrs={'class':'form-control'}),
        
#         }


class BedForm(forms.ModelForm):
    aadhar_number =forms.IntegerField()
    phone_number =forms.IntegerField()
    name=forms.CharField(label='What is your name?')
    address=forms.CharField(label='What is your Address?')
    proof=forms.ImageField()
    city=forms.CharField(label='What is your City?')
    pin_code =forms.IntegerField()
    gender=forms.CharField(label='What is your gender?',widget=forms.Select(choices=GENDER))
    age =forms.IntegerField()
    co_mobidity=forms.CharField(label='What are your comobidity?',widget=forms.Select(choices=mobidity_list))
    ambulance_required=forms.CharField(label='Do you require an ambulance?',widget=forms.Select(choices=PREGNANT))
    scheme=forms.CharField(label='What is your gender?',widget=forms.Select(choices=GENDER))
    preferance=forms.CharField(label='What is your gender?',widget=forms.Select(choices=GENDER))
    health_centre=forms.CharField(label='What is your gender?',widget=forms.Select(choices=GENDER))
    # district=forms.CharField(max_length=10)
    # Hospital=forms.CharField(max_length=10, label='Nearby hospitals?')
    tested = forms.CharField(label='Was your COVID test positive?',widget=forms.Select(choices=PREGNANT))
    # is_donor = forms.BooleanField(required=False)
    symptoms = forms.CharField()

    class Meta:
        model= BedRequest
        fields=('aadhar_number','phone_number','name', 'address' , 'proof', 'city', 'pin_code', 'gender', 'age'
        ,'co_mobidity', 'ambulance_required', 'scheme','preferance','health_centre','tested','symptoms')

         