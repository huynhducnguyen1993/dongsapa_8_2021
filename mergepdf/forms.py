from django import forms
from django.forms import widgets


class PdfUploadForm(forms.Form):
    file = forms.FileField(label="",widget=forms.FileInput(attrs={"class":"form-control"}))
    page = forms.IntegerField(min_value=1, label="Nhập Trang Cần lấy",widget=forms.NumberInput(attrs={"class":"form-control"}))
    
class Pdfmerge(forms.Form):
    file = forms.FileField(label=" Chọn File PDF để  Nối ",widget=forms.FileInput(attrs={"class":"form-control","multiple":"multiple"}))

