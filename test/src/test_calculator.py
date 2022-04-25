from app.src.calculator import Calculator

cal = Calculator()

def test_add():
	assert cal.add(1,1) == 2
	assert cal.add(1,2) == 3
	assert cal.add(2,3) == 4

def test_substract():
	assert cal.substract(2,1) == 1
	assert cal.substract(5,1) == 4


