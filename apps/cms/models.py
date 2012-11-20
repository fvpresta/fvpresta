from django.db import models

class Client(models.Model):
    name = models.CharField(max_length = 50, db_index= True, unique = True)
    logo = models.ImageField(upload_to = 'cms/clients')

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

