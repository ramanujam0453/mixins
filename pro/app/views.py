from django.shortcuts import render
from rest_framework import mixins, generics
from . models import Emp
from . serializers import EmpSerializer


class EmpList(mixins.CreateModelMixin, mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Emp.objects.all()
    serializer_class = EmpSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class EmpDetails(mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Emp.objects.all()
    serializer_class = EmpSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
