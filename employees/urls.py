from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# ---------------- API ROUTER ----------------
router = DefaultRouter()
router.register(r'employees', views.EmployeeViewSet, basename='employee')
router.register(r'attendance', views.AttendanceViewSet, basename='attendance')

# ---------------- URL PATTERNS ----------------

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('employees/', views.employee_list, name='employee_list'),
    path('employees/add/', views.add_employee, name='add_employee'),
    path('employees/delete/<int:pk>/', views.delete_employee, name='delete_employee'),
    path('attendance/', views.attendance_list, name='attendance_list'),
    path('attendance/mark/', views.mark_attendance, name='mark_attendance'),
    path('attendance/<int:employee_id>/', views.attendance_list, name='attendance_by_employee'),
    path('api/', include(router.urls))
]
