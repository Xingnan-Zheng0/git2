
class Calculator:

	def add(self, a, b):
		return a + b

	def substract(self, a, b):
        	return a -  b

	def multiply(self, a, b):
        	return a *  b

	def divide(self, a, b):
		try:
                	return a /  b
		except ZeroDivisionError as e:
			print("Divide by Zero")

if __name__ == "__main__":
	cal = Calculator()
	print("This is in calculator.py")
	print(cal.add(1,3))
	print(cal.substract(3,1))
	print(cal.multiply(2,4))
	print(cal.divide(10,2))
	print(cal.divide(1,0))
