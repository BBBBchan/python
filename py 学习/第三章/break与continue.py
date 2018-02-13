while True:
	stuff = input("String to capitalize [type q to quit]: ")
	if stuff == "q":
		break
	print(stuff.capitalize())

while True:
	value = input("Integer , plaese [q yo quit]: ")
	if value == "q":
		break
	number = int(value)
	if number % 2 == 0:
		continue
	print(number, "squared is", number * number)
