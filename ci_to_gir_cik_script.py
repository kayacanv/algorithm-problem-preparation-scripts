#Hackerrank To kamp.ubilo
import sys
import os

os.chdir(os.path.dirname(os.path.realpath(__file__)))

print("input/ and output/ directories should be at the same path with the python script")
problem_name = input("Please enter filename of the problem: ")
dir_name = input("Please enter output directory name of new inputs: ")


ins = sorted(list(filter(lambda x: x.endswith('.txt'), os.listdir(os.path.join(os.getcwd(), 'input/')))))
outs = sorted(list(filter(lambda x: x.endswith('.txt'), os.listdir(os.path.join(os.getcwd(), 'output/')))))

if len(ins) != len(outs):
    print('Number of inputs and number of output are not equal')

if not os.path.isdir(os.path.join(os.getcwd(), dir_name)):
    os.mkdir(dir_name)

for i in range(len(ins)):
    
    print(i + 1)

    os.system('cp ' + os.path.join('input', ins[i]) + ' ' + os.path.join(dir_name, problem_name + '.' + str(i + 1) + '.gir'))
    os.system('cp ' + os.path.join('output', outs[i]) + ' ' + os.path.join(dir_name, problem_name + '.' + str(i + 1) + '.cik'))