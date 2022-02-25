import optparse

import matplotlib.pyplot as pl
import setuptools.command.alias

#
pl.xlabel('arrr')
pl.ylabel('y')
x = ['хуй','oleni','raki','gays','boyzzz']
y = [3,1,4,5,6]

bars = pl.bar(x,y)
pl.title('Alla from kazahstan')
pl.grid(True) #отображение координатной сетки

for bar in bars:
    bar.set_color('r')
bars[0].set_color('b')
pl.show()