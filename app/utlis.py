#!/usr/bin/env python3
# -*- coding: utf-8 -*from .models import *
import os, django, sys

sys.path.append('../')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tagtoo.settings")
django.setup()
from django.conf import settings
from app.models import *
from datetime import datetime as dt
from datetime import timedelta

BASE_DIR = settings.BASE_DIR
result_path = os.path.join(BASE_DIR, 'app/result.txt')
result_path2 = os.path.join(BASE_DIR, 'app/result2.txt')
print(result_path)

t = timedelta(days=7)


def result():
    print('update')
    Now = dt.today()
    From = Now - t
    trans = Transcation.objects.filter(purchase_time__range=[From, Now])
    dict = {}
    mid = {}
    cnt = {}
    Ans = {}
    for i in range(24):
        dict[i] = {}
        mid[i] = 0
        cnt[i] = 0
    for tran in trans:
        Time = tran.purchase_time
        currency = tran.currency
        # print(Time)
        hour = Time.hour
        # print(tran.content_ids)
        try:
            content_ids = tran.content_ids.split(',')
        except:
            content_ids = []
        for id in content_ids:
            try:
                obj = Product.objects.get(product_key=id)
            except:
                continue
            price = obj.price
            if currency != "TWD":
                price *= 4.5
            mid[hour] += price
            cnt[hour] += 1
            price = (price // 10) * 2 + 1
            try:
                dict[hour][price] += 1
            except:
                dict[hour][price] = 1
    for i in range(24):
        now_dict = dict[i]
        max_k = 0
        max_v = 0
        count = 0
        sum_k = 0
        for k, v in now_dict.items():
            if v > max_v:
                max_v = v
                sum_k = k
                count = 1
            elif v == max_v:
                sum_k += k
                count += 1
        try:
            ans = (sum_k / count) * 5
        except:
            ans = 0
        try:
            Ans[i] = [ans, mid[i] / cnt[i]]
        except:
            Ans[i] = [ans, 0]
        now = dt.now()
    Ans['update_time'] = now
    f = open(result_path, 'w')
    print(Ans, file=f)
    f.close()


def test(a):
    return len(a[1])


def result2():
    user_list = {}
    list = []
    Now = dt.today()
    From = Now - t
    trans = Transcation.objects.filter(purchase_time__range=[From, Now])
    cnt = 0
    for tran in trans:
        print(cnt)
        cnt += 1
        if (tran.user in user_list.keys()):
            if (tran.value):
                user_list[tran.user][0] += tran.value
            if (tran.content_ids):
                for j in tran.content_ids.split(','):
                    try:
                        product = Product.objects.get(product_key=j)
                    except:
                        continue
                    user_list[tran.user].append(product)
        else:
            user_list[tran.user] = []
            if (tran.value):
                user_list[tran.user].append(tran.value)
            else:
                user_list[tran.user].append(0)
            if (tran.content_ids):
                for j in tran.content_ids.split(','):
                    if (j):
                        try:
                            product = Product.objects.get(product_key=j)
                        except:
                            continue
                        user_list[tran.user].append(product)

    print(type(user_list))
    print("User list finish building~")
    inc_key = []
    for item in sorted(user_list.items(), key=test):
        inc_key.append(item[0])
    print("Sorting finish!")
    dict = {}
    Ans = []
    for user in inc_key[-50:]:
        print(user)
        dict[user] = {}
        for product in user_list[user][1:]:
            Class = product.Class
            try:
                dict[user][Class] += 1
            except:
                dict[user][Class] = 1
        Ans.append({"user": user, "result": dict[user]})
    f = open(result_path2, 'w')
    print(Ans, file=f)
    f.close()
    print("finish")


if __name__ == '__main__':
# print(result2())
# print(result())
