from random import randint, choice

def create_question():
    operations = ["+", "-", "*", "/"]
    number1 = randint(1, 10)
    number2 = randint(1, 10)
    selected_operation = choice(operations)

    return number1, number2, selected_operation

def get_answer(number1, number2, selected_operation):
    answer = float(input(f"What is {number1} {selected_operation} {number2}? "))
    return answer

def check_answer(number1, number2, selected_operation, answer):
    correct_answer = 0
    if selected_operation == "+":
        correct_answer = number1 + number2
    elif selected_operation == "-":
        correct_answer = number1 - number2
    elif selected_operation == "*":
        correct_answer = number1 * number2
    elif selected_operation == "/":
        correct_answer = number1 / number2

    if answer == correct_answer:
        print("Correct!")
        return 1
    else:
        print("Wrong answer.")
    return -1

def game():
    player1 = input("Enter the name of player 1: ")
    player2 = input("Enter the name of player 2: ")
    total_score_player1 = 0
    total_score_player2 = 0
    for i in range(5):
        print("------------- NEW ROUND ---------------")
        print(f"{player1}'s turn:")
        number1, number2, selected_operation = create_question()
        answer1 = get_answer(number1, number2, selected_operation)
        score_player1 = check_answer(number1, number2, selected_operation, answer1)
        total_score_player1 += score_player1

        print(f"{player2}'s turn:")
        number1, number2, selected_operation = create_question()
        answer2 = get_answer(number1, number2, selected_operation)
        score_player2 = check_answer(number1, number2, selected_operation, answer2)
        total_score_player2 += score_player2

    print(f"{player1}'s score: {total_score_player1}")
    print(f"{player2}'s score: {total_score_player2}")
    if total_score_player1 > total_score_player2:
        print(f"{player1} WINS! {player2} LOSES.")
    elif total_score_player2 > total_score_player1:
        print(f"{player2} WINS! {player1} LOSES.")
    else:
        print("GAME OVER. IT'S A DRAW.")
    return 0

game()
