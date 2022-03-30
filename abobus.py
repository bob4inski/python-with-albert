import itertools
a = ['1.1.1','1.2.1','1.1.2','1.2.2','1.3']
ban = sorted(a, key = lambda x:x[0])
for i in range(len(ban)):
    ban[i] = ban[i].split('.')
print(ban)
f = itertools.groupby(ban)

for i,j in f:
    print(i)
  