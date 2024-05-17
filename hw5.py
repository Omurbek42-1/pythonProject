import random
from decouple import config

# Загрузка начального капитала из файла settings.ini
STARTING_MONEY = int(config('MY_MONEY'))

# Список чисел от 1 до 10
slots = list(range(1, 11))

# Функция для совершения ставки
def make_bet(money):
    bet_slot = int(input("Выберите число от 1 до 10, на которое сделаете ставку: "))
    bet_amount = int(input("Введите сумму ставки: "))
    if bet_amount > money:
        print("У вас недостаточно средств для такой ставки!")
        return make_bet(money)
    return bet_slot, bet_amount

# Функция для определения выигрыша
def determine_win(bet_slot, bet_amount):
    winning_slot = random.choice(slots)
    if bet_slot == winning_slot:
        return bet_amount * 2
    else:
        return -bet_amount

# Основная игровая логика
def play_game():
    money = STARTING_MONEY
    while True:
        print(f"Ваши текущие средства: {money}$")
        bet_slot, bet_amount = make_bet(money)
        money_change = determine_win(bet_slot, bet_amount)
        money += money_change
        print(f"Выпавшее число: {winning_slot}")
        if money <= 0:
            print("У вас закончились деньги. Игра окончена.")
            break
        else:
            play_again = input("Хотите сыграть еще? (yes/no): ")
            if play_again.lower() != "yes":
                print(f"Итоговый результат игры: {money}$")
                break

if _name_ == "_main_":
    play_game()