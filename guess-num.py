import random
r = random.randint(1,100)

while True:
	num = input('please guess a number')
	num = int(num)
	if num == r:
		print('right number, congratulation')
		break
	elif num > r:
		print('entered number is larger than answer')
	elif num < r:
		print('entered number is smaller than answer')

