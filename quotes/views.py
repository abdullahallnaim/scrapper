from rest_framework import generics, filters
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from .models import Quote
from .serializers import QuoteSerializer
import random

class QuoteListAPIView(generics.ListAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['text', 'author']

@api_view(['GET'])
def random_quote(request):
    quote_count = Quote.objects.count()
    random_index = random.randint(0, quote_count - 1)
    random_quote = Quote.objects.all()[random_index]
    serializer = QuoteSerializer(random_quote)
    return Response(serializer.data)
