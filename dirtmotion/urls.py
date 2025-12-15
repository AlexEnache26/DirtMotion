from django.contrib import admin
from django.urls import path
from viewer.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),

    # HOME
    path('', home_page, name='home'),
    path('hello/<str:s>/', hello, name='hello'),

    # ITEMS
    path('item/create', ItemCreateView.as_view(), name='Item_create'),
    path('items/new/', ItemCreateView.as_view(), name='item_create'),
    path('items/', items_list, name='items_list'),
    path('add', add_item, name='add_item'),
    path('item_detail/<int:item_id>/', view_item, name='item_detail'),

    # AUTH
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', register, name='register'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('my-account/', my_account, name='my_account'),

    # 🔐 FORGOT PASSWORD (RESET PASSWORD)
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

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
