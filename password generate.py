import random
import string

letters = string.ascii_letters
numbers = string.digits
letters_and_numbers = letters + numbers
num = int(input("Введите длину пароля от 1 до 20: "))
print("Пароль будет с цифрами и буквами или только с цифрами или только с буквами?")
num2 = input("Введите 'Y' если только с буквами""\n""Введите 'U' если только с цифрами""\n""Введите 'Z' если с буквами и цифрами""\n""Введите букву: ")
if 20 >= num:
    if num2 == "Y" or num2 == "y":
        password = ''.join(random.choice(letters) for num1 in range(num))
        print(password)
    else:
        if num2 == "U" or num2 == "u":
            password = ''.join(random.choice(numbers) for num1 in range(num))
            print(password)
        else:
            if num2 == "Z" or num2 == "z":
                password = ''.join(random.choice(letters_and_numbers) for num1 in range(num))
                print(password)
            else:
                print("Введена не правильная буква")
else:
    print("Вы ввели не правильное число, попробуйте заного")

    
