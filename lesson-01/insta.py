def insta(n):
    peoples = len(n)
    if peoples == 1:
        return insta_answer_2(n , 1)
    if peoples == 2:
        return insta_answer_2(n , 2)
    if peoples == 3:
        return insta_answer_2(n , 3)
    if peoples >= 4:
        return insta_answer_2(n)

def insta_answer_3(n,a = 100):
    c = 'likes it'
    if a == 1:
        return (f'{n[0]} {c}')
    if a == 2:
        return (f'{n[0]} and {n[1]}  {c}')
    if a == 3:
        return (f'{n[0]} , {n[1]}  and {n[2]}  {c}')
    if a == 100:
        return (f'{n[0]} and {len(n) - 1}  others  {c}')

def insta_answer_2(n,a = 100):
    c = 'likes it'
    if a == 1:
        return ('{0[0]} likes it'.format(n))
    if a == 2:
        return ('{0[0]} and {0[1]} likes it'.format(n))
    if a == 3:
        return ('{0[0]} , {0[1]} and {0[2]}  likes it'.format(n))
    if a == 100:
        return ('{0[0]} and {len(n) -1 }  likes it'.format(n))

def insta_answer_1(n,a = 100):
    c = 'likes it'
    if a == 1:
        return '%s likes it'%(n)
    if a == 2:
        return '%s and %s likes it'%(n[0],n[1])
    if a == 2:
        return '%s , %s and %s likes it'%(n[0],n[1],n[2])
    if a == 100:
        return '%s and %d likes it'%(n[0], len(a) -1)




ludi = ['Вася','Петя','Андрей']
print(insta(ludi))


