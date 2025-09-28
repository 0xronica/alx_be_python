def perform_operation(num1, num2, operation):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "DIVIDE_BY_ZERO"   # recognisable flag for main.py
        return num1 / num2
    else:
        return "INVALID_OPERATION"   # for safety in case of invalid input
