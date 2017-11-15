# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.models.expressions import F
from django.shortcuts import render, redirect
from django.urls.base import reverse

from bodyweightlogs.forms import BodyWeightLogForm
from bodyweightlogs.models import BodyWeightLog


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
    # bound form to submitted data
    form = BodyWeightLogForm(request.POST)

    # save to DB
    try:
        form.save()
    except Exception,e:
        raise e

    # redirect to index
    return redirect(reverse('index'))


def update(request, log_id):
    """
    Update page for body weight log
    """
    # retrieve instance from uuid
    try:
        bodyweightlog = BodyWeightLog.objects.get(id=log_id)
    except Exception,e:
        raise e

    # bound form to submitted data
    form = BodyWeightLogForm(request.POST, instance=bodyweightlog)

    # save to DB
    try:
        form.save()
    except Exception,e:
        raise

    # redirect to detail page
    return redirect(reverse('detail', kwargs={'log_id': log_id}))

