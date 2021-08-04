
from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
import PyPDF2


# Create your views here.
def pdf_extract(request):
    
    if request.method == 'POST':
        if 'extractpdf' in request.POST:
            # If you submit via POST
            form = PdfUploadForm(request.POST, request.FILES)
            if form.is_valid():
                # Such as form validation, access to extract files page
                page_num = int(request.POST.get("page"))
                # Pdf document pages from the object code is zero, so minus 1
                page_index = page_num - 1
                # Get upload the file object
                f = request.FILES['file']
                
                # Open uploaded files, write new PDF file
                with open('original.pdf', 'wb+') as pdfFileObj:
                    for chunk in f.chunks():
                        pdfFileObj.write(chunk)

                                                               # Use PyPDF2 read the new PDF file
                        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
                    
                                         # Use PyPDF2 extract Page Object
                        pageObj = pdfReader.getPage(page_index) 
                        print(pageObj)
                                                                # Use PyPDF2 create a new PDF file objects
                        pdfWriter = PyPDF2.PdfFileWriter()
                        # Add a page object that has been read
                        pdfWriter.addPage(pageObj)
                        # Write a new page will extract the PDF file
                        with open('extracted_pages.pdf', 'wb') as pdfOutputFile:
                            pdfWriter.write(pdfOutputFile)
                        # Open a new PDF file, output by HttpResponse
                        with open('extracted_pages.pdf', 'rb') as pdfExtract:
                            response = HttpResponse(pdfExtract.read(), content_type='application/pdf')
                            response['Content-Disposition'] = 'attachment; filename="extracted_page_{}.pdf"'.format(page_num)
                            return response
                    

        if 'mergepdf' in request.POST:
            return HttpResponse("Oh my chúi ")
            
    else:
                # If the user does not pass the POST, submitting to generate an empty form
                form = PdfUploadForm()
                form_merge =Pdfmerge()
                context = {
                    'form':form,
                    'form_merge':form_merge,
                }
                return render(request, 'mergepdf/pdf.html',context)
        

     