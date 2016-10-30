import json


def test(a):
    return len(a[1])


user_list = {}
list = []
for i in open('transcation.txt', 'r', encoding='UTF-8'):
    list.append(json.loads(i)['results'])

print('In ready,size:', len(list))

for pages in list:
    for i in pages:
        if (i["user"] in user_list.keys()):
            if (i["value"]):
                user_list[i["user"]][0] += i["value"]
            if (i["content_ids"]):
                for j in i["content_ids"].split(','):
                    if (j):
                        user_list[i["user"]].append(j)
        else:
            user_list[i["user"]] = []
            if (i["value"]):
                user_list[i["user"]].append(i["value"])
            else:
                user_list[i["user"]].append(0)
            if (i["content_ids"]):
                for j in i["content_ids"].split(','):
                    if (j):
                        user_list[i["user"]].append(j)

print(type(user_list))
print("User list finish building~")
inc_key = []
for item in sorted(user_list.items(), key=test):
    inc_key.append(item[0])
print("Sorting finish!")
