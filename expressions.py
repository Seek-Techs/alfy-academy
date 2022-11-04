import math

def calc_math_expression(num1, num2, operator):
    # num1 = float(input('enter a number'))
    # num2 = float(input('enter a number'))
    # operator = input('enter the operator')
    if operator == '+':
        return(num1 + num2)
        
    elif operator == '-':
        return(num1 - num2)

    elif operator == '*':
        return(num1 * num2)

    elif operator == ':':
        try:
            return(num1 / num2)
        except ZeroDivisionError:
            return None

    else:
        return None
 
def calc_math_expression_from_str(str_input):
    split = str_input.split()
    num1 = float(split[0])
    num2 = float(split[2])
    operator = split[1]
    return calc_math_expression(num1, num2, operator)
    
def find_largest_and_smallest_numbers(num1=0.0, num2=0.0, num3=0.0):
    number = []
    number.append(num1)
    number.append(num2)
    number.append(num3)
    number.sort()
    return (number[2], number[0])

def quadratic_equation_solver(a, b, c):
    d = b**2 - 4 * a * c
    try: 
        x1 = (-b + math.sqrt(d))/(2 * a) 
        x2 = (-b - math.sqrt(d))/(2 * a)
        if x1 != x2:
            return (x1, x2)
        else:
            return (x1, None)
    except ValueError: 
        return (None, None)

def quadratic_equation_solver_from_user_input():
    user_input = input('Enter number for "a b c": ')
    content_split_list = user_input.split('')
    a = float(content_split_list[0])
    b = float(content_split_list[1])
    c = float(content_split_list[2])

    return quadratic_equation_solver(a, b, c)

def temp_checker(min_temp, temp_1, temp_2, temp_3):
    if temp_1 > min_temp or temp_2 > min_temp or temp_3 > min_temp:
        return True

    else:
        return False

# calc_math_expression(5, 6, '+')
# calc_math_expression_from_str('10 : 5')

# print(find_largest_and_smallest_numbers(num1=9.5, num2=6, num3=7))