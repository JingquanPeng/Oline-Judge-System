# coding: utf-8
from django.shortcuts import render, redirect, reverse
from project1.apps.login.models import ParkingRecord
from django.contrib import messages
import datetime
from datetime import datetime


# select by date:
# select * from django_project1.login_parkingrecord where date(date) between '2019-10-01' and '2019-10-30';
# select by staff name:
# select * from django_project1.login_parkingrecord where staffName ="M";

# list all records
def allParkingRecord(request):
    # post: click delete or update
    if request.method == 'POST':
        item_id = request.POST.get('itemId')
        operation = request.POST.get('operationType')
        # print(item_id,operation)
        # update
        if operation == "1":
            print("Update", item_id)
            obj = ParkingRecord.objects.filter(id=item_id).first()
            # print(obj)
            # print(obj.username, obj.description)
            arrTime = obj.arrivalTime
            arrHour = int(arrTime.split(":")[0])
            arrMin = int(arrTime.split(":")[1])
            dic = {
                "id": item_id,
                "plateNumber": obj.plateNumber,
                "arrivalDate": obj.arrivalDate,
                "arrHour": arrHour,
                "arrMin": arrMin,
                "entrance": obj.entrance,
                "staffName": obj.staffName,
                "status": obj.status
            }
            hour_list = [i for i in range(0, 24)]
            min_list = [i for i in range(0, 60)]
            return render(request, 'addParkingRecord.html', {'obj': dic, 'hour_list': hour_list, 'min_list': min_list})
            # delete
        elif operation == "2":
            ParkingRecord.objects.filter(id=item_id).delete()
            messages.error(request, '删除成功!')
            print("delete", item_id)
            # search by date
        elif operation == "3":
            d = request.POST.get("searchDate")
            d = datetime.strptime(d, '%Y-%m-%d')
            # print(d)
            # print(type(d))
            record_list = ParkingRecord.objects.filter(arrivalDate=d)
            return render(request, 'parkingRecordList.html', {'data': record_list})
        elif operation == "4":
            n = request.POST.get('searchName')
            record_list = ParkingRecord.objects.filter(staffName=n)
            return render(request, 'parkingRecordList.html', {'data': record_list})
    # select all
    record_list = ParkingRecord.objects.all()

    # select by staff name
    # record_list = ParkingRecord.objects.filter(staffName='M')
    # select * from django_project1.login_parkingrecord where staffName ="M";

    # select by date
    # start_date = datetime.date(2019, 10, 1)
    # end_date = datetime.date(2019, 10, 30)
    # record_list = ParkingRecord.objects.filter(arrivalDate__range=(start_date, end_date))
    # select * from django_project1.login_parkingrecord where date(date) between '2019-10-01' and '2019-10-30';
    # print(hour_list)
    return render(request, 'parkingRecordList.html', {'data': record_list})


# add one parking record
def addParkingRecord(request):
    # post
    if request.method == 'POST':
        item_id = request.POST.get('id')
        plateNumber = request.POST.get('plateNumber')
        date = request.POST.get('arrivalDate')
        arrHour = request.POST.get('arrHour')
        arrMin = request.POST.get('arrMin')
        if int(arrHour) < 10:
            arrHour = "0" + arrHour
        if int(arrMin) < 10:
            arrMin = "0" + arrMin
        arrivalTime = arrHour + ":" + arrMin
        print(arrivalTime)
        staffName = request.POST.get('staffName')
        entrance = request.POST.get('entrance')
        status = request.POST.get('status')

        # print(type(item_id))
        # print(item_id, plateNumber, date, arrivalTime, staffName, entrance, status)
        # update
        if item_id != "-1":
            rid = int(item_id)
            # record = PurchaseRecord.objects.get(id=rid).update(username=username, description=description,
            #                                                    money=money, type=type_status)
            record = ParkingRecord.objects.get(id=rid)
            record.plateNumber = plateNumber
            record.arrivalDate = date
            record.arrivalTime = arrivalTime
            record.staffName = staffName
            record.status = status
            record.entrance = entrance
            record.save()
            print("update", item_id)
            messages.error(request, '更新成功')
        # add new
        else:
            if len(staffName) > 10:
                messages.error(request, "长度不能超过10")
                hour_list = [i for i in range(0, 24)]
                min_list = [i for i in range(0, 60)]
                return render(request, 'addParkingRecord.html',
                              {'hour_list': hour_list, 'min_list': min_list})
            ParkingRecord.objects.create(plateNumber=plateNumber, arrivalDate=date, arrivalTime=arrivalTime,
                                         staffName=staffName, status=status, entrance=entrance)
            print("##")
            # print(item_id)
            print("add success")
            messages.error(request, '添加成功!')
        return redirect(reverse('allParkingRecord'))

    dic = {
        "id": -1
    }
    hour_list = [i for i in range(0, 24)]
    min_list = [i for i in range(0, 60)]
    return render(request, 'addParkingRecord.html', {'obj': dic, 'hour_list': hour_list, 'min_list': min_list})
