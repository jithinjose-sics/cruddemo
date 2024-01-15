from django.contrib import admin
from django.urls import path
from .import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/',views.student_list),
    path('students/<int:id>',views.student_details),
]

urlpatterns=format_suffix_patterns(urlpatterns)
