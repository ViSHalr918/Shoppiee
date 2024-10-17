from django.db import models

from django.contrib.auth.models import User


from django.db.models.signals import post_save

# Create your models here.

class UserProfile(models.Model):


    bio = models.CharField(max_length=500,null=True)

    profile_pic = models.ImageField(upload_to="profile_pictures",default="/profile_pictures/default.png")

    user_object = models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile")

    create_date = models.DateTimeField(auto_now=True)

    update_date = models.DateTimeField(auto_now_add=True)

    is_active   = models.BooleanField(default=True)

    def __str__(self):
        return self.user_object.username
    


address_choice=[

    ("Home","Home"),

    ("Work","Work")
]
    

class Address(models.Model):

    name = models.CharField(max_length=300)    

    city = models.CharField(max_length=100 ,null=True)

    area = models.CharField(max_length=100 , null=True)

    pincode = models.PositiveIntegerField()

    house_no = models.CharField(max_length=300 , null=True)

    landmark = models.CharField(max_length=500 , null=True)

    phone_number = models.PositiveIntegerField()

    label = models.CharField(max_length=10,choices=address_choice,default="Home")

    user_object = models.ForeignKey(User,on_delete=models.CASCADE,related_name="detail")

    create_date = models.DateTimeField(auto_now=True)

    update_date = models.DateTimeField(auto_now_add=True)

    is_active   = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    


product_choice = [
    ("Mobiles & Accessories","Mobiles & Accessories"),

    ("Vechicles","Vechicles"),

    ("Electronics & Appliances","Electronics & Appliances"),

    ("Furniture","Furniture"),

    ("Fashion","Fashion"),

    ("Books & Hobbies","Books & Hobbies"),

    ("Sports","Sports"),

    ("Pet Food & Accessories","Pet Food & Accessories")




]



class Product(models.Model):

    brand = models.CharField(max_length=100)

    title = models.CharField(max_length=100)

    description = models.CharField(max_length=500)

    owner = models.ForeignKey(User,on_delete=models.CASCADE,related_name="products")

    category = models.CharField(choices=product_choice,max_length=50)

    image = models.ImageField(upload_to="product_pic")

    price = models.PositiveIntegerField()

    create_date = models.DateTimeField(auto_now=True)

    update_date = models.DateTimeField(auto_now_add=True)

    is_active   = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    


class WishList(models.Model):

    owner    = models.OneToOneField(User,on_delete=models.CASCADE,related_name="basket")

    create_date = models.DateTimeField(auto_now=True)

    update_date = models.DateTimeField(auto_now_add=True)

    is_active   = models.BooleanField(default=True)




class WishListItems(models.Model):

    wishlist_object = models.ForeignKey(WishList,on_delete=models.CASCADE,related_name="basket_item")

    product_object = models.ForeignKey(Product,on_delete=models.CASCADE)

    is_order_placed = models.BooleanField(default=False)

    create_date = models.DateTimeField(auto_now=True)

    update_date = models.DateTimeField(auto_now_add=True)

    is_active   = models.BooleanField(default=True)




class OrderSummary(models.Model):

    user_object = models.ForeignKey(User,on_delete=models.CASCADE,related_name="orders")

    product_objects = models.ManyToManyField(Product)

    order_id = models.CharField(max_length=400,null=True)

    is_paid = models.BooleanField(default=False)

    create_date = models.DateTimeField(auto_now=True)

    update_date = models.DateTimeField(auto_now_add=True)

    is_active   = models.BooleanField(default=True)



def create_profile(sender,instance,created,*args,**kwargs):

    if created:

        UserProfile.objects.create(user_object = instance)

post_save.connect(sender=User,receiver=create_profile)

def create_basket(sender,instance,created,*args,**kwargs):
    if created : 
        WishList.objects.create(owner = instance)

post_save.connect(sender=User,receiver=create_basket)

