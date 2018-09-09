from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from . import models
from . models import bookingq
import time
import datetime
import json

def index(request):
    return render(request, 'work/news.html')

def scrapy(request):
    bk = models.bookingq()

    # 定时任务
    # 设定一个标签 确保是运行完定时任务后 再修改时间
    flag = 0
    # 获取当前时间
    now = datetime.datetime.now()
    # 启动时间
    # 启动时间为当前时间 加5秒
    sched_timer = datetime.datetime(now.year, now.month, now.day, now.hour, now.minute,
                                    now.second) + datetime.timedelta(seconds=5)
    # 启动时间也可自行手动设置
    # sched_timer = datetime.datetime(2017,12,13,9,30,10)
    while True:
        time.sleep(1)
        # 当前时间
        bk = models.bookingq()
        now = datetime.datetime.now()
        print(now)
        print(sched_timer)
        # print(datetime.timedelta(seconds=2))
        # 本想用当前时间 == 启动时间作为判断标准，但是测试的时候 毫秒级的时间相等成功率很低 而且存在启动时间秒级与当前时间毫秒级比较的问题
        # 后来换成了以下方式，允许1秒之差
        if sched_timer < now < sched_timer + datetime.timedelta(seconds=2):
            time.sleep(1)
            print("抓取時間",now,'flag:',flag)
            # 运行程序
            bk.gooo()
            # 将标签设为 1
            flag += 1
            # print(flag)
        else:
            # print(flag)
            # 标签控制 表示主程序已运行，才修改定时任务时间
            if flag == 1:
                # 修改定时任务时间 时间间隔为2分钟
                sched_timer = sched_timer + datetime.timedelta(seconds=600)
                flag = 0
# Create your views here.
def news(request):
    bk = models.bookingq()

    # # 定时任务
    # # 设定一个标签 确保是运行完定时任务后 再修改时间
    # flag = 0
    # # 获取当前时间
    # now = datetime.datetime.now()
    # # 启动时间
    # # 启动时间为当前时间 加5秒
    # sched_timer = datetime.datetime(now.year, now.month, now.day, now.hour, now.minute,
    #                                 now.second) + datetime.timedelta(seconds=5)
    # # 启动时间也可自行手动设置
    # # sched_timer = datetime.datetime(2017,12,13,9,30,10)
    # while True:
    #     # 当前时间
    #     bk = models.bookingq()
    #     now = datetime.datetime.now()
    #     # print(now)
    #     # print(sched_timer)
    #     # print(datetime.timedelta(seconds=2))
    #     # 本想用当前时间 == 启动时间作为判断标准，但是测试的时候 毫秒级的时间相等成功率很低 而且存在启动时间秒级与当前时间毫秒级比较的问题
    #     # 后来换成了以下方式，允许1秒之差
    #     if sched_timer < now < sched_timer + datetime.timedelta(seconds=2):
    #         time.sleep(1)
    #         print("抓取時間",now)
    #         # print(sched_timer)
    #         # 运行程序
    #         bk.gooo()
    #         # 将标签设为 1
    #         flag += 1
    #         # print(flag)
    #     else:
    #         # print(flag)
    #         # 标签控制 表示主程序已运行，才修改定时任务时间
    #         if flag == 1:
    #             # 修改定时任务时间 时间间隔为2分钟
    #             sched_timer = sched_timer + datetime.timedelta(seconds=120)
    #             flag = 0

    go = []
    go = bk.news()
    listt=[]
    listn=[]
    listh=[]
    


    count=0
    # for x in range(0,3):
    for io in go:
        listt.append(io[0])
        listn.append(io[1])
        listh.append(io[2])
        count+=1
        if count == 3:
            break
        # print(listt,listn,listh)
    # print(go)
    # title = io[0]
    # news = io[1]
    # http = io[2]
    listt1 = listt[0]
    listt2 = listt[1]
    listt3 = listt[2]

    listn1 = listn[0]
    listn2 = listn[1]
    listn3 = listn[2]

    listh1 = listh[0]
    listh2 = listh[1]
    listh3 = listh[2]
    go_dic = {}
    go_dic = {'listt1':listt1,'listt2':listt2,'listt3':listt3, 'listn1':listn1,'listn2':listn2,'listn3':listn3, 'listh1':listh1,'listh2':listh2,'listh3':listh3}
    print('data')
    time.sleep(2)
    # return JsonResponse(go_dic)
    response = JsonResponse(go_dic, json_dumps_params={'ensure_ascii':False})
    return response
        # return render(request,'work/news.html',locals()) 

# def prtt(request):
#         bk = models.bookingq()
#         go = []
#         go = bk.news()
#         listt=[]
#         listn=[]
#         listh=[]
        
#         count=0
#         # for x in range(0,3):
#         for io in go:
#             listt.append(io[0])
#             listn.append(io[1])
#             listh.append(io[2])
#             count+=1
#             if count == 3:
#                 break
#             print(listt,listn,listh)
#         # print(go)
#         # title = io[0]
#         # news = io[1]
#         # http = io[2]
#         listt1 = listt[0]
#         listt2 = listt[1]
#         listt3 = listt[2]

#         listn1 = listn[0]
#         listn2 = listn[1]
#         listn3 = listn[2]

#         listh1 = listh[0]
#         listh2 = listh[1]
#         listh3 = listh[2]
#         go_dic = {}
#         go_dic = {'listt1':listt1,'listt2':listt2,'listt3':listt3, 'listn1':listn1,'listn2':listn2,'listn3':listn3, 'listh1':listh1,'listh2':listh2,'listh3':listh3}
#         print('data')
#         time.sleep(2)
#         # return JsonResponse(go_dic)
#         response = JsonResponse(go_dic, json_dumps_params={'ensure_ascii':False})
#         return response
#         #return render('work/news.html',locals())




