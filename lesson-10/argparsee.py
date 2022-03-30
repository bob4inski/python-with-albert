import argparse
import sys
import os



def rabote(a,b):
  
    if os.path.exists(a) and os.path.isfile(a):
       
        if os.path.exists(b) and os.path.isdir(b):
            if b[-1] != '/':
                b += '/'
                
            print(a,b)
            with open(a) as f:
                k = 1

                for line in f:
                    filename = f'{b}{sourse}{k}.txt'
                    with open(filename, 'w') as d:
                        d.write(line)
                        print('jj')
                    k += 1
                    
    else:
        print('gg')


parser = argparse.ArgumentParser()
parser.add_argument('-i','--input')
parser.add_argument('-o','--output')


args = parser.parse_args(sys.argv[1:])
rabote(args.input, args.output)



