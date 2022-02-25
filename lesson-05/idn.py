import calendar
from re import A
def wtf(records,y,m,result = []):
    count = 0
    c = calendar.Calendar()
    for date,record in zip(c.itermonthdates(y,m),records):
        result.append(date.isoformat() + '  ' + record)
        count += 1
    dd = count + 1  
    arrp = records[dd:]
    if len(arrp) == 0:
        return result
    else:
        if m == 12:
            m = 1
            return wtf(arrp,y+1,m,result)
        return wtf(arrp,y,m+1,result)

def out(a):
    for i in a:
        print(i)
a = []
for i in range(30000):
    a.append(str(i))


c = wtf(a,2022,2)
out(c)