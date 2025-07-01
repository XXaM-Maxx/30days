def basic():
    FirstNumber = int(input("Введите ваше первое число: "))
    TwiceNumber = int(input("Введите ваше второе число: "))
    operation = input("Введите операцию: ")
    if operation == "+":
        if TwiceNumber < 0:
            print(f"({FirstNumber}) + {TwiceNumber} = {FirstNumber + TwiceNumber}")
        else:
            print(f"{FirstNumber} + {TwiceNumber} = {FirstNumber + TwiceNumber}")
    elif operation == "-":
        if TwiceNumber < 0:
            print(f"{FirstNumber} - ({TwiceNumber}) = {FirstNumber - TwiceNumber}")
        else:
            print(f"{TwiceNumber} - {FirstNumber} = {TwiceNumber - FirstNumber}")
    elif operation == "*":
        if TwiceNumber < 0:
            print(f"{FirstNumber} * ({TwiceNumber}) = {FirstNumber * TwiceNumber}")
        else:
            print(f"{TwiceNumber} * {FirstNumber} = {TwiceNumber * FirstNumber}")
    elif operation == "/":
        if TwiceNumber == 0:
            print("Деление на ноль запрещено")
        else:
            print(f"{TwiceNumber} / {FirstNumber} = {TwiceNumber / FirstNumber}")
    else:
        print("Неверная операция")

def main():
    while True:
        if input("Введите 'basic' для запуска программы или 'exit' для выхода: ") == "basic":
            basic()
        else:
            break

if __name__ == '__main__':
    main()
