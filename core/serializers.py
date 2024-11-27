from rest_framework import serializers
from .models import AstronomyShow, ShowTheme, PlanetariumDome, ShowSession, Reservation, Ticket

class AstronomyShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = AstronomyShow
        fields = '__all__'

class ShowThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShowTheme
        fields = '__all__'

class PlanetariumDomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanetariumDome
        fields = '__all__'

class ShowSessionSerializer(serializers.ModelSerializer):
    astronomy_show = AstronomyShowSerializer()
    planetarium_dome = PlanetariumDomeSerializer()

    class Meta:
        model = ShowSession
        fields = '__all__'

class ReservationSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()  # User name or email

    class Meta:
        model = Reservation
        fields = '__all__'

class TicketSerializer(serializers.ModelSerializer):
    show_session = ShowSessionSerializer()
    reservation = ReservationSerializer()

    class Meta:
        model = Ticket
        fields = '__all__'
