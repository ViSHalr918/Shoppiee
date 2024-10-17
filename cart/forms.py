from django import forms    

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User

from cart.models import UserProfile,Product,Address


class SignUpForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}),label="Enter Password")
    password2= forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))

    class Meta:   

        model = User

        fields = ["username","password1","password2","email"]

        widgets = {
            "username":forms.TextInput(attrs={"class":"form-control"}),
            "email":forms.TextInput(attrs={"class":"form-control"}),
        }

class LoginForm(forms.Form):

    username = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))


class UserProfileForm(forms.ModelForm):

    class Meta:

        model = UserProfile

        fields = ["bio","profile_pic"]

        widgets = {
            "bio":forms.TextInput(attrs={"class":"form-control my-3"}),
            "profile_pic":forms.FileInput(attrs={"class":"form-control my-2"})
        }


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        exclude = ("owner","create_date","update_date","is_active")

        widgets = {
            "brand":forms.TextInput(attrs={"class":"form-control mb-3"}),
            "title":forms.TextInput(attrs={"class":"form-control mb-3"}),
            "description":forms.Textarea(attrs={"class":"form-control mb-3","rows":5}),
            "image":forms.FileInput(attrs={"class":"form-control mb-3 mt-3"}),
            "price":forms.NumberInput(attrs={"class":"form-control mb-3"}),
            
        }

class AddressForm(forms.ModelForm):

    name= forms.CharField(widget=forms.TextInput(attrs={"class":"form-control mb-2","placeholder":"Enter your name"}))
    city= forms.CharField(widget=forms.TextInput(attrs={"class":"form-control mb-2","placeholder":"Enter your city"}))
    area= forms.CharField(widget=forms.TextInput(attrs={"class":"form-control mb-2","placeholder":"Enter your area"}))
    pincode= forms.CharField(widget=forms.TextInput(attrs={"class":"form-control mb-2","placeholder":"Enter your pincode"}))
    house_no= forms.CharField(widget=forms.TextInput(attrs={"class":"form-control mb-2","placeholder":"Enter your house no or buliding no"}))
    phone_number= forms.CharField(widget=forms.TextInput(attrs={"class":"form-control mb-2","placeholder":"Enter your Mobile Number"}))
    landmark= forms.CharField(widget=forms.TextInput(attrs={"class":"form-control mb-2","placeholder":"Eg : Near Church"}))

    class Meta:
        model = Address

        exclude = ["user_object","create_date","update_date","is_active"]

