import pytest
from src.calculator import add, subtract, multiply, divide, square

class TestCalculator:
    """Test class for basic calculator functions."""
    
    def test_add_positive_numbers(self):
        """Test addition with positive numbers."""
        assert add(2, 3) == 5
        assert add(0, 5) == 5
        assert add(-1, 1) == 0
    
    def test_add_negative_numbers(self):
        """Test addition with negative numbers."""
        assert add(-2, -3) == -5
        assert add(-5, 0) == -5
    
    def test_subtract_positive_numbers(self):
        """Test subtraction with positive numbers."""
        assert subtract(5, 3) == 2
        assert subtract(3, 5) == -2
        assert subtract(0, 5) == -5
    
    def test_subtract_negative_numbers(self):
        """Test subtraction with negative numbers."""
        assert subtract(-2, -3) == 1
        assert subtract(-5, 0) == -5
    
    def test_multiply_positive_numbers(self):
        """Test multiplication with positive numbers."""
        assert multiply(2, 3) == 6
        assert multiply(0, 5) == 0
        assert multiply(1, 5) == 5
    
    def test_multiply_negative_numbers(self):
        """Test multiplication with negative numbers."""
        assert multiply(-2, 3) == -6
        assert multiply(-2, -3) == 6
    
    def test_divide_positive_numbers(self):
        """Test division with positive numbers."""
        assert divide(6, 2) == 3
        assert divide(5, 2) == 2.5
        assert divide(0, 5) == 0
    
    def test_divide_negative_numbers(self):
        """Test division with negative numbers."""
        assert divide(-6, 2) == -3
        assert divide(-6, -2) == 3
    
    def test_divide_by_zero(self):
        """Test division by zero raises ValueError."""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(5, 0)
    
    def test_divide_by_zero_negative(self):
        """Test division by zero with negative numbers."""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(-5, 0)

    def test_square_positive_numbers(self):
        """Test squaring positive numbers."""
        assert square(2) == 4
        assert square(0) == 0
        assert square(1) == 1

    def test_square_negative_numbers(self):
        """Test squaring negative numbers."""
        assert square(-2) == 4
        assert square(-5) == 25
        assert square(-1) == 1

# Additional test functions outside the class
def test_add_floats():
    """Test addition with floating point numbers."""
    assert add(2.5, 3.5) == 6.0
    assert add(0.1, 0.2) == pytest.approx(0.3, rel=1e-9)

def test_multiply_floats():
    """Test multiplication with floating point numbers."""
    assert multiply(2.5, 3.0) == 7.5
    assert multiply(0.1, 0.2) == pytest.approx(0.02, rel=1e-9)