"""
Unit Tests for Calculator
Students start with 2 passing tests, then add more
"""
import pytest
from src.calculator import add, divide, subtract

class TestBasicOperations:
    """Test basic arithmetic operations"""
    
    def test_add_positive_numbers(self):
        """Test adding positive numbers"""
        assert add(2, 3) == 5
        assert add(10, 15) == 25
    
    def test_subtract_positive_numbers(self):
        """Test subtracting positive numbers"""
        assert subtract(5, 3) == 2
        assert subtract(10, 4) == 6

class TestMultiplyDivideWithValidation:
    """Test multiplication and division with input validation."""
    
    def test_multiply_input_validation(self):
        """Test multiply rejects non-numeric inputs."""
        with pytest.raises(TypeError, match="Both arguments must be numbers"):
            multiply("5", 3)
        with pytest.raises(TypeError, match="Both arguments must be numbers"):
            multiply(5, "3")
    
    def test_divide_input_validation(self):
        """Test divide rejects non-numeric inputs."""
        with pytest.raises(TypeError, match="Division requires numeric inputs"):
            divide("10", 2)

# TODO: Students will add TestMultiplyDivide class
class TestMultiplyDivide:
    """Test multiplication and division operations"""
    
    def test_multiply_positive_numbers(self):
        """Test multiplying positive numbers"""
        assert multiply(2, 3) == 6
        assert multiply(5, 4) == 20
    
    def test_multiply_with_zero(self):
        """Test multiplying with zero"""
        assert multiply(5, 0) == 0
        assert multiply(0, 10) == 0
    
    def test_multiply_negative_numbers(self):
        """Test multiplying negative numbers"""
        assert multiply(-2, 3) == -6
        assert multiply(-4, -5) == 20
    
    def test_divide_positive_numbers(self):
        """Test dividing positive numbers"""
        assert divide(10, 2) == 5
        assert divide(15, 3) == 5
    
    def test_divide_with_decimals(self):
        """Test division resulting in decimals"""
        assert divide(7, 2) == 3.5
        assert divide(5, 4) == 1.25
    
    def test_divide_by_zero(self):
        """Test that dividing by zero raises an error"""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(10, 0)