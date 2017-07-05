from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.db.models import Sum, Avg

from collections import OrderedDict

from mysites.models import MySite, MySiteValues

class ListMySites(ListView):
    '''
    List all my sites
    '''
    model = MySite

class MySiteDetail(DetailView):
    '''
    My Sites Details
    '''
    model = MySite

class ListMySitesSum(ListView):
    '''
    Summary - Sum of A values and sum of B values
    '''
    model = MySite
    template_name = 'mysites/mysite_summary.html' 

    def get_context_data(self, **kwargs):
        context = super(ListMySitesSum, self).get_context_data(**kwargs)

        #Python Programming to find sum of A Values and sum of B values
        sum_dict = OrderedDict()
        site_values = MySiteValues.objects.all().order_by('mysite__id').values('mysite__name', 'a_value', 'b_value')
        for value_dict in site_values:
            if sum_dict.has_key(value_dict['mysite__name']):
                sum_dict[value_dict['mysite__name']]['a_sum'] += value_dict['a_value']
                sum_dict[value_dict['mysite__name']]['b_sum'] += value_dict['b_value']
            else:
                sum_dict[value_dict['mysite__name']] = {'a_sum': value_dict['a_value'], 
                                                           'b_sum': value_dict['b_value']}

        context.update({"sum_dict": sum_dict})
        return context

class ListMySitesAvg(ListView):

    '''
    Summary - Average of A values and sum of B values
    '''

    model = MySite
    template_name = 'mysites/mysite_summary_average.html' 

    def get_context_data(self, **kwargs):
        context = super(ListMySitesAvg, self).get_context_data(**kwargs)

        #Using Raw SQL
        sites = MySiteValues.objects.raw("select ms.*, (select avg(msv.a_value) from mysites_mysitevalues msv where msv.mysite_id = ms.id) avg_a_value, (select avg(msv.b_value) from mysites_mysitevalues msv where msv.mysite_id = ms.id) avg_b_value from mysites_mysite ms") 

        #We can also use Django ORM annotate to find avg
        #sites = MySite.objects.annotate(a_avg=Avg('mysitevalues__a_value'), b_avg=Avg('mysitevalues__b_value')) 
        
        context.update({"sites": sites})
        return context
