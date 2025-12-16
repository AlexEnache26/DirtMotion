from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from viewer import views
from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    # HOME
    path('', views.home_page, name='home'),
    path('hello/<str:s>/', views.hello, name='hello'),

    # ITEMS
    path('item/create/', views.ItemCreateView.as_view(), name='item_create'),
    path('items/', views.items_list, name='items_list'),
    path('add/', views.add_item, name='add_item'),
    path('item_detail/<int:item_id>/', views.view_item, name='item_detail'),

    # AUTH
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('register/', views.register, name='register'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('my-account/', views.my_account, name='my_account'),

    # CONTACT ✅
    path('contact/', views.contact, name='contact'),

    # 🔐 RESET PASSWORD
    path(
        'password-reset/',
        auth_views.PasswordResetView.as_view(
            template_name='registration/password_reset.html'
        ),
        name='password_reset'
    ),
    path(
        'password-reset/done/',
        auth_views.PasswordResetDoneView.as_view(
            template_name='registration/password_reset_done.html'
        ),
        name='password_reset_done'
    ),
    path(
        'reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='registration/password_reset_confirm.html'
        ),
        name='password_reset_confirm'
    ),
    path(
        'reset/done/',
        auth_views.PasswordResetCompleteView.as_view(
            template_name='registration/password_reset_complete.html'
        ),
        name='password_reset_complete'
    ),
]
