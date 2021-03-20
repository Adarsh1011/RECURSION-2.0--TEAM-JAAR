from django import forms
from django.db.models import fields
from .models import Post, BedRequest

PREGNANT=[('Yes', 'Yes'), ('No', 'No')]
WEIGHT = [('light', 'till 30'), ('medium', 'from 30 to 70'), ('heavy', "above 70")]
GENDER = [('Male', 'Male'),('Female', 'Female'), ('Other', 'Other')]
CITY = [('Mumbai', 'Mumbai'), ('Pune', 'Pune')]
BOOKING = [(1, 'Allow Covid Bed Registration'),(2, 'Allow Bed Registration'), (3, 'Delete Entry')]

# class PostForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = ('name', 'content','weight', "pregnant", "anemia", "infectious_diseases", "doctors_prescription",
#             "days", "test", "covid"
#         )
#         widgets = {

#             'name' : forms.TextInput(attrs={'class':'form-control'}),
#             # 'category': forms.Select(choices=choice_list,attrs={'class':'form-control'}),
#             'content': forms.Textarea(attrs={'class':'form-control'}),
#             'covid_cap' : forms.Select(choices=ANEMIA, attrs={'class':'form-control'}),
#             'norm_cap': forms.Select(choices=ANEMIA,attrs={'class':'form-control'}),
        
#         }

class PostForm(forms.ModelForm):
    name =forms.CharField()
    content=forms.Textarea()
    covid_cap=forms.IntegerField(label='Number of covid beds?')
    norm_cap = forms.IntegerField(label='Number of covid beds?')
    city = forms.CharField(max_length=10 ,widget=forms.Select(choices=CITY))
    address = forms.Textarea()
    # Hospital=forms.CharField(max_length=10, label='Nearby hospitals?')
    # has_corona = forms.CharField(label='Was your COVID test positive?',widget=forms.Select(choices=PREGNANT))
    # is_donor = forms.BooleanField(required=False)
    # location = forms.CharField()

    class Meta:
        model = Post 
        fields = ['name', 'content', 'covid_cap', 'norm_cap', 'city',
                   'address'
                 ]

class BedForm(forms.ModelForm):
    aadhar_number =forms.IntegerField()
    phone_number =forms.IntegerField()
    name=forms.CharField(label='What is your name?')
    address=forms.CharField(label='What is your Address?')
    # proof=forms.ImageField()
    city=forms.CharField(label='What is your City?')
    pin_code =forms.IntegerField()
    gender=forms.CharField(label='What is your gender?',widget=forms.Select(choices=GENDER))
    age =forms.IntegerField()
    co_mobidity=forms.CharField(label='What are your comobidity?',widget=forms.Select(choices=GENDER))
    ambulance_required=forms.CharField(label='Do you require an ambulance?',widget=forms.Select(choices=PREGNANT))
    scheme=forms.CharField(label='What is your gender?',widget=forms.Select(choices=GENDER))

    # preferance=forms.CharField(label='What is your gender?',widget=forms.Select(choices=GENDER))
    # health_centre=forms.CharField(label='What is your gender?',widget=forms.Select(choices=GENDER))
    # district=forms.CharField(max_length=10)
    # Hospital=forms.CharField(max_length=10, label='Nearby hospitals?')

    tested = forms.CharField(label='Was your COVID test positive?',widget=forms.Select(choices=PREGNANT))

    # is_donor = forms.BooleanField(required=False)

    symptoms = forms.CharField()

    class Meta:
        model= BedRequest
        fields=('aadhar_number', 'name', 'phone_number', 'address' , 'city', 'pin_code',  'age', 'gender', 
             'co_mobidity', 'ambulance_required', 'scheme', 'tested','symptoms'
        #   'proof',
        )

class Booking(forms.ModelForm):
    choice=forms.CharField(widget=forms.Select(choices=BOOKING))
    class Meta:
        model= Post
        fields = ["choice"]

