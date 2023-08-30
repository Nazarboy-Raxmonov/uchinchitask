from django.urls import path
from .views import sotuvchiallviews, sotuvchidetailsviews,mahsulotallviews, mahsulotdetailsviews

urlpatterns = [
    path('mahsulot/details/<int:mahsulot_id>', mahsulotdetailsviews),
    path('sotuvchi/details/<int:sotuvchi_id>', sotuvchidetailsviews),
    path('mahsulot/all/', mahsulotallviews),
    path('sotuvchi/all/', sotuvchiallviews)
]