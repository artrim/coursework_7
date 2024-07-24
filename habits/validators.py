from datetime import timedelta

from rest_framework.exceptions import ValidationError


class ChooseHabitValidator:

    def __init__(self, related_habit, award):
        self.related_habit = related_habit
        self.award = award

    def __call__(self, habit):
        if habit.get(self.related_habit) and habit.get(self.award):
            raise ValidationError('Не должно быть заполнено одновременно и поле вознаграждения, '
                                  'и поле связанной привычки. Можно заполнить только одно из двух')


class DurationValidator:

    def __init__(self, duration):
        self.duration = duration

    def __call__(self, habit):
        max_duration = timedelta(seconds=120)
        if (habit.get(self.duration)
                and habit.get(self.duration) > max_duration):
            raise ValidationError(f'Время выполнения должно быть не больше {max_duration}.')


class RelatedHabitsValidator:

    def __init__(self, related_habit, pleasant_habit_sign):
        self.related_habit = related_habit
        self.pleasant_habit_sign = pleasant_habit_sign

    def __call__(self, habit):
        if (habit.get(self.related_habit)
                and not habit.get(self.pleasant_habit_sign)):
            raise ValidationError('В связанные привычки могут попадать только привычки с признаком приятной привычки.')


class PeriodicityValidator:

    def __init__(self, periodicity):
        self.periodicity = periodicity

    def __call__(self, habit):
        if habit.get(self.periodicity) and habit.get(self.periodicity) > 7:
            raise ValidationError('Нельзя выполнять привычку реже, чем 1 раз в 7 дней.')


class AbsenceValidator:

    def __init__(self, award, related_habit, pleasant_habit_sign):
        self.award = award
        self.related_habit = related_habit
        self.pleasant_habit_sign = pleasant_habit_sign

    def __call__(self, habit):
        if habit.get(self.pleasant_habit_sign) and (
            habit.get(self.award) or habit.get(self.related_habit)
        ):
            raise ValidationError('У приятной привычки не может быть вознаграждения или связанной привычки.')
