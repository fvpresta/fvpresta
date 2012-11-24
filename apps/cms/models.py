from django.db import models

class Client(models.Model):
    name          = models.CharField(verbose_name = 'Name', max_length = 50, db_index= True, unique = True)
    url           = models.URLField(verbose_name = 'URL')
    logo          = models.ImageField(verbose_name = 'Logo',upload_to = 'cms/clients')
    display_order = models.IntegerField(verbose_name = 'Display order')

    class Meta:
        ordering = ['display_order']

    def __unicode__(self):
        return self.name

class Project(models.Model):
    client = models.ForeignKey(Client, related_name = 'projects')
    name = models.CharField(max_length = 50)

    def __unicode__(self):
        return self.name

class Capture(models.Model):
    project = models.ForeignKey(Project, related_name = 'captures')
    image = models.ImageField(upload_to = 'cms/captures')

class Carousel(models.Model):
    image = models.ImageField(upload_to = 'cms/carousel')

