from django.contrib.auth.models import User
from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import generics, viewsets

from .serializers import CategorySerializer, UserSerializer, ProductSerializer
from .models import Category, Product


class ViewAPICategory(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, pk=None):
        if pk is not None:
            snippet = self.get_object(pk)
            serializer = CategorySerializer(snippet)
        else:
            categories = Category.objects.all()
            serializer = CategorySerializer(categories, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        snippet = self.get_object(pk)
        serializer = CategorySerializer(snippet, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        snippet = self.get_object(pk)
        snippet.delete()
        return Response({'delete': f"category {pk} removed"})

class ViewAPIProduct(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
