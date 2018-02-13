number_List = [number for number in range(1,6) ]
print(number_List)

number_List1 = [number-1 for number in range(1,6) ]
print(number_List1)

a_list = [number for number in range(1,6) if number % 2 == 1 ]
print(a_list)

rows = range(1,4)
cols = range(1,3)
cells = [(row, col) for row in rows for col in cols]
for cell in cells:
	print(cell)
for row, col in cells:
	print(row, col)

#字典推导式
word = 'letters'
letter_counts = {letter : word.count(letter) for letter in set(word)}
print(letter_counts)