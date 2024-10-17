from django.urls import path,include

from cart import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path("register",views.RegisterView.as_view(),name="register"),

    path("",views.LogInView.as_view(),name="login"),

    path("logout",views.LogoutView.as_view(),name="logout"),

    path("index",views.IndexView.as_view(),name="index"),

    path("profile_edit/<int:pk>",views.UserProfileUpdateView.as_view(),name="profile"),

    path("address",views.AddressView.as_view(),name="address"),

    path("address/create",views.AddressCreateView.as_view(),name="address_create"),

    path("address/<int:pk>/delete/",views.AddressDeleteView.as_view(),name="address_delete"),

    path("product/add",views.ProductCreateView.as_view(),name="product-add"),

    path("myproducts",views.MyProductsView.as_view(),name="myproducts"),

    path("product/<int:pk>/remove",views.ProductDeleteView.as_view(),name="product_remove"),

    path("product/<int:pk>/detail",views.ProductDetailView.as_view(),name="product_detail"),

    path("add/<int:pk>/wishlist",views.AddToWishListItemsView.as_view(),name="add_to_wishlist"),

    path("cartlist/",views.CartView.as_view(),name="cart_items"),

    path("cart/<int:pk>/remove",views.WishListItemDeleteView.as_view(),name="cartitem_delete"),

    path("select/address",views.SelectAddressView.as_view(),name="select_address"),

    path('select/address/on_payment',views.SelectAddressOnPayment.as_view(),name="address_on_payment"),

    path('checkout',views.CheckOutView.as_view(),name="checkout")
    

    
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)