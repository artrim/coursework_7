from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from habits.models import Habit
from habits.paginators import HabitPagination
from habits.permissions import IsOwner
from habits.serializers import HabitSerializers


class HabitCreateAPIView(generics.CreateAPIView):
    serializer_class = HabitSerializers
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        habit = serializer.save()
        habit.owner = self.request.user
        habit.save()


class HabitPublishedListAPIView(generics.ListAPIView):
    serializer_class = HabitSerializers
    pagination_class = HabitPagination

    def get_queryset(self):
        return Habit.objects.filter(is_published=True)


class HabitListAPIView(generics.ListAPIView):
    serializer_class = HabitSerializers
    pagination_class = HabitPagination
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Habit.objects.filter(owner=user)


class HabitRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = HabitSerializers
    queryset = Habit.objects.all()
    permission_classes = [IsOwner]


class HabitUpdateAPIView(generics.UpdateAPIView):
    serializer_class = HabitSerializers
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class HabitDestroyAPIView(generics.DestroyAPIView):
    serializer_class = HabitSerializers
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]
