#Author: Pooja Varshneya
# Find all numbers in a list that are divisble by 33

def divisible_by_33(num):
	return num % 33 == 0

def list_div_by_33(input):
	output = filter(divisible_by_33, input)
	return output

if __name__ == '__main__':
	
	input = [10,20,33,5,66]
	print list_div_by_33(input)