from Algos import sorts
from random import random
from RandyDandyProblems import *
import matplotlib.pyplot as plt
from DataStructs.LinkedList import LinkedList
from DataStructs.BinarySearchTree import BST
import time

def func1(t1, t2, n):
	if n == 1:
		return t1
	elif n == 2:
		return t2
	a = func1(t1, t2, n - 1) ** 2
	b = func1(t1, t2, n - 2)
	return a + b

if __name__ == '__main__':
	
	
	t1 = 0
	t2 = 1
	n = 28
	start_time = time.time()
	weirdFib(t1, t2, n)
	
	second_time = time.time()
	print(second_time - start_time)
	for i in range(1, n + 1):
		func1(t1, t2, i)
	third_time = time.time()
	print(third_time - second_time)