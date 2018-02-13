rabbits = ['Flopsy', 'Mospy', 'Cottontail', 'Peter']
for rabbit in rabbits:
	print(rabbit)

string = 'hello, may I have sex with you?'
for letter in string:
	print(letter)

accusation = {'room': 'ballroom', 'weapen': 'lead pipe',
				'preson': 'Col. Mustard'}

for key in accusation:
	print(key)

for value in accusation.values():
	print(value)

for item in accusation.items():
	print(item)

for card, contents in accusation.items():
	print('Card', card, 'has the contents', contents)
