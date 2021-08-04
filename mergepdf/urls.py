from django.urls import path
from . import views

# namespace
app_name = 'pdf'

urlpatterns = [
    # Upload pdf, pages need to extract user input, return to the page to be extracted
    path('tach-trang/', views.pdf_extract, name='pdf_extract'),
]