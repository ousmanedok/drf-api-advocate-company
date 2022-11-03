from dataclasses import field
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Advocate, Company, Link 


class CompanySerializer(serializers.HyperlinkedModelSerializer):
    advocates = serializers.SlugRelatedField(queryset=Advocate.objects.all(), slug_field='name', many=True)
    class Meta:
        model = Company
        fields = ['id', 'name', 'logo', 'href', 'summary', 'advocates']

class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ['youtube', 'twitter', 'github']

class AdvocateSerializer(serializers.ModelSerializer):
    company = CompanySerializer(many=True, read_only=True)  
    links = LinkSerializer(read_only=True)

    class Meta:
        model = Advocate
        fields = ['id', 'name', 'profile_pic', 'short_bio', 'long_bio', 'advocate_years_exp', 'company', 'links']




