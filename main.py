import random 
import string
import pyperclip
import argparse

def generate_password(length=12, use_digits=True, use_letters=True, use_special=True):
    """Генерирует случайныке пароли с задаными параметрами"""

    charcters = ''
    if use_digits:
        charcters += string.digits
    if use_letters:
        charcters += string.ascii_letters
    if use_special:
        charcters += string.punctuation

    if not charcters:
        raise ValueError("Не указаны параметры для генерации пароля")

    password = ''.join(random.choice(charcters) for _ in range(length))
    return password

def main():
    parser = argparse.ArgumentParser(description='Генератор паролей')
    parser.add_argument('-l', '--length', type=int, default=12, help='Длина пароля')
    parser.add_argument('-d', '--no-digits', action='store_false',dest='digits', help='Исключит цифры в пароль')
    parser.add_argument('-a', '--no-letters', action='store_false', dest='letters', help='Исключит буквы в пароль')
    parser.add_argument('-s', '--no-special', action='store_false', dest='special', help='Исключит спецсимволы в пароль')
    parser.add_argument('-c', '--copy', action='store_true', help='Копировать пароль в буфер обмена')

    args = parser.parse_args()

    try:
        password = generate_password(length=args.length, use_digits=args.digits, use_letters=args.letters, use_special=args.special)
        print(f'Пароль: {password}')
        if args.copy:
            try:
                pyperclip.copy(password)
                print('Пароль скопирован в буфер обмена')
            except Exception as e:
                print(f'Не удалось скопировать пароль в буфер обмена {e}')
    except ValueError as e:
        print(f"Ошибка: {e}")

if __name__ == '__main__':
    main()