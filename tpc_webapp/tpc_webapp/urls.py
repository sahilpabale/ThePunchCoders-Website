from django.contrib import admin
from django.urls import path,include
from . import views

admin.site.site_header = "ThePunchCoders Admin"
admin.site.site_title = "ThePunchCoders Admin Panel"
admin.site.index_title = "Welcome to ThePunchCoders Admin Panel"

urlpatterns = [
    path('tpc-admin/', admin.site.urls),
    path('', include('home.urls'), name='MainHomeApp'),
    path('blog/', include('blog.urls'), name='BlogApp'),
    path('courses/', include('courses.urls'), name='CoursesApp'),
    path('account/', include('account.urls'), name='AccountApp'),
]
