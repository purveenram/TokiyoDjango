from django.urls import path
from . import views  
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('searchInput/',views.searchInput,name='searchInput'),

    path('home/',views.home,name='home'),
    path('login/', views.login, name='login'),
    path('credentialCheck/', views.credentialCheck, name="credentialCheck"),
    path('logout/', views.logout, name='logout'),

    path('registrationCustomer/', views.registrationCustomer, name='registrationCustomer'),
    path('addCustomer/', views.addCustomer, name='addCustomer'),
    path('profile/', views.customerProfile, name='profile'),
    path('updateProfile/', views.updateProfile, name='updateProfile'),

    path('registrationAddress/', views.registrationAddress, name='registrationAddress'),
    path('addAddress/', views.addAddress, name='addAddress'),
    path('address/', views.customerAddress, name='address'),
    path('updateAddress/', views.updateAddress, name='updateAddress'),

    path('category/<int:category>/', views.viewCategory, name='category'),
    path('product/<int:prod>/', views.viewProduct, name='product'),
    path('cart/', views.viewCart, name='cart'),

    path('addInCart/<int:prod>/', views.addInCart, name='addInCart'),
    path('removeInCart/<int:productId>/', views.removeInCart, name='removeInCart'),

    path('makePayment/', views.makePayment, name='makePayment'),
    path('viewOrders/', views.viewOrders, name='viewOrders'),
    path('removeInOrder/<int:orderId>/', views.removeInOrder, name='removeInOrder'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
