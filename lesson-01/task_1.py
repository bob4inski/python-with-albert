#первый пример форматирования
nums = [0,10,20]
print('first:{0[0]:}  second:{0[1]:}'.format(nums))
#второй прмиер
nums = [1,2,3]
#вывести строку в которой в левой части
# из 10ти символов первый эл-т из списка, а остально '!'
# в правой остальное '?'
a = 10
print('first:{0[0]:!<10}  second:{0[1]:?>10}'.format(nums))

print('int: {0:d} hex: {0:x} oct: {0:o}'.format(40))

#третий способ форматирования
a = 'text'
b = 10
print(f'{a} {b}')