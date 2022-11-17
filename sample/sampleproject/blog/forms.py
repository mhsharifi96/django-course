from django.utils.translation import gettext_lazy as _


from django import forms
from .models import Comment,Category


#https://docs.djangoproject.com/en/4.1/topics/forms/
class commentForm(forms.Form):
    email = forms.EmailField(max_length=254)
    title = forms.CharField(max_length=254)
    content = forms.CharField(max_length=1000,widget=forms.Textarea) #widget=forms.Textarea
    # name = forms.CharField( max_length=254, required=False,widget=forms.TextInput(attrs={'size': 10, 'title': 'Your name'}))
    # password = forms.CharField(max_length=255 , widget=forms.PasswordInput())

























class SimpleForm(forms.Form):
    name = forms.CharField(max_length=255,label="نام",initial="maktab",)
    lastname = forms.CharField(max_length=255,label="نام خانوادگی ",help_text="نام خانوادگی منظور همون فامیلی است ",initial="sharif")
    birthday = forms.IntegerField(label="سال تولد ") #required=False,    error_messages={'invalid':"داداش فقط عدد"}
    choice = forms.ChoiceField(label="الکی",choices=((1,'one'),(2,'two')))
    description = forms.CharField(widget=forms.Textarea)
    # tags = forms.ModelChoiceField(label=" model choice",queryset=Tag.objects.all()) #to_field_name = "title" --> chose value of select
    #refrence : https://docs.djangoproject.com/en/4.2/ref/forms/fields/#django.forms.ModelChoiceField

    def save(self):
        print('on save method : ',self.cleaned_data)
        # ....
        #refrence : https://stackoverflow.com/questions/11943912/how-do-you-write-a-save-method-for-forms-in-django

    

class CommentModelForm(forms.ModelForm):
   
    class Meta :
        model = Comment
        # fields = '__all__' 
        fields = ['email','title','content'] 
        # exclude = ['post']   
        labels = {
            
            'title':_('تایتل'),
            'content':'محتوا',
        }
        widgets = {
            'content': forms.Textarea(attrs={'cols': 20, 'rows': 10}),
        }



class CategoryModelForm(forms.ModelForm):
    class Meta : 
        model = Category
        fields = '__all__' 

