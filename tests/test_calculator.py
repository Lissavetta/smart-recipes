from calculator import Calculator


def test_calculator_class_exists():
    assert Calculator is not None
    

def test_has_add_method():
    assert hasattr(Calculator(), "add")
    

def test_add_returns_number():
    assert isinstance(Calculator().add(2, 3), int)   
    
    
def test_add_two_and_three_is_five():
    assert Calculator().add(2, 3) == 5
    
    
def test_add_ten_and_twenty_is_thirty():
    assert Calculator().add(10, 20) == 30  
    

def test_add_negative_and_positive():
    assert Calculator().add(-5, 5) == 0   
    
    
def test_has_subtract_method():
    assert hasattr(Calculator(), "subtract")
    
    
def test_subtract_ten_minus_four_is_six():
    assert Calculator().subtract(10, 4) == 6
    
    
def test_subtract_three_minus_seven_is_minus_four():
    assert Calculator().subtract(3, 7) == -4
    
    
def test_has_multiply_method():
    assert hasattr(Calculator(), "multiply")
    
    
def test_multiply_three_and_four_is_twelve():
    assert Calculator().multiply(3, 4) == 12
    
    
def test_multiply_two_and_five_is_ten():
    assert Calculator().multiply(2, 5) == 10
    
    
def test_multiply_by_zero_is_zero():
    assert Calculator().multiply(100, 0) == 0
    
    
def test_has_divide_method():
    assert hasattr(Calculator(), "divide")
    

def test_divide_ten_by_two_is_five():
    assert Calculator().divide(10, 2) == 5