"""
utility.py - Basic arithmetic utility module.
"""

def sum_values(a: float, b: float, c: float) -> float:
    """
    Calculates and returns the sum of three numeric values.
    
    Args:
        a (float): First number.
        b (float): Second number.
        c (float): Third number.
        
    Returns:
        float: Sum of a, b, and c.
    """
    return a + b + c


if __name__ == "__main__":
    # Example usage
    num1 = 10
    num2 = 20
    num3 = 30

    result = sum_values(num1, num2, num3)
    print(f"The sum of {num1}, {num2}, and {num3} is: {result}")
