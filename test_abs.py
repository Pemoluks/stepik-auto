# перепишем тест более проще - для PyTest
def test_abs1():
	assert abs(-42) == 42, "Should be abs value of a number"

def test_abs2():
	assert abs(-42) == -42, "Should be abs value of a number"

