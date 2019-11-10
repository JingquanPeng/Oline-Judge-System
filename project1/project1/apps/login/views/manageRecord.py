# encoding: utf-8
from django.shortcuts import render, redirect, reverse
from project1.apps.login.models import PurchaseRecord
from django.contrib import messages

# list all records
def allRecord(request):
    # post: click delete or update
    if request.method == 'POST':
        item_id = request.POST.get('itemId')
        operation = request.POST.get('operationType')
        # print(item_id,operation)
        # update
        if operation == "1":
            print("Update", item_id)
            obj = PurchaseRecord.objects.filter(id=item_id).first()
            # print(obj)
            # print(obj.username, obj.description)
            dic = {
                "id": item_id,
                "username": obj.username,
                "date": obj.date,
                "description": obj.description,
                "money": obj.money
            }
            return render(request, 'addPurchaseRecord.html', {'obj': dic})
            # delete
        elif operation == "2":
            PurchaseRecord.objects.filter(id=item_id).delete()
            messages.error(request, '删除成功!')
            print("delete", item_id)
    record_list = PurchaseRecord.objects.all()
    return render(request, 'PurchaseRecordList.html', {'data': record_list})


# add or update one record
def addRecord(request):
    # post
    if request.method == 'POST':
        item_id = request.POST.get('id')
        username = request.POST.get('username')
        date = request.POST.get('date')
        description = request.POST.get('description')
        money = request.POST.get('money')
        type_status = request.POST.get('status')
        print(type(item_id))
        # update
        if item_id != "-1":
            rid = int(item_id)
            # record = PurchaseRecord.objects.get(id=rid).update(username=username, description=description,
            #                                                    money=money, type=type_status)
            record = PurchaseRecord.objects.get(id=rid)
            record.username = username
            record.description = description
            record.money = money
            record.type = type_status
            record.save()
            print("update", item_id)
            messages.error(request, '更新成功')
        # add new
        else:
            PurchaseRecord.objects.create(username=username, description=description
                                          , money=money, type=type_status)
            print("##")
            print(item_id, username, description, date, money, type_status)
            print("add success")
            messages.error(request, '添加成功!')
        return redirect(reverse('allRecord'))

    dic = {
        "id": -1,
        "username": "",
        "date": "",
        "description": "",
        "money": ""
    }
    return render(request, 'addPurchaseRecord.html', {'obj': dic})
