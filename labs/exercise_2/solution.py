results = [1,2]

def divisible_by_2(num):
	return num % 2 == 0

def fibonacci():
	sum = 0
	x = 1
	y = 2
	i = 2
	while sum < 4000000:
		sum = x + y 
		x = y
		y = sum
		results.insert(i, sum)
		i = i + 1
	
	return i	

def sum_of_fib():
	n = fibonacci()
	list_num = filter(divisible_by_2, range(1,n)) 
	sum_fib_n = reduce(lambda x,y: x + results[y-1], list_num)
	return sum_fib_n


if __name__ == '__main__':
	print sum_of_fib()

