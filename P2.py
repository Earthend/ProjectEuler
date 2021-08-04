prev = 1
current = 2
i = 0
total = 0

while(current < 4000000):
	if(current % 2 == 0):
		total += current 
	i = current
	current = current + prev
	prev = i

print(total)