
"""
1) Написать функцию поиска первых n чисел последовательности фибоначчи (https://ru.wikipedia.org/wiki/Числа_Фибоначчи)
	fib(10) -> [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
	fib(1) -> [0]
	fib(0) -> []
Желательно реализовать как с помощью циклов, так и рекурсией
"""

"""
2) https://www.codewars.com/kata/5583090cbe83f4fd8c000051
""" 

#2)
def digitize(n):
    ls = []
    for i in str(n):
		    ls.append(int(i))
    return ls[::-1]

#print(digitize(12345))

#1)пока не разобрался с этим 

def fib(a):
	n = 0
	lst = []
	while n != a:
		lst.append(n)
		n += 1
	return lst

print(fib(10))