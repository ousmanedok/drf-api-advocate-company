from rest_framework import serializers
from .models import Advocate, Company, Link 

class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ['youtube', 'twitter', 'github']

class AdvocateSerializer(serializers.ModelSerializer):
    links = LinkSerializer(read_only=True)

    class Meta:
        model = Advocate
        fields = ['id', 'name', 'profile_pic', 'short_bio', 'long_bio', 'advocate_years_exp', 'links']

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        exclude = ('advocates', )
class CompanyDetailSerializer(serializers.ModelSerializer):
    advocates = AdvocateSerializer(many=True)
    class Meta:
        model = Company
        fields = ['id', 'name', 'logo', 'summary', 'advocates']
        

class AdvocateDetailSerializer(serializers.ModelSerializer):
    company = serializers.SerializerMethodField()
    links = LinkSerializer(read_only=True)

    def get_company(self, obj: Advocate):
        print(obj.id)
        return CompanySerializer(instance=Company.objects.filter(advocates__in=[obj.pk]), many=True).data

    class Meta:
        model = Advocate
        fields = ['id', 'name', 'profile_pic', 'short_bio', 'long_bio', 'advocate_years_exp', 'company' ,'links']


