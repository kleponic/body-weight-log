# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from bodyweightlogs.models import BodyWeightLog
from bodyweightlogs.forms import BodyWeightLogForm
from django.urls.base import reverse


def index(request):
    """
    Index page
    """
    data = {
        'bodyweightlogs': BodyWeightLog.objects.all(),
    }

    return render(request, 'index.html', data)


def detail(request, uuid):
    """
    detail page for each date
    """
    try:
        bodyweightlog = BodyWeightLog.objects.get(uuid=uuid)
    except Exception,e:
        raise e

    data = {
        'bodyweightlog': bodyweightlog,
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


def update(request, uuid):
    """
    Update page for body weight log
    """
    # retrieve instance from uuid
    try:
        bodyweightlog = BodyWeightLog.objects.get(uuid=uuid)
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
    return redirect(reverse('detail', kwargs={'uuid': uuid}))

