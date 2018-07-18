from celery import Celery

app = Celery('celery_config', broker='redis://localhost:6379/0', include=['celery_blog', 'pack.celery_fetch'])
