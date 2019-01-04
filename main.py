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
	
	
	a = [1, 4, 5]
	b = [2, 3, 3]
	c = [1, 2, 3]
	print(triplets(a, b, c))