"""withoutrest2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from testapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD:withoutrest2/withoutrest2/urls.py
    path('api/', views.EmployeeCRUD.as_view()),
=======
    # path('api/', views.emp_data_view),
    # path('apijson/', views.emp_data_jsonview),
    # path('apijsond/', views.emp_data_jsonview),
    # path('cbvget/', views.JsonCbv.as_view())
    path('api/<int:id>/', views.StudentView.as_view()),
    path('api/', views.StudentListView.as_view()),
    path('allinone/', views.StudentCrud.as_view())


>>>>>>> 7e5f1a7f606ba64aede62341f2940cabc99deb2a:withoutrest1/withoutrest1/urls.py

]
