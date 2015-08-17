from django.shortcuts import render_to_response
from django.template import Context,RequestContext
from cv.models import Section

def index(request):
    context = RequestContext(request)
    sections = Section.objects.all()
    context['sects'] = sections
    
    return render_to_response('cv_2014_2.html', context)


import cStringIO as StringIO
import ho.pisa as pisa
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from cgi import escape
from reportlab.pdfgen import canvas

def render_to_pdf(template_src, context_dict):
    template = get_template(template_src)
    context = Context(context_dict)
    html  = template.render(context)
    result = StringIO.StringIO()

    pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("UTF-8")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), mimetype='application/pdf')
    return HttpResponse('We had some errors<pre>%s</pre>' % escape(html))

#def index_as_pdf(request):
    #context = RequestContext(request)
    #sections = Section.objects.all()
    #context['sects'] = sections
    #context['pagesize'] = 'A4'
    
    #return render_to_pdf('cv_pdf.html',context)
    
#def index_as_pdf(request):
    ## Create the HttpResponse object with the appropriate PDF headers.
    #response = HttpResponse(content_type='application/pdf')
    #response['Content-Disposition'] = 'attachment; filename="cv.pdf"'

    ## Create the PDF object, using the response object as its "file."
    #p = canvas.Canvas(response)

    ## Draw things on the PDF. Here's where the PDF generation happens.
    ## See the ReportLab documentation for the full list of functionality.
    #p.drawString(100, 100, "Hello world.")

    ## Close the PDF object cleanly, and we're done.
    #p.showPage()
    #p.save()
    #return response

import os
from django.conf import settings
from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template

# Convert HTML URIs to absolute system paths so xhtml2pdf can access those resources
def link_callback(uri, rel):
    # use short variable names
    sUrl = settings.STATIC_URL      # Typically /static/
    sRoot = settings.STATIC_ROOT    # Typically /home/userX/project_static/
    mUrl = settings.MEDIA_URL       # Typically /static/media/
    mRoot = settings.MEDIA_ROOT     # Typically /home/userX/project_static/media/

    # convert URIs to absolute system paths
    if uri.startswith(mUrl):
        path = os.path.join(mRoot, uri.replace(mUrl, ""))
    elif uri.startswith(sUrl):
        path = os.path.join(sRoot, uri.replace(sUrl, ""))

    # make sure that file exists
    if not os.path.isfile(path):
            raise Exception(
                    'media URI must start with %s or %s' % \
                    (sUrl, mUrl))
    return path

def index_as_pdf(request):
    
    context = RequestContext(request)
    sections = Section.objects.all()
    context['sects'] = sections
    context['PDF_HEADER'] = settings.PDF_HEADER
    context['PDF_CONTACT'] = settings.PDF_CONTACT
    #context['pagesize'] = 'A4'
    
    #return render_to_pdf('cv_pdf.html',context)
    
    # Render html content through html template with context
    template = get_template('cv_pdf.html')
    html  = template.render(context)

    # Write PDF to file
    file = open(os.path.join(settings.MEDIA_ROOT, 'cv.pdf'), "w+b")
    pisaStatus = pisa.CreatePDF(html, dest=file,
            link_callback = link_callback)

    # Return PDF document through a Django HTTP response
    file.seek(0)
    pdf = file.read()
    file.close()            # Don't forget to close the file handle
    return HttpResponse(pdf, mimetype='application/pdf')