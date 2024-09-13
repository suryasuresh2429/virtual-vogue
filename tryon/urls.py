from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='index'),
    path('about/', views.about, name='about'),
    path('user_profile/', views.user_profile, name='user_profile'),
    path('tryon/', views.tryon, name='tryon'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    #ecart
    path('buy-now/', views.buy_now, name='buy_now'),
    path('buy-now1/', views.buy_now1, name='buy_now1'),
    path('buy-now2/', views.buy_now2, name='buy_now2'),
    path('buy-now3/', views.buy_now3, name='buy_now3'),
    path('buy-now4/', views.buy_now4, name='buy_now4'),
    path('buy-now5/', views.buy_now5, name='buy_now5'),
    path('buy-now6/', views.buy_now6, name='buy_now6'),
    path('buy-now7/', views.buy_now7, name='buy_now7'),
    path('buy-now8/', views.buy_now7, name='buy_now8'),
    path('add-to-cart/', views.add_to_cart, name='add_to_cart'),
    path('checkout/', views.checkout, name='checkout_page'),
    path('wishlist/', views.wishlist, name='wishlist'),
    # path('wishlist/remove/<int:item_id>/', views.remove_from_wishlist, name='remove_from_wishlist'),
    # path('process-payment/', views.process_payment, name='process_payment'),
]