import os
import sys
from random import randint
import numpy as np
import string
import random




SUBTASKS = [2, 10, 25]
LIMITS_N = [15, 1000,100000]
LIMITS_T = [15, 10000, 1e5]
LIMITS_NUMS = [20, 1e3, 1e5]

def prepare_input(i):
	input_path = 'input/input{}.txt'.format('0'+str(i) if i<10 else i)
	output_path = 'output/output{}.txt'.format('0'+str(i) if i<10 else i)


	print('Generating '+ str(i) + 'th input...' ) 

	tot = 0
	for j in range(len(SUBTASKS)):
		tot += SUBTASKS[j]
		
		if tot >= i:
			curr = j
			break

	#Prepare custom input here
	with open(input_path, 'w+') as input_file:


		n = give_num(LIMITS_N[curr], i)
		write_line_to_file(input_file, [n])

		write_line_to_file(input_file, permutation(n))

#		q = give_num(LIMITS_T[curr], i)
#		write_line_to_file(input_file, [q])
#		for j in range(q):
#			write_line_to_file(input_file, two_random_input(n,i))
			

	execute('./sol < ' + input_path + ' > ' + output_path)


def sample_case():
	prepare_input(1)

	print("Sample Input:")

	execute("cat input/input01.txt")

	print("Sample Output:")

	execute("cat output/output01.txt")

	resp = input("Does it look right? Press 'y/Y' to continue.")

	if resp != 'y' and resp != 'Y':

		print('Code aborted.')
		sys.exit()

def write_line_to_file(input_file, lst):
	input_file.write(' '.join(list(map(str,lst))) + '\n')

def two_random_input_large(limit):
	
	x = randint(1 , min(limit/10, 1000))
	y = randint(max(limit - limit/10 , 1) , limit)

	if x > y:
		x,y = y,x

	return [x,y]

def two_random_input(mx, i): # Second One Always is Bigger
	if randint(0,1) == 0:
		try:
			return two_random_input_large(mx) 
		except:
			pass
	x = randint(1, mx)
	y = randint(1, mx)
	if x > y:
		x,y = y,x
	return [x,y]

def give_num(mx, i, min_value = 1):

	mn = min(mx - mx//10, min_value)

	return randint(mn,mx)

def construct_chain(n):
	edges = []
	for i in range( 2 ,n - n//10):
		edges.append(str(i) + ' ' + str(i-1))

	for i in range(n - n//10, n+1):
		edges.append(str(i) + ' ' + str(randint(1,i-1)))

	return ['\n'.join(edges)]

def construct_long_tree(n):
	edges = []
	for i in range(2,n+1):
		edges.append(str(i) + ' ' + str(randint(max(1,i-15),i-1)))

	return ['\n'.join(edges)]

def construct_random_tree(n):
	edges = []
	for i in range(2,n+1):
		edges.append(str(i) + ' ' + str(randint(1,i-1)))

	return ['\n'.join(edges)]

def construct_tree(n):
	
	if randint(0,4) == 0:
		return construct_chain(n)

	if randint(0,3) != 0:
		return construct_long_tree(n)

	return construct_random_tree(n)

def permutation(n):
	
	return list(np.random.permutation(range(1,n+1)))


def execute(s):
    print(s)
    os.system(s)

# def construct_graph(n , m, isweighted):
# 	grb, edges = construct_tree(n)

# 	for i in range(len(edges)):
# 		edges[i] = edges[i] + ((' ' + str(randint(1,n)))*isweighted)


# 	for i in range(n,m+1):
# 		x = y = 0
# 		while True:
# 			x = randint(1,n)
# 			y = randint(1,n)
# 			if x != y:
# 				break
# 		edges.append(str(x) + ' ' + str(y) + ((' ' + str(randint(1,n)))*isweighted))

# 	return ['\n'.join(edges)],edges


def random_array(mx,n):
	return [randint(1,mx) for x in range(n)]

def random_string(string_length):
    letters = string.ascii_lowercase + string.ascii_uppercase #  + "0123456789"
    return ''.join(random.choice(letters) for i in range(stringLength))
    

execute("g++ -std=c++11 solution.cpp -osol")

execute("rm -rf input output")
execute("mkdir input && mkdir output")

sample_case()

tot_subtask = 0

for subtask_size in SUBTASKS:
	tot_subtask += subtask_size

for i in range(tot_subtask):
	prepare_input(i+1)


print('Hackerrank test wizard -- run with Python-3')
os.chdir(os.getcwd())


execute('zip -r input-output.zip input output')
