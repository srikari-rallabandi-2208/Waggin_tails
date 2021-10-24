from django.urls import path
from . import views


urlpatterns = [
	#path('register/', views.registerPage, name="register"),
	path('loginPM', views.loginPM, name="loginPM"),
    path('loginV', views.loginV, name="loginV"),  
    path('SignupPM', views.SignupPM, name="SignupPM"),
    path('SignupV', views.SignupV, name="SignupV"),  
	# path('logout/', views.logoutUser, name="logout"),
    path('memberarea', views.memberArea, name="memberarea"),
    path('vmemberarea', views.vmemberArea, name="vmemberarea"),
    path('', views.home, name="home"),
    # path('user/', views.userPage, name="user-page"),

    path('ownerSettings', views.ownerSettings, name="ownerSettings"),
    path('petSettings', views.petSettings, name="petSettings"),

    path('volunteerSettings1', views.volunteerSettings1, name="volunteerSettings1"),
    path('volunteerSettings2', views.volunteerSettings2, name="volunteerSettings2"),


    #path('products/', views.products, name='products'),
    # path('customer/<str:pk_test>/', views.customer, name="customer"),

    # path('create_order/<str:pk>/', views.createOrder, name="create_order"),
    # path('update_order/<str:pk>/', views.updateOrder, name="update_order"),
    # path('delete_order/<str:pk>/', views.deleteOrder, name="delete_order"),


]