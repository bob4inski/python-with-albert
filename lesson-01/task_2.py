def num_2_num(num, syst):
    stroka = '{0:%s}'%(syst)
    return stroka.format(num)

num = 8
syst = 'b'
print(num_2_num(num,syst))