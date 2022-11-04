from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from .advocates import advocates
from .models import Advocate
from .models import Company
from .serializers import AdvocateSerializer, CompanySerializer, AdvocateDetailSerializer, CompanyDetailSerializer
from .pagination import StandardResultsSetPagination

# Create your views here.

@api_view(['GET'])
def getRoutes(request):
    api_urls = {
        'api/advocates/',
        'api/advocates/id',
        'api/companies/',
        'api/companies/id',
        }

    return Response(api_urls)

@api_view(['GET'])
def getAdvocates(request):
    advocates = Advocate.objects.all()
    if len(advocates) > 0 :
        paginator = StandardResultsSetPagination()
        result_page = paginator.paginate_queryset(advocates, request)
        serializer = AdvocateSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)
    else:
        return Response({},status=status.HTTP_200_OK)    


@api_view(['GET'])
def getAdvocate(request, pk):
    advocate = Advocate.objects.get(id=pk)
    serializer = AdvocateDetailSerializer(advocate)
    return Response(serializer.data)  


@api_view(['GET'])
def getCompanies(request):
    companies = Company.objects.all()
    if len(companies) > 0 :
        paginator = StandardResultsSetPagination()
        result_page = paginator.paginate_queryset(companies, request)
        serializer = CompanySerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)
    else:
        return Response({},status=status.HTTP_200_OK)

@api_view(['GET'])
def getCompany(request, pk):
    company = Company.objects.get(id=pk)
    serializer = CompanyDetailSerializer(company)
    return Response(serializer.data)  