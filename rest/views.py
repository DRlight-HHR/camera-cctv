from test_app.models import book
from .models import camera
from .serilizations import book_s, camera_s
from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions

from django.shortcuts import get_object_or_404


class movie(APIView):
    permission_classes = [permissions.IsAdminUser]

    def put(self, request, pk):
        query = camera.objects.get(pk=pk)
        seri = camera_s(query, request.data)
        if seri.is_valid():
            seri.save()
            return Response(status=status.HTTP_426_UPGRADE_REQUIRED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class movie_get(APIView):
    def get(self, request, pk):
        query = get_object_or_404(camera, pk=pk)
        seri = camera_s(query, context={'request': request})
        return Response(seri.data, status=status.HTTP_200_OK)


class get(APIView):
    def get(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        # return HttpResponse("Welcome Home<br>You are visiting from: {}".format(ip))
        if ip == '127.0.0.1':  # Set ip here
            query = book.objects.all()
            seri = book_s(query, many=True, context={'request': request})
            return Response(seri.data, status=status.HTTP_200_OK)
        else:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)


class maker(APIView):
    permission_classes = [permissions.IsAdminUser]

    def post(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        # return HttpResponse("Welcome Home<br>You are visiting from: {}".format(ip))
        if ip == '127.0.0.1':  # Set ip here
            seri = book_s(data=request.data)
            if seri.is_valid():
                seri.save()
                return Response(seri.data, status=status.HTTP_201_CREATED)
            else:
                return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
        else:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)


def check(request, string):
    try:
        ser = request.GET[string]
        return ser
    except Exception as error:
        return 0


class search(APIView):
    def get(self, request):
        ser = ''
        stri = ''
        for i in ['name', 'author', 'Publisher']:
            b = check(request, i)
            if b != 0:
                ser = b
                print(ser)
                if i == 'name':
                    query = book.objects.filter(name=ser)
                elif i == 'author':
                    query = book.objects.filter(author=ser)
                else:
                    query = book.objects.filter(Publisher=ser)
        print(query)
        seri = book_s(query, many=True)
        return Response(seri.data, status=status.HTTP_200_OK)


class delete_data(APIView):
    def delete(self, request, id):
        query = book.objects.get(id=id)
        query.delete()
        return Response(status=status.HTTP_200_OK)


from rest_framework.decorators import api_view


@api_view(['GET'])
def deletedata(request):
    a = request.GET['name']
    query = book.objects.filter(name=a)
    query.delete()
    return Response(status=status.HTTP_200_OK)
