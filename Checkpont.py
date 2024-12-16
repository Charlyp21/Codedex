import random as rd

choices = ['✊','✋','✌️','🦎','🖖']
phrases = ['Scissors cut Paper.',
        'Paper covers Rock.',
        'Rock crushes Lizard.',
        'Lizard poisons Spock.',
        'Spock smashes Scissors.',
        'Scissors beat Lizard.',
        'Lizard eats Paper.',
        'Paper disproves Spock.',
        'Spock vaporizes Rock.',
        'Rock breaks Scissors.']

play = True
computer = 0

while play:
        player = int(input(
        """
================================
Rock Paper Scissors Lizard Spock
================================
1) ✊
2) ✋
3) ✌️
4) 🦎
5) 🖖

Pick a number: 
        """
        ))
        computer = rd.randint(1, 5)
        print('\n')
        print(f'You Chose: {choices[player-1]}')
        print(f'CPU Chose: {choices[computer-1]}')

        if computer == player:
                print('It\'s a Tie!')
        elif player == 1 and (computer == 3 or computer == 4):
                if computer == 3:
                        print(phrases[9])
                elif computer == 4:
                        print(phrases[23])
                print('You Win!')
        elif player == 2 and (computer == 1 or computer == 5):
                if computer == 1:
                        print(phrases[1])
                elif computer == 5:
                        print(phrases[7])
                print('You Win!')
        elif player == 3 and (computer == 2 or computer == 4):
                if computer == 2:
                        print(phrases[0])
                elif computer == 4:
                        print(phrases[5])
                print('You Win!')
        elif player == 4 and (computer == 2 or computer == 5):
                if computer == 2:
                        print(phrases[6])
                elif computer == 5:
                        print(phrases[3])
                print('You Win!')
        elif player == 5 and (computer == 3 or computer == 1):
                if computer == 3:
                        print(phrases[4])
                elif computer == 1:
                        print(phrases[8])
                print('You Win!')
        elif computer == 1 and (player == 3 or player == 4):
                if player == 3:
                        print(phrases[9])
                elif player == 4:
                        print(phrases[2])
                print('CPU Win!')
        elif computer == 2 and (player == 1 or player == 5):
                if player == 1:
                        print(phrases[1])
                elif player == 5:
                        print(phrases[7])
                print('CPU Win!')
        elif computer == 3 and (player == 2 or player == 4):
                if player == 2:
                        print(phrases[0])
                elif player == 4:
                        print(phrases[5])
                print('CPU Win!')
        elif computer == 4 and (player == 2 or player == 5):
                if player == 2:
                        print(phrases[6])
                elif player == 5:
                        print(phrases[3])
                print('CPU Win!')
        elif computer == 5 and (player == 3 or player == 1):
                if player == 3:
                        print(phrases[4])
                elif player == 1:
                        print(phrases[8])
                print('CPU Win!')
        else: 
                print('Invalid number')
        
        x = int(input(
                """
Play again?
1) Yes
2) No
                """
        ))
        
        if x == 2:
                play = False