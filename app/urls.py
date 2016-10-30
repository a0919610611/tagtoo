#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', Homepage),
    url(r'^result', Result),
]
