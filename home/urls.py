from django.urls import path , include
from . import views


urlpatterns = [
    
    
    #landingPage
    path('',views.landing,name="landing"),

    # Home
    path('home/', views.home,name="home"),

    # Auth
    path('register', views.register,name="register"),
    path('login', views.login,name="login"),
    path('logout', views.logout,name="logout"),

    # Group
    path('group',views.group,name="group"),
    path('create-group',views.creategroup,name="create-group"),
    path('group/<str:id>',views.groupdetails,name="groupdetails"),
    path('group/<str:id>/add-member',views.addmember,name="addmember"),
    #delete-group
    path("group/<str:id>/deletegroup", views.deletegroup, name="delete Group"),

    # path("group/<str:id>/deleteexpense",views.deleteexpense,name="deleteexpense"),

    # calculate
    path('sendmsg',views.sendmsg,name="sendmsg"),

    # history
    path('history',views.history,name="history"),

    #wallet
    path('wallet',views.wallet,name="wallet"),
    
    #support
    path('support',views.support,name="support"),

    #profile
    path('profile',views.profile,name="profile")

    

]