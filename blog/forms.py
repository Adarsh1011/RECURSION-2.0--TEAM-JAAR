from django import forms
from .models import Post

ANEMIA=[('Mumbai','Mumbai'),('no','No')]
WEIGHT = [('light', 'till 30'), ('medium', 'from 30 to 70'), ('heavy', "above 70")]

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
    city = forms.CharField(max_length=10 ,widget=forms.Select(choices=ANEMIA))
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