import os
import requests
import pandas as pd
import numpy as np

def get_num():
    '''获取URL中的随机数'''
    num_get = requests.get("https://python666.cn/cls/number/guess/").text
    return num_get

def creat_file(name):
    with open('game_many_user.text','w',encoding='utf-8')as f:
        file = pd.DataFrame([],columns=['姓名','次数','最少猜出答案数','平均猜出答案数'])
        file.to_csv('game_many_user.text',sep=' ',index=False)
        handle_file(name)

def file_exists(name):
    if os.path.exists('game_many_user.text'):
        handle_file(name)
    else:
        creat_file(name)



def handle_file(name):
    text = pd.read_table('game_many_user.text',encoding='utf-8',sep=' ')
    #text = text.astype(str)

    y =text[text['姓名'].astype(str).str.contains(name)].index.tolist()
    print(y)
    if y :
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        #for i in range(text.shape[0]):
        i = y[0]
        if name == text.loc[i,'姓名']:
            print(text.loc[i,'姓名'])
            print('{},你已经玩了{num}次，最少{num1}轮猜出答案，平均{num2:.2f}轮猜出答案，开始游戏！'.format(name,num = int(text.loc[i,'次数']),num1 = int(text.loc[i,'最少猜出答案数']),num2=float(text.loc[i,'平均猜出答案数'])))
            game_time, game_turn = start_game()
            text.loc[i, '次数'] = int(text.loc[i,'次数'])+game_time
            a = int( text.loc[i,'最少猜出答案数'])
            if a == 0:
                text.loc[i, '最少猜出答案数'] = game_turn
            else:
                if game_turn < a:
                    text.loc[i, '最少猜出答案数'] = game_turn
            text.loc[i, '平均猜出答案数'] = (a + text.loc[i, '最少猜出答案数'])/text.loc[i, '次数']
            ave = [name,text.loc[i, '次数'],text.loc[i,'最少猜出答案数'],text.loc[i, '平均猜出答案数']]
            print(ave)
            text.loc[i] = ave
            text.to_csv('game_many_user.text', sep=' ', index=False, mode='r+')
            print('{},你已经玩了{num}次，最少{num1}轮猜出答案，平均{num2:.2f}轮猜出答案，游戏结束！'.format(name,num = int(text.loc[i,'次数']),num1 = int(text.loc[i,'最少猜出答案数']),num2=float(text.loc[i,'平均猜出答案数'])))


    else:
        print("##########################################")
        print("123456789987654321")
        file = pd.DataFrame([[name,0,0,0.00]], columns=['姓名', '次数', '最少猜出答案数', '平均猜出答案数'])
        print(file)
        print('||||||||||||||||||||||||||||||||||||||||||||||')
        report = pd.concat([text, file], ignore_index=True)
        report.to_csv('game_many_user.text', sep=' ',index=False, mode='a+', header=False)
        handle_file(name)



def start_game():
    i = 1
    j = 0
    c = 0
    num = int(get_num())
    t = True
    while t:
        answer = int(input('请猜一个1-100的数字:'))
        if type(answer) is not int and answer<0 and answer>100:
            print("请输入一个1-100的整数")
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
                if c == 0:
                    c = j
                    j = 0
                else:
                    if j < c:
                        c = j
                        j = 0
                k= input("是否继续游戏？（Y/N）")
                if k.lower()== 'y':
                    i += 1

                    continue
                else:
                    t = False
    return (i,c)


name = input("请输入您的名字：")
file_exists(name)





