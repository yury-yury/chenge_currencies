from datetime import datetime, timedelta

from django_celery_beat.models import PeriodicTask, IntervalSchedule


schedule, created = IntervalSchedule.objects.get_or_create(
    every=2,
    period=IntervalSchedule.HOURS,
)

PeriodicTask.objects.create(
    interval=schedule,
    name='Update database',
    task='change_currencies.main.tasks.update_database',
    expires=datetime.utcnow() + timedelta(seconds=30)
)