# Create your views here.
from django.views.generic.detail import DetailView

from docs.models import Document

class DocumentDetail(DetailView):
    model = Document
    slug_field = "uuid"
    template_name = 'document.html'
    
    