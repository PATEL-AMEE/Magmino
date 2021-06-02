
# from django.contrib import admin
# from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]


from django.urls import include, path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path("", include("app1.urls")),
]
urlpatterns += staticfiles_urlpatterns()