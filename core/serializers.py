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
    astronomy_show = AstronomyShowSerializer()
    planetarium_dome = PlanetariumDomeSerializer()

    class Meta:
        model = ShowSession
        fields = "__all__"

    def create(self, validated_data):
        astronomy_show_data = validated_data.pop("astronomy_show")
        planetarium_dome_data = validated_data.pop("planetarium_dome")

        astronomy_show = AstronomyShow.objects.create(**astronomy_show_data)
        planetarium_dome = PlanetariumDome.objects.create(**planetarium_dome_data)

        show_session = ShowSession.objects.create(
            astronomy_show=astronomy_show,
            planetarium_dome=planetarium_dome,
            **validated_data
        )

        return show_session


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
