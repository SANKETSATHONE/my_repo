from django.urls import path
from employee.views import  Get_one_Employee, edit_Employee, Delete_Employee


urlpatterns = [

    path('get/<int:id>',Get_one_Employee),
    path('edit/<int:id>', edit_Employee),
    path('del/', Delete_Employee),

    ]