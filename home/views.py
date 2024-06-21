from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, RetrieveAPIView
from rest_framework.mixins import UpdateModelMixin, CreateModelMixin
from rest_framework.permissions import IsAdminUser
from .serializer import CardSerializer, CarsSerializer, FirmwareSerializer
from .models import Cards, Cars, Firmware
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
# Create your views here.

class CardsCreateList(CreateModelMixin, ListAPIView):
    serializer_class = CardSerializer
    queryset = Cards.objects.all()
    permission_classes = (IsAdminUser, )

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data,status=status.HTTP_201_CREATED, headers=headers)


class CheckFirmware(APIView):
    def post(self, request, *args, **kwargs):
        mac_address = request.data.get('mac_address')
        firmware_version = request.data.get('firmware_version')

        try:
            car = Cars.objects.get(mac_address=mac_address)
        except Cars.DoesNotExist:
            try:
                firmware = Firmware.objects.get(version=firmware_version)
            except Firmware.DoesNotExist:
                return Response({'error': 'firmware version does not exist'}, status=status.HTTP_404_NOT_FOUND)
            car_lisence = request.data.get('license_plate')
            new_car = Cars.objects.craete(
                license_plate_max = car_lisence,
                mac_address = mac_address,
                firmware_version = firmware
            )
            new_car.save()
            return Response({'message': 'Car added successfully'}, status=status.HTTP_201_CREATED)
        
        if car.firmware_version.verison != firmware_version:
            firmware_data = car.firmware_version.firmware_data
            return Response({'firmware_data': firmware_data}, status=status.HTTP_200_OK)
        
        return Response({'message': 'No update needed'}, status=status.HTTP_200_OK)
    
    def patch(self, request,*args, **kwargs):
        try:
            car = Cars.objects.get(mac_address=request.data.get('mac_address'))
        except Cars.DoesNotExist:
            return Response({'error': 'Car not found'}, status=status.HTTP_404_NOT_FOUND)
        
        ser_data = CardSerializer(car, data=request.data, partial=True)
        if ser_data.is_valid():
            firmware_version = request.data.get('firmware_version')
            try:
                new_firmware = Firmware.objects.get(version=firmware_version)
            except Firmware.DoesNotExist:
                return Response({'error': 'firmware version doesn`t exist'})
            
            if car.firmware_version != new_firmware:
                car.firmware_version = new_firmware
                car.save()
                return Response({'message': 'firmware updated successfully'}, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'firmware is already up to date'}, status=status.HTTP_200_OK)
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)


class FirmwareViewSet(viewsets.ModelViewSet):
    queryset = Firmware.objects.all()
    serializer_class = FirmwareSerializer