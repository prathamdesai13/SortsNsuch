from Algos import sorts
from random import random
from RandyDandyProblems import *
from DataStructs.Stack import Stack
if __name__ == '__main__':
	
	s = Stack()
	s.display()
	s.push(10)
	s.push(20)
	s.display()
	print(s.size())
	x = s.pop()
	print(s.size())
	s.display()
	print(x)
	s.pop()
	s.display()
	s.pop()
