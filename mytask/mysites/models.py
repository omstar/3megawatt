from __future__ import unicode_literals

from django.db import models

class MySite(models.Model):
    '''
    To store all my sites with unique identifier as name
    '''
    name = models.CharField(('Site Name'), unique=True, max_length=20)

    def __unicode__(self):
        return '%s' % (self.name.title())

class MySiteValues(models.Model):
    '''
    Store A values of mysite(any site) 
    '''
    a_value = models.DecimalField(("A value"), max_digits=5, decimal_places=2)
    b_value = models.DecimalField(("B value"), max_digits=5, decimal_places=2)
    mysite = models.ForeignKey(MySite, null=True, blank=True)
    date = models.DateField(("When it is"))

    def __unicode__(self):
        return '%s' % (self.mysite.name)
