import os
from datetime import datetime

from celery import Celery
from celery.schedules import crontab

# from library.tasks import send_loan_notification
# from library.models import Loan

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'library_system.settings')

app = Celery('library_system')

# app.conf.beat_schedule = {
#     'run-sample-task-daily': {
#         'task': 'tasks.check_overdue_loans',
#         'schedule': crontab(hour=24),
#         'args': (),
#     },
# }
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


# @app.tasks
# def check_overdue_loans():
#     today = datetime.today().strftime('%Y-%m-%d')
#
#     due_loan_members = Loan.objects.filter(is_returned=False, due_date__lt=today).all()
#     if due_loan_members:
#         for member in due_loan_members:
#             send_loan_notification.delay(member.id)

