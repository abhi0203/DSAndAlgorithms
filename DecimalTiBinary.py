def decimalToBinary(num):
	assert int(num)== num, "Enter an integer"
	if num<0:
		num*=-1
	if num==0:
		return 0
	else:
		#print(num)
		return num%2 + 10* decimalToBinary(int(num/2))

print(decimalToBinary(-10))
