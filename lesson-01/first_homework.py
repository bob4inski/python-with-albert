def biba(input,place, N, simbol):
    text = ''
    if place == 'center':
        for i in input:
            text += '\n  {0:{1}^{2}s}'.format(str(i),simbol,N)
    if place == 'left':
        for i in input:
            text += '\n  {0:{1}<{2}s}'.format(str(i),simbol,N)
    if place == 'right':
        for i in input:
            text += '\n  {0:{1}>{2}s}'.format(str(i),simbol,N)
    return text

ass = [12,21312,122121]
pla = 'right'
n = 111
print(biba(ass,pla,n,'*'))