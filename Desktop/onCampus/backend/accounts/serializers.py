from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers

from accounts.models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = [
        'plan',
        'is_landlord',
        'plan',
        'image',
        'phone',
        'address',
        'city',
        'email',
        'monday',
        'tuesday',
        'wednesday',
        'thursday',
        'friday',
        'saturday',
        'sunday',
        'want_location',
        'country']


class UserSerializer(UserDetailsSerializer):

    profile = UserProfileSerializer()

    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + ("profile",)
