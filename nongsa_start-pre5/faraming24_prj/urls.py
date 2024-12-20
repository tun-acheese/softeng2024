from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('', include('single_pages.urls')),
    path('todo/', include('todo_app.urls')),
    path('calendar/', include('calendar_app.urls')),
    path('greenhouse/', include('greenhouse_reservation.urls', namespace='greenhouse_reservation')),  # 'greenhouse_reservation' 네임스페이스 설정
]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
