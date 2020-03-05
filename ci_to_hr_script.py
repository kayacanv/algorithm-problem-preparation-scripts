import sys
import os

os.chdir(os.path.dirname(os.path.realpath(__file__)))

print("input/ and output/ directories should be at the same path with the python script")




ins = sorted(list(filter(lambda x: True, os.listdir(os.path.join(os.getcwd(), 'input/')))))
outs = sorted(list(filter(lambda x: True, os.listdir(os.path.join(os.getcwd(), 'output/')))))



if len(ins) != len(outs):
    print('Number of inputs and number of output are not equal')

for i in range(len(ins)):
    
    print(i + 1)

    os.system('mv ' + os.path.join('input', ins[i]) + ' ' + os.path.join('input' , 'input' + str(i ) + '.txt'))
    os.system('mv ' + os.path.join('output', outs[i]) + ' '  + os.path.join('output' , 'output' + str(i ) + '.txt'))

os.system('zip -r input-output.zip input output')
