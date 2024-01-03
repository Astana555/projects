'''from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('feedback.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
'''

from django.urls import path
from .views import feedback

urlpatterns = [
    path('', feedback, name='feedback'),
]