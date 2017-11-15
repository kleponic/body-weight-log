# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.models.expressions import F
from django.shortcuts import render, redirect
from django.urls.base import reverse

from bodyweightlogs.forms import BodyWeightLogForm
from bodyweightlogs.models import BodyWeightLog
from datetime import timedelta


def index(request):
    """
    Index page
    """
    data = {
        'bodyweightlogs': BodyWeightLog.objects.all().annotate(variance=F('max_weight') - F('min_weight')),
    }

    return render(request, 'index.html', data)


def detail(request, log_id):
    """
    detail page for each date
    """
    try:
        bodyweightlog = BodyWeightLog.objects.get(id=log_id)
    except Exception,e:
        raise e

    data = {
        'bodyweightlog': bodyweightlog,
        'variance': bodyweightlog.max_weight - bodyweightlog.min_weight
    }

    return render(request, 'detail.html', data)


def create(request):
    """
    Create page for body weight log
    """
    # initial form
    form = BodyWeightLogForm()

    # check for submitted data
    if request.method == "POST":

        # bound form to submitted data
        form = BodyWeightLogForm(request.POST)

        # check form validity
        if not form.is_valid():
            # display form error
            print form.errors()
        else:

            # set data
            date = form.cleaned_data.get('date')
            date_range = [date.date(), date.date()+timedelta(days=1)]
            min_weight = form.cleaned_data.get('min_weight')
            max_weight = form.cleaned_data.get('max_weight')

            # check if date is already in DB, so we update max and min
            try:
                bodyweightlog=BodyWeightLog.objects.get(date__range=date_range)
            except BodyWeightLog.DoesNotExist:
                bodyweightlog = None

            # if not yet in DB, we create one
            if not bodyweightlog:
                bodyweightlog = form.save(commit=False)

            else:
                # update value
                if min_weight < bodyweightlog.min_weight:
                    bodyweightlog.min_weight = min_weight 
                if max_weight > bodyweightlog.max_weight:
                    bodyweightlog.max_weight = max_weight 

            # save to DB
            try:
                bodyweightlog.save()
            except Exception,e:
                raise e

        # redirect to index
        return redirect(reverse('index'))

    return render(request, 'form.html', {'form': form})


def update(request, log_id):
    """
    Update page for body weight log
    """
    # retrieve instance from uuid
    try:
        bodyweightlog = BodyWeightLog.objects.get(id=log_id)
    except Exception,e:
        raise e

    # initial form
    form = BodyWeightLogForm(instance=bodyweightlog)

    # check for submitted data
    if request.method == "POST":

        # bound form to submitted data
        form = BodyWeightLogForm(request.POST, instance=bodyweightlog)

        # check form validity
        if not form.is_valid():

            # display error
            print form.errors()

        else:
            # save to DB
            try:
                form.save()
            except Exception,e:
                raise e

        # redirect to detail page
        return redirect(reverse('detail', kwargs={'log_id': log_id}))

    return render(request, 'form.html', {'form': form})



