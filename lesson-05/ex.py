import calendar

def wtf(a,month)
c = calendar.Calendar()
for i in c.iterweekdays():
    print(i)
    for day in c.itermonthdates(2022,2):
        print(day)