from django.shortcuts import render,redirect

from django.urls import reverse_lazy

from django.db.models import Sum

from django.views.generic import View,UpdateView,CreateView,ListView

from cart.forms import SignUpForm,LoginForm,UserProfileForm,ProductForm,AddressForm

from cart.models import UserProfile,Product,WishListItems,Address,OrderSummary,Cash_On_Delivery

from django.contrib.auth import authenticate,login,logout

from django.views.decorators.csrf import csrf_exempt

from django.utils.decorators import method_decorator




KEY_ID = 'rzp_test_GRFSxyS5rYy9tz'

KEY_SECRET = '7EAGwte0zokwc900F21NYk9I'



# Create your views here.


class RegisterView(View):

    def get(self,request,*args,**kwargs):

        form_instance = SignUpForm()

        return render(request,"cart/register.html",{"form":form_instance})
    
    def post(self,request,*args,**kwargs):

        form_instance = SignUpForm(request.POST)

        if form_instance.is_valid():
            form_instance.save()
            return redirect("login")
        else:
            return render(request,"cart/register.html",{"form":form_instance})
        
class LogInView(View):

    def get(self,request,*args,**kwargs):

        form_instance = LoginForm()

        return render(request,"cart/login.html",{"form":form_instance})
    
    def post(self,request,*args,**kwargs):

        form_instance = LoginForm(request.POST)

        if form_instance.is_valid():
            data = form_instance.cleaned_data

            user_obj = authenticate(request,**data)

            if user_obj:
                login(request,user_obj)
                print("success")
                return redirect("index")
            else:

                return render(request,"cart/login.html",{"form":form_instance})
            
class LogoutView(View):
    def get(self,request):
        logout(request)
        return redirect("login")
    

           
class IndexView(View):
    
    def get(Self,request,*args,**kwargs):

        qs = Product.objects.all().exclude(owner=request.user)

        return render(request,"cart/index.html",{"works":qs})
    

class MobilesAccessories_view(View):

    def get(self,request):

        qs = Product.objects.filter(category = "Mobiles & Accessories")

        return render(request,"cart/mobile.html",{"mobile":qs})
    
class Electronics_view(View):

    def get(self,request):

        qs = Product.objects.filter(category = "Electronics & Appliances")

        return render(request,"cart/Electronics.html",{"Electronics":qs})
    
class VechiclesView(View):

    def get(self,request):

        qs = Product.objects.filter(category = "Vechicles")

        return render(request,"cart/Vechicles.html",{"Vechicles":qs})
    
class SportsView(View):

    def get(self,request):

        qs = Product.objects.filter(category = "Sports")

        return render(request,"cart/Sports.html",{"Sports":qs})
    
class FurnitureView(View):

    def get(self,request):

        qs = Product.objects.filter(category = "Furniture")

        return render(request,"cart/Furniture.html",{"Furniture":qs})


class UserProfileUpdateView(UpdateView):

    model = UserProfile

    form_class = UserProfileForm

    template_name = 'cart/profile_edit.html'

    success_url = reverse_lazy("index")

class AddressView(View):

    def get(self,request,*args,**kwargs):


        qs = Address.objects.filter(user_object=request.user)

        return render(request,"cart/address.html",{"address":qs})




class AddressCreateView(View):
    def get(self,request,*args,**kwargs):

        form_instance = AddressForm()
        return render(request,"cart/address_create.html",{"form":form_instance})
    
    def post(self,request,*args,**kwargs):

        form_instance = AddressForm(request.POST)

        if form_instance.is_valid():
            form_instance.instance.user_object=request.user
            form_instance.save()
            print("address added successfully")
            return redirect("address")
        else:
            return render(request,"cart/address_create.html",{"form":form_instance})
        
class AddressDeleteView(View):

    def get(self,request,**kwargs):
        id = kwargs.get("pk")
        Address.objects.get(id=id).delete()
        return redirect("address")
    

class ProductCreateView(CreateView):

    model = Product

    form_class = ProductForm

    template_name = "cart/product_add.html"

    success_url = reverse_lazy("index")

    def post(self, request, *args, **kwargs):
        
        form_instance = ProductForm(request.POST,files=request.FILES)

        if form_instance.is_valid():
            form_instance.instance.owner = request.user
            form_instance.save()
            return redirect("index")
        else:
            return render(request,self.template_name,{"form":form_instance})
     
        
class MyProductsView(View):


    def get(self,request,*args,**kwargs):

        qs = Product.objects.filter(owner=request.user)

        return render(request,"cart/myproducts.html",{"works":qs})
    
class ProductDeleteView(View):

    def get(self,request,*args,**kwargs):

        id = kwargs.get("pk")

        Product.objects.get(id=id).delete()

        return redirect("myproducts")


