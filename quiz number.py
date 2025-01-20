def bis_balid():# checking an introduced boundary
    while True:
        num = input('Введите правую границу для случайного выбора числа (граница должна быть целым числом > 1):')
        if num.isdigit() and int(num) > 1:
            return int(num)
        else:
            continue
def is_valid(num):
    return num.isdigit() and int(num) in range (1,rb)# checking a correct user introduced number
def guess_num(f):    
    from random import randint
    print(f'Вам нужно будет угадать число, загаданное компьютером от 1 до {f}')
    guessed_num = randint(1,f)
    counter = 0
    while True:
        users_num = input('Enter the guessed number:')
        if is_valid(users_num):
            if int(users_num) > guessed_num:
                print('Вы ввели число больше загаданного, попробуйте еще разок')
                counter += 1
            elif int(users_num) < guessed_num:
                print('Вы ввели число меньше загаданного, попробуйте еще разок')
                counter += 1
            else:
                break
        else:
            print(f'Введите число от 1 до {f}, которое \
                по Вашему мнению загадал компьютер')
    print('Вы угадали, поздравляем!', \
        f'Число ваших попыток: {counter}', sep = '\n')
#начало основной программы
print('Добрый день!Хотите сыграть в числовую угадайку?')
n = input('Хотите сыграть в числовую угадайку? (введите да или нет):')
if n.lower() in ('yes', 'y', 'да', 'lf'):
    rb = bis_balid()
    guess_num(rb)
    m = input('Хотите еще сыграть в числовую угадайку? (введите да или нет):')
    if m.lower() in ('yes', 'y', 'да', 'lf'):
        print('Давайте сыграем еще')
        rb = bis_balid()
        guess_num(rb)
    else:
        print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
else:
    print('Жаль, Еще увидимся...')
