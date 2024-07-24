from rest_framework import serializers

from habits.models import Habit
from habits.validators import ChooseHabitValidator, DurationValidator, RelatedHabitsValidator, AbsenceValidator, \
    PeriodicityValidator
from users.serializers import UserSerializer


class HabitSerializers(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Habit
        fields = '__all__'
        validators = [
            ChooseHabitValidator('related_habit', 'award'),
            DurationValidator('duration'),
            RelatedHabitsValidator('related_habit', 'pleasant_habit_sign'),
            AbsenceValidator('award', 'related_habit', 'pleasant_habit_sign'),
            PeriodicityValidator('periodicity'),
        ]
