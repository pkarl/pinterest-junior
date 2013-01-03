from embedly import Embedly

from django.db import models
from django.forms import ModelForm
from django.contrib import admin

from settings import EMBEDLY_KEY

class Board(models.Model):
    name = models.CharField(max_length="255")
    date_created = models.DateTimeField(auto_now=True, editable=False)

    def __unicode__(self):
        return self.name

class Link(models.Model):
    name = models.CharField(max_length="255", editable=False)
    url = models.TextField()
    data = models.TextField(editable=False)
    date_created = models.DateTimeField(auto_now=True, editable=False)
    board = models.ForeignKey(Board) # Adding FK to links
 
    def save(self, *args, **kwargs):
        """
            custom save function to grab URL information when necessary
        """
        if not self.data:
            self.set_link_data()
        super(Link, self).save(*args, **kwargs)

    def set_link_data(self):
        # connect to embedly + get url data
        client = Embedly(EMBEDLY_KEY)
        self.data = client.oembed(self.url).__dict__['data']
        self.name = self.data['title']

        # TODO: if error assert something alarming about urls + embedly

    def __unicode__(self):
        return self.name

class LinkForm(ModelForm):
    class Meta:
        model = Link

class LinkAdmin(admin.ModelAdmin):
    pass

admin.site.register(Link, LinkAdmin)

class BoardForm(ModelForm):
    class Meta:
        model = Board

class BoardAdmin(admin.ModelAdmin):
    pass

admin.site.register(Board, BoardAdmin)