# -*- coding:utf-8 -*-
# @Time : 2020/2/13 21:57
# @Author : Jerry

import os
import requests
import pandas as pd
import numpy as np

def get_num():
    '''
       功能：获取URL中的随机数
       参数：无
       返回值：获取到的随机数
    '''
    num_get = requests.get("https://python666.cn/cls/number/guess/").text
    return num_get

def creat_file(name):
    '''
       功能：创建文件
       参数：输入的姓名
       返回值：无
    '''
    with open('game_many_user.text','w',encoding='utf-8')as f:
        file = pd.DataFrame([],columns=['姓名','次数','最少猜出答案数','平均猜出答案数','总数'])
        file.to_csv('game_many_user.text',sep=' ',index=False)
        handle_file(name)

def file_exists(name):
    '''
       功能：检查文件是否存在，如果存在调用操作文件函数，不存在则调用创建文件函数
       参数：输入的姓名
       返回值：无
    '''
    if os.path.exists('game_many_user.text'):
        handle_file(name)
    else:
        creat_file(name)



def handle_file(name):
    '''
       功能：操作文件
       参数：输入的姓名
       返回值：无
    '''
    text = pd.read_table('game_many_user.text',encoding='utf-8',sep=' ')    #读取文件为DF数据
    if name in list(text['姓名']):    #判断输入的姓名是否在columns为“姓名”的列中，如果有执行
        y = text[text.姓名 == name].index.tolist()    #返回姓名为输入值的index列表
        i = y[0]
        data = text.loc[i]                      #将DF中有输入姓名的一行取出
        user_name = data['姓名']
        turn = int(data['次数'])
        Least_times =  int(data['最少猜出答案数'])
        ave_time = float(data['平均猜出答案数'])
        Total_time =  int(data['总数'])

        print('{},你已经玩了{num}次，最少{num1}轮猜出答案，平均{num2:.2f}轮猜出答案，开始游戏！'.format(user_name,num = int(turn),num1 = int(Least_times),num2=float(ave_time)))
        game_time, game_turn,total_turn = start_game()      #调用运行游戏函数
        turn = turn + game_time
        a = int(Least_times)
        if a == 0:
            Least_times = game_turn
        elif game_turn < a:
            Least_times = game_turn
        Total_time = Total_time + int(total_turn)
        ave_time = (Total_time/turn)
        ave = [user_name,turn,Least_times,ave_time,Total_time]
        text.loc[i] = ave
        print('{},你已经玩了{num}次，最少{num1}轮猜出答案，平均{num2:.2f}轮猜出答案，游戏结束！'.format(user_name,num = int(turn),num1 = int(Least_times),num2=float(ave_time)))
        text.to_csv('game_many_user.text', sep=' ', index=False, mode='r+')         #将结果保存入文件中

    else:   #如果输入的姓名不在文件中，添加这名用户
        file = pd.DataFrame([[name,0,0,0.00,0]], columns=['姓名', '次数', '最少猜出答案数', '平均猜出答案数','总数'])
        report = pd.concat([text, file], ignore_index=True)
        report.to_csv('game_many_user.text', sep=' ',index=False, mode='a+', header=False)
        handle_file(name)



def start_game():
    '''
           功能：运行游戏
           参数：无
           返回值：本轮游戏次数，最少猜中数，猜游戏总数
        '''
    i = 1
    j = 0
    c = 0
    m= 0
    t = True
    num = int(get_num())
    while t:
        try:
            answer = int(input('请猜一个1-100的数字:'))
            if type(answer) is not int and answer<0 and answer>100:
                print("请输入一个1-100的整数")
                continue
            else:
                if answer < num:
                    j+=1
                    print('猜小了，再试试！')
                    continue
                elif answer > num:
                    j += 1
                    print('猜大了，再试试！')
                    continue
                else:
                    j += 1
                    print('猜对了，你一共猜了{}轮'.format(j),end='')
                    m += j
                    if c == 0:
                        c = j
                        j = 0
                    else:
                        if j < c:
                            c = j
                            j = 0
                    k= input("是否继续游戏？（Y/N）")
                    if k.lower()== 'y':
                        num = int(get_num())
                        i += 1

                        continue
                    else:
                        t = False
        except ValueError:
            print("输入有误，请重新输入！")
            continue
    return (i,c,m)


name = input("请输入您的名字：")
file_exists(name)





