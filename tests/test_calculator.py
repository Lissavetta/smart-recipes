from calculator import Calculator


def test_calculator_class_exists():
    assert Calculator is not None
    

def test_has_add_method():
    assert hasattr(Calculator(), "add")
    

def test_add_returns_number():
    assert isinstance(Calculator().add(2, 3), int)    