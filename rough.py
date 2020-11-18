t = int(input())
for _ in range(t): 
	n, k = [int(x) for x in input().split()]
	nums = [int(x) for x in input().split()]
	
	#for array of len, med at len // 2
	jump = (n + 1) // 2
	n * k  - n // 2
	total = 0
	
	first = ((n - 1) // 2) * k
	for i in range(first): 
		nums[i] = 0
	# nums[0 : ((n - 1) // 2) * k] = [0] * ((n - 1) // 2) * k
	for i in range(n * k - 1 - n // 2, -1, -(n //2 + 1)): 
		# print('I : ', i)
		n = nums[i]
		# print('N : ', n)
		total += n
	print(total)