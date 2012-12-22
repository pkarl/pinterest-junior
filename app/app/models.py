from embedly import Embedly

from django.db import models
from django.forms import ModelForm

from settings import EMBEDLY_KEY

class Link(models.Model):
    name = models.CharField(max_length="255", editable=False)
    url = models.TextField()
    data = models.TextField(editable=False)
    date_created = models.DateTimeField(auto_now=True, editable=False)

    def save(self, *args, **kwargs):
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