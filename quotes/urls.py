from django.urls import path
from .views import QuoteListAPIView, random_quote

urlpatterns = [
    path('api/quotes/', QuoteListAPIView.as_view(), name='quote-list'),
    path('api/quotes/random/', random_quote, name='random-quote'),
]
