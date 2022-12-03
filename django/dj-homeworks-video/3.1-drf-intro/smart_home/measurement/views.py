# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView


from rest_framework.generics import RetrieveAPIView, ListAPIView, RetrieveUpdateAPIView
from .models import Sensor, Measurement
from .serializers import SensorSerializer, MeasurementSerializer, SensorDetailSerializer
from rest_framework.response import Response


class SensorsView(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def post(self, request):
        data = request.data
        name = data['name']
        description = data['description']
        Sensor(name=name, description=description).save()
        return Response(data)


class SensorUpdateView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

    def patch(self, request, pk):
        return self.partial_update(request)


class MeasurementView(ListAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    def post(self, request):
        data = request.data
        sensor = Sensor.objects.get(id=data['sensor'])
        temperature = data['temperature']
        if 'image' in data.keys():
            image = data['image']
            Measurement(sensor=sensor, temperature=temperature, image=image).save()
        else:
            Measurement(sensor=sensor, temperature=temperature).save()
        return Response(data)
