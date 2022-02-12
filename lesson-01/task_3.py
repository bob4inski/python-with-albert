

def tales(title, tale):
    return '{0: >{1}s} \n \t {1:} '.format(title.upper(), tale)

title = 'skazka'
tale = 'Robert pishet chota'

print(tales(title, tale))