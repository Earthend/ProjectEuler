current_num = 3
total = 0
while(current_num < 1000):
	if(current_num % 3 == 0 or current_num % 5 == 0):
		total += current_num
		print(total)
	current_num+=1
