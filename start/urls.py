
from django.urls import path, include
from .views import Index, ApiCartListView

urlpatterns = [
    path("",Index.as_view(), name="index"),
    path('api/cards', ApiCartListView.as_view(), name="api"),

]
