


def derivative(f, x, h=1e-7):
    """Calculate derivative using central difference method"""
    try:
        return (f(x + h) - f(x - h)) / (2 * h)
    except ZeroDivisionError:
        return float('inf')

def square(x):
    """Calculate x²"""
    return x * x

def constant(x):
    return x



# Test points
x_values = [0, 1, 2, 3]
h = 0.0001

for x in x_values:
    numerical_deriv = round(derivative(constant, x, h))
    print(f"x={x}:")
    print(f"  Numerical derivative: {numerical_deriv}")
    

 