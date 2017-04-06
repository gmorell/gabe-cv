import datetime
import pytz
import uuid

from adminsortable.models import SortableMixin
from django.db import models
# from imagekit.models.fields import ImageSpecField
from imagekit.models import ImageSpecField
from pilkit.processors.resize import ResizeToFill

# Create your models here.

class Project(SortableMixin, models.Model):
    
    name = models.CharField(max_length=32)
    slug = models.SlugField()
    blurb = models.TextField(null=True,blank=True)
    last_updated = models.DateTimeField(auto_now=True)
    display_class = models.CharField(max_length=32, default="bh_dots")

    display_order = models.PositiveIntegerField(default=0, editable=False, db_index=True)
    
    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['display_order']
        verbose_name_plural = 'Projects'

    @property
    def entries(self):
        return self.projectentry.filter(posted__lte=datetime.datetime.now(pytz.utc))
    
    @property
    def latest_entry(self):
        return self.entries.latest()
    
    @property
    def first_entry(self):
        return self.entries.reverse()[0]
    
    @property
    def entry_count(self):
        return self.entries.count()
    

class ExternalProjectLink(models.Model):
    """
    A link to something else
    """
    project = models.ForeignKey('Project', related_name="links")
    url = models.URLField(max_length=256)
    icon = models.CharField(max_length=32, null=True, blank=True, default="fa-external-link")
    
        
class Entry(models.Model):

    project = models.ForeignKey('Project',related_name="projectentry")
    title = models.CharField(max_length=32)
    slug = models.SlugField()
    body = models.TextField()
    
    posted = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-posted']
        get_latest_by = "posted"
        
    def __unicode__(self):
        return self.title
    
    @property
    def is_viewable(self):
        if datetime.datetime.now(pytz.utc) >= self.posted:
            return True
        else:
            return False
        
    @property
    def get_prev_in_proj(self):
        try:
            x = self.get_previous_by_posted(project=self.project)
            return x
        except:
            return False
    @property
    def get_next_in_proj(self):
        try:
            x = self.get_next_by_posted(posted__lte=datetime.datetime.now(pytz.utc))
            return x
        except:
            return False
    @property
    def get_prev(self):
        try:
            x = self.get_previous_by_posted(posted__lte=datetime.datetime.now(pytz.utc))
            return x
        except:
            return False
    
    @property
    def get_next(self):
        try:
            x = self.get_next_by_posted()
            return x
        except:
            return False

class InlineEntryImg(models.Model):
    created         = models.DateTimeField(auto_now_add=True)
    modified        = models.DateTimeField(auto_now=True)
    
    title           = models.CharField(max_length=128)
    
    image           = models.ImageField(upload_to='projects')
    image_r = ImageSpecField(
                        source='image', # for resized
                        processors=[ResizeToFill(1080, 609)],
                        format='JPEG',
                        options={'quality': 80})
    
    image_t = ImageSpecField(
                        source='image_r', # for resized
                        processors=[ResizeToFill(108, 61)],
                        format='JPEG',
                        options={'quality': 60})

    identifier      = models.UUIDField(default=uuid.uuid4)
    
    def __unicode__(self):
        return self.title
    
    class Meta:
        ordering = ['-title']