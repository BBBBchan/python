#定义类
class Person():
	def __init__(self, name):
		self.name = name

hunter = Person('Elmer Fudd')
print('The mighty hunter:', hunter.name)

class MDPerson(Person):
	def __init__(self, name):
		self.name = "Doctor " + name
class JDPerson(Person):
	def __init__(self, name):
		self.name = name + ", Esquire"
person = Person('Fudd')
doctor = MDPerson('Fudd')
lawyer = JDPerson('Fudd')
print(person.name)
print(doctor.name)
print(lawyer.name)

#继承和覆盖方法和添加方法
class car():
	def exclaim(self):
		print("I'm a car")
	def greeting(self):
		print("hello!")
class Yugo(car):
	def greeting(self):
		print('Hi!')
	def need_a_push(self):
		print("A litle help here?")

give_me_a_car = car()
give_me_a_yugo = Yugo()

give_me_a_car.exclaim()		#继承
give_me_a_yugo.exclaim()	
give_me_a_car.greeting()	#覆盖
give_me_a_yugo.greeting()
give_me_a_yugo.need_a_push()

#使用super从父类获得帮助
class EmailPerson(Person):
	"""docstring for EmailPerson"""
	def __init__(self, name, email):
		super().__init__(name)
		self.email = email
bob = EmailPerson('Bob Frapples', 'bob@frapples.com')
print(bob.name)
print(bob.email)

#使用属性对特性进行访问和设置
class Duck():
	def __init__(self, input_name):
		self.hidden_name = input_name
	def get_name(self):
		print('inside the getter')
		return self.hidden_name
	def set_name(self, input_name):
		print('inside the setter')
		self.hidden_name = input_name
	name = property(get_name, set_name)
fowl = Duck('Howard')

print(fowl.name)		#自动调用get_name
print(fowl.get_name())	#手动调用

fowl.name = 'Daffy'		#自动调用set_name
fowl.set_name('Daffy')	#手动调用

#使用装饰器
class duck():
	def __init__(self, input_name):
		self.hidden_name = input_name
	@property				#使用property自动生成setter
	def name(self):
		print('inside the getter')
		return self.hidden_name
	@name.setter
	def name(self, input_name):
		print('inside the setter')
		self.hidden_name = input_name
fowl = duck('Howard')
print(fowl.name)
fowl.name = 'Donald'
print(fowl.name)

class Circle():
	def __init__(self, radius):
		self.radius = radius
	@property
	def diameter(self):
		return 2 * self.radius
c = Circle(5)
print(c.radius)
print(c.diameter)
c.radius = 7		#可以更改radius特性的值但不能直接改变diameter值（因为没有设置setter）
print(c.diameter)	#改变radius的值后diameter的值随之更新

#使用名称重整保护私有特性
class Duck():							#重新改写duck类，用__name代替hidden_name,使其无法从外部访问
	def __init__(self, input_name):
		self.__name = input_name
	@property
	def name(self):
		print('inside the getter')
		return self.__name
	@name.setter
	def name(self, input_name):
		print('inside the setter')
		self.__name = input_name
fowl = Duck('Howard')					#验证可以正常使用,但无法在外部访问__name特性了
print(fowl.name)
fowl.name = 'Donald'
print(fowl.name)
print(fowl._Duck__name)					#可以通过这种方式访问

#方法的类型
class A():
	count = 0
	def __init__(self):
		A.count += 1
	def exclaim(self):
		print("I'm an A")
	@classmethod
	def kids(cls):
		print("A has", cls.count, "little objects.")
	@staticmethod										#静态方法
	def commercial():
		print('This CoyoteWeapon has been brought to you by Acme')
easy_a = A()
breezy_a = A()
wheezy_a = A()
A.kids()
A.commercial()

#鸭子类型
class Quote():
	def __init__(self, person, words):
		self.person = person
		self.words = words
	def who(self):
		return self.person
	def says(self):
		return self.words + '.'
class QuestionQuote(Quote):
	def says(self):
		return self.words + '?'			#可以在子类的对象中访问self.words
class ExclamationQuote(Quote):
	def says(self):
		return self.words + '!'

hunter = Quote('Elmer Fudd', "I'm hunting wabbits")
print(hunter.who(), 'says:', hunter.says())
hunted1 = QuestionQuote('Bugs Bunny', "What's up, doc")
print(hunted1.who(), 'says:', hunted1.says())
hunted2 = ExclamationQuote('Daffy Duck', "It's rabbit season")
print(hunted2.who(), 'says:', hunted2.says())

class BabblingBrook():
	def __init__(self, input_name, words):
		self.name = input_name
		self.words = words
	def who(self):
		return self.name
	def says(self):
		return self.words
def who_says(obj):
	print(obj.who(), 'says', obj.says())
brook = BabblingBrook('Brook', 'Babble')
who_says(hunter)
who_says(hunted1)
who_says(hunted2)
who_says(brook)

#魔术方法
class Word():
	def __init__(self, text):
		self.text = text
	def __eq__(self, text2):
		return self.text.lower() == text2.text.lower()
	def __str__(self):
		return self.text
	def __repr__(self):
		return 'Word("'+ self.text'")'
first = Word('ha')
print(first)
second = Word('HA')
third = Word('eh')
print(first == second)
print(first == third)