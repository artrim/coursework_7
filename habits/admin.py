from django.contrib import admin

from habits.models import Habit


@admin.register(Habit)
class LessonAdmin(admin.ModelAdmin):
    list_display = ("owner", "place", "time", "action", "pleasant_habit_sign", "related_habit", "periodicity", "award",
                    "duration", "is_published",)
