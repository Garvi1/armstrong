num = int(input("enter a number"))
  
sum = 0
count = 0

#calculate number of individual digit
temp = num
while temp > 0:
	     count = count + 1
         temp  //= 10
#finding armstrong number

temp = num
while temp > 0:
	remainder = temp % 10
	sum = sum + (remainder**count)
    temp = temp//10
#num==sum
if num==sum:
	print('its an armstrong number')
else:
    print('its not an armstrong number')	