class ProductDetailView(View):


    def get(self,request,*args,**kwargs):

        id = kwargs.get("pk")

        qs = Product.objects.get(id=id)

        return render(request,"cart/product_detail.html",{"work":qs})
    
   
class AddToWishListItemsView(View):
    def get(self,request,*args,**kwargs):

        id = kwargs.get("pk")

        product_obj = Product.objects.get(id=id)

        WishListItems.objects.create(
                                        wishlist_object = request.user.basket,
                                        product_object = product_obj

        )

        print("successfully added to wishlist")
        return redirect("index")
    
class CartView(View):
    def get(self,request,*args,**kwargs):

        qs = request.user.basket.basket_item.filter(is_order_placed=False).order_by('-id')

        Total = request.user.basket.basket_item.filter(is_order_placed=False).values("product_object__price").aggregate(total=Sum("product_object__price")).get('total')

        return render(request,"cart/wishlist_summary.html",{"cart_items":qs,"total":Total})
    
class WishListItemDeleteView(View):
    def get(self,request,*args,**kwargs):
        id = kwargs.get("pk")
        WishListItems.objects.get(id=id).delete()
        return redirect("cart_items")



class SelectAddressView(View):

    def get(self,request,*args,**kwargs):

        qs = Address.objects.filter(user_object=request.user)

        return render(request,"cart/selectaddress.html",{"address":qs})
    


class SelectAddressOnPayment(View):

    def get(self,request,*args,**kwargs):

        form_instance = AddressForm()

        return render(request,"cart/address_on_payment.html",{"form":form_instance})
    
    def post(self,request,*args,**kwargs):

        form_instance = AddressForm(request.POST)

        if form_instance.is_valid():
            form_instance.instance.user_object=request.user
            form_instance.save()
            return redirect("checkout")
        else:
            return render(request,"cart/address_on_payment.html",{"form":form_instance})


    

    
import razorpay

 
class CheckOutView(View):
    def get(self,request,*args,**kwargs):

        client = razorpay.Client(auth=(KEY_ID, KEY_SECRET))

        Total = request.user.basket.basket_item.filter(is_order_placed=False).values("product_object__price").aggregate(total=Sum("product_object__price")).get('total') * 100

        

        data = { "amount": Total, "currency": "INR", "receipt": "order_rcptid_11" }
        
        payment = client.order.create(data=data)

        # print(payment)
        
        cart_items = request.user.basket.basket_item.filter(is_order_placed = False)

        Order_summary_obj = OrderSummary.objects.create(

                user_object = request.user,
                order_id = payment.get("id"),
                total = request.user.basket.wishlist_total()
        )

        # (cart_items.values("product_object"))

        for ci in cart_items:
            Order_summary_obj.product_objects.add(ci.product_object)

        for ci in cart_items:
            ci.is_order_placed=True

            ci.save()
   
        context = {
            "key": KEY_ID,
            "amount":data.get("amount"),
            "currency" : data.get("currency"),
            "order_id" : payment.get("id")

        }

        return render(request,"cart/checkout.html",context)
        
@method_decorator(csrf_exempt,name='dispatch')
class PaymentVerificationView(View):    

    def post(self,request,*args,**kwargs):

        # {'razorpay_payment_id': ['pay_PBuAjfaSaipLFR'],
        #   'razorpay_order_id': ['order_PBuAU2e0nsMGBT'],
        #   'razorpay_signature': ['ab80a3d081dfffd9697098fa993131f813bc85a4ad7e9d6252ff6bf041f85b70']}



        print(request.POST)
        client = razorpay.Client(auth=(KEY_ID, KEY_SECRET))
        order_summary_object = OrderSummary.objects.get(order_id = request.POST.get("razorpay_order_id"))
        login(request,order_summary_object.user_object)

        try : 
            client.utility.verify_payment_signature(request.POST)
            print("success")
            order_id = request.POST.get("razorpay_order_id")

            OrderSummary.objects.filter(order_id = order_id).update(is_paid=True)

        except : 

            print("unsuccess")        
        

        # return render(request,"cart/success.html")
    
        return redirect("index")
    
class Cash_On_DeliveryView(View):

    def get(self,request):

        cart_items = request.user.basket.basket_item.filter(is_order_placed = False)

        delivery_obj = Cash_On_Delivery.objects.create(
                    owner = request.user,
        )

        for ci in cart_items:
            delivery_obj.product_objects.add(ci.product_object)

        for ci in cart_items:
            ci.is_order_placed=True

            ci.save()

        return redirect("index")
    

class MyPurchaseView(ListView):
    model = OrderSummary
    context_object_name = "orders"

    def get(self,request):

        qs = OrderSummary.objects.filter(
            user_object = request.user,
            is_paid = True

        ).order_by('-id')

        return render(request,"cart/order_summary.html",{"orders":qs})
    




