from django import forms
from django.views.generic import FormView, ListView
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Employee, Attendance
from .serializers import EmployeeSerializer, AttendanceSerializer
from .forms import EmployeeForm, AttendanceForm
from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404

#--------------Frontend Views using Django----------------#
# Home Page
def home(request):
    return render(request, 'employees/home.html')

# Employee Views
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employees/employee_list.html', {'employees': employees})

def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Employee added successfully!')
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'employees/add_employee.html', {'form': form})

def delete_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    employee.delete()
    messages.success(request, 'Employee deleted successfully!')
    return redirect('employee_list')

# Attendance Views
def attendance_list(request, employee_id=None):
    if employee_id:
        attendances = Attendance.objects.filter(employee_id=employee_id)
    else:
        attendances = Attendance.objects.all()
    return render(request, 'employees/attendance_list.html', {'attendances': attendances})

def mark_attendance(request):
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            employee = form.cleaned_data['employee']
            date = form.cleaned_data['date']

            # Check if attendance already exists
            if Attendance.objects.filter(employee=employee, date=date).exists():
                messages.error(request, f"Attendance for {employee.full_name} on {date} already exists!")
            else:
                form.save()
                messages.success(request, f"Attendance for {employee.full_name} on {date} recorded successfully!")
                return redirect('attendance_list')
        else:
            # Show form errors
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = AttendanceForm()
    
    return render(request, 'employees/mark_attendance.html', {'form': form})

    
#--------------Backend API views----------------#

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if Employee.objects.filter(employee_id=serializer.validated_data['employee_id']).exists():
            return Response({"error": "Employee ID exists"}, status=status.HTTP_400_BAD_REQUEST)
        if Employee.objects.filter(email=serializer.validated_data['email']).exists():
            return Response({"error": "Email exists"}, status=status.HTTP_400_BAD_REQUEST)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if Attendance.objects.filter(employee=serializer.validated_data['employee'],
                                     date=serializer.validated_data['date']).exists():
            return Response({"error": "Attendance exists"}, status=status.HTTP_400_BAD_REQUEST)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
