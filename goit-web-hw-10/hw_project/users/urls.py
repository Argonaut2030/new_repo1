# from django.urls import path, include

# from . import views


# app_name = "quotes"

# urlpatterns = [
#     path("", views.main, name="root")
# ]


# urlpatterns = [
#     path("admin/", views.main, name="root"),
#     path("", include("quotes.urls"))
#     # path("users/0", include("users.urls"))
# ]


from django.urls import path, include
from . import views
# from quotes import views

app_name = 'users'

urlpatterns = [
    path('signup/', views.signupuser, name='signup'),
    path('login/', views.loginuser, name='login'),
    # path('', views.main, name='index'),
    path("", include("quotes.urls", namespace='root'))
]






