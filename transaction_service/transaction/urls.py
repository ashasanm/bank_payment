from django.urls import path

from . import views

app_name = "transaction"
urlpatterns = [
    # ex: /account/
    path("transaction/", views.TransactionView.as_view(), name="transaction"),
]
