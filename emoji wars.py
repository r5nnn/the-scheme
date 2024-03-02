import time

class Emoji:
    def __init__(self, name, emoji, hp, df, atk):
        self.atk = atk
        self.df = df
        self.hp = hp
        self.emoji = emoji
        self.name = name
        self.alive = True
    def attack(self, enemy):
        enemy.hp -= self.atk/((enemy.df+100)/100)

    def dead(self):
        self.emoji = '💀'
        self.hp = 0
        self.alive = False

def main(emojis):
    player1 = input('''——————————————————————————————————————————————————————————————
Player1 picks their emoji:
''')
    player2 = input('''——————————————————————————————————————————————————————————————
Player2 picks their emoji:
''')
    while True:
        try:
            player1 = int(player1)
            player2 = int(player2)
        except ValueError:
            for i in emojis:
                if player1 == i.name:
                    player1 = i
                elif player2 == i.name:
                    player2 = i
        except:
            break
    print('——————————————————————————————————————————————————————————————')
    print('Player 2 → ' + player2.emoji)
    print('\n')
    print('Player 1 → ' + player1.emoji)
    print('——————————————————————————————————————————————————————————————')
    time.sleep(1)

    flip = 0
    winner = ''
    while True:
        flip += 1
        print('{emoji} [HP: {hp} ATK: {atk} DEF: {df}]'.format(emoji=player2.emoji, hp=player2.hp, atk=player2.atk, df=player2.df))
        print('\n')
        print('{emoji} [HP: {hp} ATK: {atk} DEF: {df}]'.format(emoji=player1.emoji, hp=player1.hp, atk=player1.atk, df=player1.df))
        print('——————————————————————————————————————————————————————————————')
        if player1.alive is False or player2.alive is False:
            break
        time.sleep(0.75)
        if player1.alive and flip % 2 == 1:
            print(player1.emoji + ' attacks ' + player2.emoji + '!')
            print('{emoji} [HP: {hp} - {atk}]'.format(emoji=player2.emoji, hp=player2.hp, atk=player1.atk/((player2.df+100)/100)))
            print('——————————————————————————————————————————————————————————————')
            player1.attack(player2)
            time.sleep(0.75)
        if player2.hp <= 0:
            winner = 'player1'
            player2.dead()
        if player2.alive and flip % 2 == 0:
            print(player2.emoji + ' attacks ' + player1.emoji + '!')
            print('{emoji} [HP: {hp} - {atk}]'.format(emoji=player1.emoji, hp=player1.hp, atk=player2.atk/((player1.df+100)/100)))
            print('——————————————————————————————————————————————————————————————')
            player2.attack(player1)
            time.sleep(0.75)
        if player1.hp <= 0:
            winner = 'player2'
            player1.dead()
    time.sleep(0.75)
    print(winner + ' has won the round')
    print('press enter to restart')
    input('——————————————————————————————————————————————————————————————')

def catalogue(emojis):
    print('——————————————————————————————————————————————————————————————')
    for i in emojis:
        print('{emoji} Emoji name: {name} [HP: {hp} ATK: {atk} DEF: {df}]'.format(emoji=i.emoji, name=i.name, hp=i.hp, atk=i.atk, df=i.df))
    input('——————————————————————————————————————————————————————————————')

happy = Emoji('happy', '😀', 100, 0, 10)
grin = Emoji('grin', '😁', 100, 0, 15)

emojis = [happy, grin]

STATUS = True

while STATUS:
    menuOption = input('''
                          __.__                                
  ____   _____   ____    |__|__| __  _  _______ _______  ______
_/ __ \ /     \ /  _ \   |  |  | \ \/ \/ /\__  \\_  __ \/  ___/
\  ___/|  Y Y  (  <_> )  |  |  |  \     /  / __ \|  | \/\___ \ 
 \___  >__|_|  /\____/\__|  |__|   \/\_/  (____  /__|  /____  >
     \/      \/      \______|                  \/           \/ 
by r5ne                                                 v0.0.1

            --Enter 1 for Begin, 2 for Catalogue--            
''')
    if menuOption == '1':
        main(emojis)
    elif menuOption == '2':
        catalogue(emojis)
    else:
        print('Unknown value given.')
        print('Restarting program...')
        time.sleep(1)
