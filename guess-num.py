start = input('please decide the start number') #決定隨機數字開始值
end = input('pease diced the end number') #決定隨機數字結束值
start = int(start)
end = int(end)

import random
r = random.randint(start, end)
count = 0
while True:
	count = count + 1 # count += 1 
	num = input('please guess a number')
	num = int(num)
	if num == r:
		print('right number, congratulation')
		print('this is', count, 'time you guested')
		break
	elif num > r:
		print('entered number is larger than answer')
	elif num < r:
		print('entered number is smaller than answer')
	print('this is', count, 'time you guested')
