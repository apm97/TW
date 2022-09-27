from unicodedata import name
from django.urls import path
from . import views
from .views import MyTokenObtainPairView
from .views import StripeCheckoutView

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [

    path('users/profile/', views.getUserProfile, name="users-profile"),
    path('users/profile/update/', views.updateUserProfile, name="users-profile-update"),
    path('users/', views.getUsers, name="users"),


    path('users/login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('users/register/', views.registerUser, name='register'),
    
    path('users/delete/<str:pk>/', views.deleteUser, name="user-delete"),
    path('users/update/<str:pk>/', views.updateUser, name="user-update"),
    path('users/<str:pk>/', views.getUserById, name="user"),

    path("notes/", views.note, name="note"),
    path("notes/<int:pk>/", views.note_detail, name="detail"),
    path("notes/create/", views.createNote, name="create-content"),
    path('notes/mynotes/', views.getMyNotes, name="mynotes"),
    path('notes/delete/<str:pk>/', views.deleteNotes, name="note-delete"),


    path("subscription/", views.subscriptions, name="subscriptions"),
    path('subscription/mysubscription/', views.getMyMembership, name="mysub"),
    path("subscription/update/", views.updateMembership, name="update-Membership"),
    path("subscription/delete/<str:pk>/", views.deleteMembership, name="delete-Membership"),

    path('stripe/create-checkout-session', StripeCheckoutView.as_view()),

]