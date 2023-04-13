from django.contrib import admin
from django.urls import path,include
import blogapp.urls
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

import blogapp
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(blogapp.urls)),

]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)