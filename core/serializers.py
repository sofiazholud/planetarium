from rest_framework import serializers
from .models import (
    AstronomyShow,
    ShowTheme,
    PlanetariumDome,
    ShowSession,
    Reservation,
    Ticket,
)


class AstronomyShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = AstronomyShow
        fields = "__all__"


class ShowThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShowTheme
        fields = "__all__"


class PlanetariumDomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanetariumDome
        fields = "__all__"


class ShowSessionSerializer(serializers.ModelSerializer):
    astronomy_show = serializers.PrimaryKeyRelatedField(
        queryset=AstronomyShow.objects.all()
    )
    planetarium_dome = serializers.PrimaryKeyRelatedField(
        queryset=PlanetariumDome.objects.all()
    )

    class Meta:
        model = ShowSession
        fields = "__all__"

    def create(self, validated_data):
        return ShowSession.objects.create(**validated_data)


class ReservationSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Reservation
        fields = "__all__"
        read_only_fields = ("user",)


class TicketSerializer(serializers.ModelSerializer):
    show_session = ShowSessionSerializer()
    reservation = ReservationSerializer()

    class Meta:
        model = Ticket
        fields = "__all__"
