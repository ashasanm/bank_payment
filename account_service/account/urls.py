from django.urls import path

from . import views

app_name = "account"
urlpatterns = [
    # ex: /account/
    path("account/", views.AccountView.as_view(), name="account"),
    path("account/balance", views.BalanceView.as_view(), name="balance"),
]
