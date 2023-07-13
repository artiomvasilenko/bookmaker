from random import randint

order_a = int(input('Напиши счет команды А: '))
order_b = int(input('Напиши счет команды Б: '))
order = int(input('Напиши свою ставку: '))

currient_a = randint(0, 5)
currient_b = randint(0, 5)

print(f'Команды сыграли со счётом {currient_a}:{currient_b}')

if order_a == currient_a and order_b == currient_b:
    print(f'Твой выигрыш х2: {order * 2} рублей.')

def check_who_win(a, b):
    if a == b:
        return 'both'
    elif a > b:
      return 'a'
    else:
        return 'b'

if check_who_win(order_a, order_b) == check_who_win(currient_a, currient_b):
    print(f'Твой выигрыш х1,5: {int(order * 1.5)} рублей.')

else:
    print(f'Ты проиграл')



    