from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm
from .models import Shop
from .serializer import ShopSerializer, ShopShowSerializer,TransactionsSerializer
from rest_framework import viewsets
from rest_framework.views import APIView, Response, Request, status


# from .serializers import ShopSerializer, TransactionsSerializer
import ipdb


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            serializer = ShopSerializer(data={'file': request.FILES['file']})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return HttpResponseRedirect('/list/')
    else:
        form = UploadFileForm()
    return render(request, 'form-upload.html', {'form': form})

class ShopView(APIView):

    def get(self, request):
        shop = Shop.objects.all()
        serializer = ShopShowSerializer(shop, many=True)
        return Response(serializer.data)
