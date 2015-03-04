from django.db import models

PAGE_CHOICES = (('l','left'),('r','right'))

class Page(models.Model):
    nav_side = models.CharField(max_length=1, choices=PAGE_CHOICES)
    nav_pos = models.PositiveIntegerField()
    nav_show = models.BooleanField(default=False)
    nav_icon = models.CharField(max_length=64)          # the icon
    nav_heading = models.CharField(max_length=32)       # the name
    
    page_heading = models.CharField(max_length=256)
    page_body = models.TextField()
    page_slug = models.SlugField(max_length=16)
    
    # todo add field for heading pattern.
    
    def __unicode__(self):
        return "<Page(%s)>" % (self.nav_heading, )