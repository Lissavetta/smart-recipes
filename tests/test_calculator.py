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