from django.urls import path
from .views import index,blog,about,services,contact,cart,checkout,shop,thankyou,login,register,logout

urlpatterns = [
    path('', index, name='index'),
    path('blog/', blog, name='blog'),
    path('about/', about, name='about'),
    path('services/', services, name='services'),
    path('contact/', contact, name='contact'),
    path('cart/', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
    path('shop/', shop, name='shop'),
    path('thankyou/', thankyou, name='thankyou'),
    path('login/', login, name='login'),
    path('register/',register,name='register'),
    path('logout/',logout,name='logout'),
]
