import pandas as pd
report = pd.read_table('report.txt',encoding='utf-8',sep=' ')   #读取text文件

ave = []

for j in range(report.shape[0]):    #按照DF的行进行遍历
    b= "{num:.1f}".format(num =report.loc[j][1:].mean())    #从每一行的第2个数字开始，每一个人的分数平均值
    ave.append(float(b))    #将算出的平均值按照顺序存入一个空列表中
report['平均分'] = ave     #将算出的平均值按照列加入DF中，columns为“平均分”
report = report.sort_values(by = '平均分',ascending=False).reset_index(drop=True)  #按照平均分降序排列，并重置index

ave1 = []

for i in report.columns[1:]:    #按照DF的列进行遍历
    a = "{num:.1f}".format(num = report[i].mean())  #对每一门学科进行计算平均分
    ave1.append(a)      #将每门学科的平均分存入一个空列表
ave1.insert(0,'平均')

#因无法用函数和方法将学科的平均分加入第一行，所以将其构建为一个DF，用concat方法将两个DF拼接
insertRow = pd.DataFrame([ave1],columns=['姓名','语文','数学','英语','物理','化学','生物','政治','历史','地理','平均分'])
report = pd.concat([insertRow,report],ignore_index=True)

#report = report.astype(str)
for k in range(report.shape[0]):
    for c in report.columns[1:]:
        if float(report.loc[k,c]) < 60:
            report.loc[k, c] = '不及格'
report.index.name = '名次'    #将index重命名为名次
report.to_csv('result.text', sep=' ', mode='a+')
