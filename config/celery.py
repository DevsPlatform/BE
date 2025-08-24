import os
from celery import Celery
from django.conf import settings

# Django settings module을 celery에서 사용할 수 있도록 설정
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.development')

app = Celery('config')

# Django settings에서 CELERY로 시작하는 설정들을 로드
app.config_from_object('django.conf:settings', namespace='CELERY')

# Django apps에서 tasks.py 파일들을 자동으로 찾아서 등록
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')