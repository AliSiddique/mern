from rest_framework import serializers
from .models import Listing, ListingViews, ListingTour, ListingMail


class ListingSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%d-%m-%Y")

    class Meta:
        model = Listing
        fields = '__all__'





class ListingMailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListingMail
        fields = '__all__'       
        read_only_fields = ('listing',)




class ListingTourSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListingTour
        fields = '__all__'               
        read_only_fields = ('listing',)