import datetime

date = '2018-07-29'
date1 = str(datetime.date.today())

date0 = date.split('-')
date1 = date1.split('-')

date0 = int(date0[0])*365 + int(date0[1])*31 + int(date0[2])
date1 = int(date1[0])*365 + int(date1[1])*31 + int(date1[2])

a = date1 - date0

print(date0)
print(date1)

print(a)

if a > 14 :
    date = '<font color="#FF0000">'+date+'</font>'
print(date)
