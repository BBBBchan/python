days = ['Monday', 'Tuesday', 'Wednesday']
fruits = ['banana', 'orange', 'peach']
drinks = ['coffee', 'tea', 'beer']
desserts = ['tiramisu', 'ice cream', 'pie', 'pudding']
for day, fruit, drink, dessert in zip(days, fruits, drinks, desserts):
	print(day, ": drink", drink, "- eat", fruit, ":- enjoy", dessert)

english = 'Monday', 'Tuesday', 'Wednesday'
french  = 'Lundi', 'Mardi', 'Mercredi'

a = list( zip(english, french) )
print(a)

b = dict( zip(english, french))
print(b)