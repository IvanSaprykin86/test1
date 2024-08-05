class throw_Exception(Exception):
    pass

def main (a):
    numbers = []
    number = 0

    for i in a.split():
        if i.isdigit():
            numbers.append(int(i))
        elif i == '+' or i == '-' or i == '*' or i == '/':
            numbers.append(i) 

    if len(numbers) > 3:
        raise throw_Exception('т.к. формат математической операции не удовлетворяет заданию - два операнда и один оператор (+, -, /, *')
    elif len(numbers) < 3:
        raise throw_Exception ('т.к. строка не является математической операцией')
    elif numbers[0] > 10:
        raise throw_Exception('Калькулятор должен принимать на вход числа от 1 до 10 включительно, не более  или Арабские числа отрицательные и ноль.')
    elif numbers[2] > 10:
        raise throw_Exception('Калькулятор должен принимать на вход числа от 1 до 10 включительно, не более  или Арабские числа отрицательные и ноль.')

    if numbers[1] == '+':
        number = numbers[0] + numbers[2]
    elif numbers[1] == '-':
        number = numbers[0] - numbers[2]
    elif numbers[1] == '*':
        number = numbers[0] * numbers[2]
    else:
        number = numbers[0] / numbers[2]

    
    print(int(number))

main(input())