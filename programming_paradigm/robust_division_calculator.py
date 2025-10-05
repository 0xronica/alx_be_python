def safe_divide(numerator, denominator):
    """Safely divide two values with error handling for non-numeric input and division by zero."""
    try:
        # Convert inputs to float
        num = float(numerator)
        den = float(denominator)

        result = num / den
        return f"The result of the division is {result}"
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    except ValueError:
        return "Error: Please enter numeric values only."
