import random
import cowsay

def rock_paper_scissors(player_choice):
    choices = ['камінь', 'ножиці', 'папір']
    computer_choice = random.choice(choices)

    print(f"Твій вибір: {player_choice}")
    print(f"Вибір комп'ютера: {computer_choice}")

    if player_choice == computer_choice:
        return "Нічия!"
    elif (player_choice == 'камінь' and computer_choice == 'ножиці') or \
         (player_choice == 'ножиці' and computer_choice == 'папір') or \
         (player_choice == 'папір' and computer_choice == 'камінь'):
        return "Ти виграв(ла)!"
    else:
        return "Ти програв(ла)!"

# Виклик функції
player_choice = input("Обери: камінь, ножиці, або папір: ").lower()
result = rock_paper_scissors(player_choice)
print(result)
