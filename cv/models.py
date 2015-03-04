from django.db import models
#from projects.models import Project

# Create your models here.

class Section(models.Model):
    title = models.CharField(max_length=128)
    
    def __unicode__(self):
        return self.title
    
    @property
    def anchortitle(self):
        return self.title.split()[0]

class Entry(models.Model):
    title = models.CharField(max_length=128)
    desc = models.TextField()
    date_start = models.DateField(null=True,blank=True)
    date_end = models.DateField(null=True,blank=True)
    section = models.ForeignKey('Section')
    related_project = models.ForeignKey('projects.Project',null=True,blank=True)

    def __unicode__(self):
        return self.title

    class Meta:
#        ordering = ['-date_end','-date_start']
        ordering = ['-date_start','-date_end']
