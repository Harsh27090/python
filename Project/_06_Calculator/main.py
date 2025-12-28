"""
calculator that saves history
"""
from pathlib import Path
def get_history():
    path = Path('history.txt')
    with open(path) as f:
        content = f.read()

    if not path.exists():
        print('File does not exist')
        return
    if content == '':
        print('No history found!')
        return
    print(f'History:\n{content}')
    return

def clear_history():
    path = Path('history.txt')
    with open(path, 'w') as f:
        print('History cleared!')
    return

def save_history(equation, result):
    path = Path('history.txt')
    with open(path, 'a+') as f:
        f.write(f'{equation} = {result}\n')
    return

def calculate(equation):
    parts = equation.split()
    if len(parts) != 3:
        print('Invalid input! Please use format: no. operator no.')
        return

    num1 = float(parts[0])
    op = parts[1]
    num2 = float(parts[2])
    result1 = 0
    if op == '+':
        result1 = num1 + num2
        return result1

    elif op == '-':
        result1 = num1 - num2
        return result1

    elif op == '*':
        result1 = num1 * num2
        return result1

    elif op == '/':
        if num2 == 0.0:
            print('Cannot divide by zero!')
            return
        result1 = num1 / num2
        return result1
    return result1

while True:
    equation = input("Enter equation or command (history, clear, exit): ")

    if equation.lower() == 'exit':
        print('Goodbye!')
        break

    elif equation.lower() == 'history':
        get_history()

    elif equation.lower() == 'clear':
        clear_history()

    else:
        result = calculate(equation)
        print(f'{equation} = {result}')
        if result is not None:
            save_history(equation, result)
