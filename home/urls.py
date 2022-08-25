from django.urls import path , include
from . import views


urlpatterns = [
    
    
    #landingPage
    path(' ',views.landingpage,name="landingpage"),

    # Home
    path('', views.home,name="home"),

    # Auth
    path('register', views.register,name="register"),
    path('login', views.login,name="login"),
    path('logout', views.logout,name="logout"),

    # Group
    path('group',views.group,name="group"),
    path('create-group',views.creategroup,name="create-group"),
    path('group/<str:id>',views.groupdetails,name="groupdetails"),
    path('group/<str:id>/add-member',views.addmember,name="addmember"),

    # calculate
    path('sendmsg',views.sendmsg,name="sendmsg"),

    # history
    path('history',views.history,name="history"),

    #history
    path('wallet',views.wallet,name="wallet"),
]