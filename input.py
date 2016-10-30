#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, django
import json
import datetime as dt

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tagtoo.settings")
django.setup()
from django.conf import settings
from app.models import *

Advertiser.objects.all().delete()
Product.objects.all().delete()
Transcation.objects.all().delete()
now = dt.datetime.now()
print(now)
fout = open("advertiser.txt", "r", encoding='UTF-8')
advertisers = {}
cnt = 0
c = fout.readline()
while (c):
    # print(c)
    dic = json.loads(c)
    results = dic['results']
    for result in results:
        advertiser = Advertiser()
        advertiser.id = result['id']
        advertiser.name = result['name']
        advertisers[advertiser.id] = advertiser
        print(cnt)
        advertiser.save()
    cnt += 1
    c = fout.readline()
fout.close()

print("cnt=%d" % cnt)

delta = dt.datetime.now()
print(delta - now)
now = dt.datetime.now()
fout = open('product_list.txt', "r", encoding='UTF-8')
c = fout.readline()
cnt = 0
now = dt.datetime.now()
print(now)
while (c):
    # print(c)
    dic = json.loads(c)
    product = Product()
    try:
        product.id = dic['id']
        product.product_key = dic['product_key']
        try:
            ad = advertisers[dic['advertiser']['id']]
            product.advertiser = ad
        except:
            pass
        product.price = dic['price']
        product.store_price = dic['store_price']
        product.update_time = dic['update_time']
        product.Class=dic['class']
        print(cnt)
        product.save()
    except:
        pass
    cnt += 1
    c = fout.readline()
print("cnt=%d" % cnt)
fout.close()
delta = dt.datetime.now()
print(delta - now)

fout = open('transcation.txt', "r", encoding="UTF-8")
now = dt.datetime.now()
print(now)
c = fout.readline()
cnt = 0
while (c):
    # print(c)
    dic = json.loads(c)
    results = dic['results']
    for result in results:
        transcation = Transcation()
        transcation.user = result['user']
        transcation.value = result['value']
        transcation.currency = result['currency']
        transcation.num_items = result['num_items']
        transcation.content_ids = result['content_ids']
        try:
            ad = advertisers[result['ec_id']]
            transcation.advertiser = ad
        except:
            pass
        transcation.purchase_time = result['purchase_time']
        transcation.click_time_last = result['click_time_last']
        transcation.click_time_7_days = result['click_time_7_days']
        transcation.click_time_30_days = result['click_time_7_days']
        transcation.ip = result['ip']
        transcation.user_agent = result['user_agent']
        transcation.save()
    # print(dic)
    # print(type(dic))
    c = fout.readline()
    cnt += 1
    print(cnt)
print("cnt=%d" % cnt)
delta = dt.datetime.now()
print(delta - now)
fout.close()
