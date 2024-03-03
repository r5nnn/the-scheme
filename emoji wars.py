import time


class Emoji:
    def __init__(self, name, emoji, hp, df, atk, charge=None):
        """
        :param name: tag of emoji
        :param emoji: literal emoji
        :param hp: health value of emoji
        :param df: defence value of emoji
        :param atk: attack value of emoji
        """
        self.atk = atk
        self.df = df
        self.hp = hp
        self.emoji = emoji
        self.name = name
        self.alive = True
        self.charge = charge if charge is not None else atk

    def dead(self):
        """
        :method dead: handles death of emoji
        """
        self.emoji = '💀'
        self.hp = 0
        self.alive = False


class Happy(Emoji):
    def attack(self, enemy):
        """
        :method attack: specific attacks for emojis of child class happy
        :param enemy: emoji which is being attacked
        """
        match self.name:
            case "bigsmile":
                print('{you} smiles at {enemy}'.format(you=self.emoji, enemy=enemy.emoji))
                print('{enemy}\'s attack increases by 2'.format(enemy=enemy.emoji))
                print('{emoji} [HP: {hp} ATK: {atk} + {buff}]'.format(emoji=enemy.emoji, hp=enemy.hp,
                                                                      atk=enemy.atk, buff=2))
                print('——————————————————————————————————————————————————————————————')
                enemy.atk += 2
            case "grin":
                evil = self.charge
                if self.hp < 100:
                    self.charge += 1
                if evil == 0:
                    print('{you} grinned at {enemy}'.format(you=self.emoji, enemy=enemy.emoji))
                    print('{emoji} [HP: {hp}]'.format(emoji=enemy.emoji, hp=enemy.hp))
                    print('——————————————————————————————————————————————————————————————')
                elif 2 > evil > 0:
                    print('{you} grinned maliciously at {enemy}'.format(you=self.emoji, enemy=enemy.emoji))
                    print('{emoji} [HP: {hp}]'.format(emoji=enemy.emoji, hp=enemy.hp))
                    print('——————————————————————————————————————————————————————————————')
                else:
                    print('{you} grins.. and suddenly attacks {enemy}!'.format(you=self.emoji, enemy=enemy.emoji))
                    print('{emoji} [HP: {hp} - {atk}]'.format(emoji=enemy.emoji, hp=enemy.hp,
                                                              atk=30 / ((enemy.df + 100) / 100)))
                    print('——————————————————————————————————————————————————————————————')
                    enemy.hp -= 30 / ((enemy.df + 100) / 100)
            case 'lol':
                if enemy.name == 'lmao':
                    print('{you} laughs so hard they start crying. But {enemy} was already laughing. '
                          'Nothing happens'.format(enemy=enemy.emoji, you=self.emoji))
                    print('{emoji} [HP: {hp}]'.format(emoji=enemy.emoji, hp=enemy.hp))
                elif enemy.name == 'grin':
                    print('{you} laughs so hard they start crying. {enemy} seems provoked!'.format(
                            enemy=enemy.emoji, you=self.emoji))
                    print('{emoji} [HP: {hp}]'.format(emoji=enemy.emoji, hp=enemy.hp))
                    enemy.charge += 2
                else:
                    print('{you} laughs so hard they start crying. '
                          'Its contagous! {enemy} starts laughing too'.format(enemy=enemy.emoji, you=self.emoji))
                    print('{emoji} [HP: {hp} DEF: {df} - {debuff}]'.format(emoji=enemy.emoji, hp=enemy.hp,
                                                                           df=enemy.df, debuff=2))
                    if enemy.df > 0:
                        enemy.df -= 2
                print('——————————————————————————————————————————————————————————————')
            case 'lmao':
                if enemy.name == 'lol':
                    print('{you} laughs so hard they are literally rolling on the floor.'
                          ' But {enemy} was already laughing. Nothing happens'.format(
                            enemy=enemy.emoji, you=self.emoji))
                    print('——————————————————————————————————————————————————————————————')
                elif enemy.name == 'grin':
                    print('{you} laughs so hard they start crying. {enemy} seems provoked!'.format(
                            enemy=enemy.emoji, you=self.emoji))
                    print('{emoji} [HP: {hp}]'.format(emoji=enemy.emoji, hp=enemy.hp))
                    print('——————————————————————————————————————————————————————————————')
                    enemy.charge += 2
                else:
                    pain = self.charge
                    self.charge += 1
                    if pain == 0:
                        print('{you} laughs so hard they are literally rolling on the floor.'
                              ' Its contagous! {enemy} drops to the floor aswell'.format(enemy=enemy.emoji,
                                                                                         you=self.emoji))
                        print('{emoji} [HP: {hp} DEF: {df} - {debuff}]'.format(emoji=enemy.emoji, hp=enemy.hp,
                                                                               df=enemy.df, debuff=4))
                        print('——————————————————————————————————————————————————————————————')
                        if enemy.df > 0:
                            enemy.df -= 2
                    if pain > 2:
                        print('{you} laughs so hard they are literally rolling on the floor. '
                              'Its actually kind of painful.\n'
                              '{enemy} also aches from the laughter'.format(enemy=enemy.emoji, you=self.emoji))
                        print('{emoji} [HP: {hp} - {enemylaugh} DEF: {df}]'.format(emoji=enemy.emoji, hp=enemy.hp,
                                                                                   df=enemy.df, enemylaugh=7))
                        print('——————————————————————————————————————————————————————————————')
                        print('{emoji} [HP: {hp} - {selflaugh} DEF: {df}]'.format(emoji=self.emoji, hp=self.hp,
                                                                                  df=self.df, selflaugh=7))
                        print('——————————————————————————————————————————————————————————————')
                        enemy.hp -= 7 / ((enemy.df + 100) / 100)
                        self.hp -= 7 / ((self.df + 100) / 100)
            case 'wink':
                print('{you} winks at {enemy}'.format(you=self.emoji, enemy=enemy.emoji))
                print('{enemy} blushes... they don\'t see the next attack coming!')
                print('{emoji} [HP: {hp} - {atk} DEF: {df} - {df}]'.format(emoji=enemy.emoji, hp=enemy.hp,
                                                          df=self.df, atk=enemy.atk))

            case _:
                print(self.emoji + ' attacks ' + enemy.emoji + '!')
                print('{emoji} [HP: {hp} - {atk}]'.format(emoji=enemy.emoji, hp=enemy.hp,
                                                          atk=self.atk / ((enemy.df + 100) / 100)))
                print('——————————————————————————————————————————————————————————————')
                enemy.hp -= self.atk / ((enemy.df + 100) / 100)


def catalogue():
    """
    :function catalogue: prints out all available emojis to choose from
    """
    print('——————————————————————————————————————————————————————————————')
    for i in emojis:
        print('{emoji} Emoji name: {name} [HP: {hp} ATK: {atk} DEF: {df}]'.format(emoji=i.emoji, name=i.name, hp=i.hp,
                                                                                  atk=i.atk, df=i.df))
    input('——————————————————————————————————————————————————————————————')


''''''


# gameloop
def main():
    player1 = input('''——————————————————————————————————————————————————————————————
Player1 picks their emoji (player1 always starts the war):
''')
    player2 = input('''——————————————————————————————————————————————————————————————
Player2 picks their emoji:
''')

    if player1.lower() in emojiNames:
        # assign class variables based on tag given
        player1 = emojis[emojiNames.index(player1)]
    else:
        # else return to main menu allowing for user to view catalogue
        print('''——————————————————————————————————————————————————————————————
Error: invalid player1 emoji tag. For a list emoji tags, input 2 in the main menu
——————————————————————————————————————————————————————————————''')
        time.sleep(1)
        return True
    if player2.lower() in emojiNames:
        player2 = emojis[emojiNames.index(player2)]
    else:
        print('''——————————————————————————————————————————————————————————————
Error: invalid player2 emoji tag. For a list emoji tags, input 2 in the main menu
——————————————————————————————————————————————————————————————''')
        time.sleep(1)
        return True
    # display whos who
    print('——————————————————————————————————————————————————————————————')
    print('Player 2 → ' + player2.emoji)
    print('\n')
    print('Player 1 → ' + player1.emoji)
    print('——————————————————————————————————————————————————————————————')
    time.sleep(1)

    flip = 0
    winner = ''
    # main fight loop
    while True:
        flip += 1
        # display game board
        print('{emoji} [HP: {hp} ATK: {atk} DEF: {df}]'.format(emoji=player2.emoji, hp=player2.hp, atk=player2.atk,
                                                               df=player2.df))
        print('\n')
        print('{emoji} [HP: {hp} ATK: {atk} DEF: {df}]'.format(emoji=player1.emoji, hp=player1.hp, atk=player1.atk,
                                                               df=player1.df))
        input('——————————————————————————————————————————————————————————————')
        # check if players are dead
        if player1.alive is False or player2.alive is False:
            break
        time.sleep(0.75)
        # if player1 is alive attack player2 (happens every 2nd cycle)
        if player1.alive and flip % 2 == 1:
            player1.attack(player2)
            time.sleep(0.75)
        # check if player2 died from that attack
        if player2.hp <= 0:
            winner = 'player1'
            player2.dead()
        # if player2 is alive attack player1 (happens every 2nd cycle)
        if player2.alive and flip % 2 == 0:
            player2.attack(player1)
            time.sleep(0.75)
        # check if player1 died from that attack
        if player1.hp <= 0:
            winner = 'player2'
            player1.dead()
    time.sleep(0.75)
    # display outcome
    print(winner + ' has won the round')
    print('press enter to restart')
    input('——————————————————————————————————————————————————————————————')


# class variables of all emojis
bigSmile = Happy('bigsmile', '😀', 100.0, 0, 0)
grin = Happy('grin', '😁', 100.0, 0, 0, 0)
lol = Happy('lol', '😂', 70.0, 0, 0)
lmao = Happy('lmao', '🤣', 50.0, 0, 0, 0)
ohNo = Happy('ohno', '😅', 100.0, 5, 12)
yeah = Happy('yeah', '😆', 100.0, 10, 10)
wink = Happy('wink', '😉', 90.0, 0, 7)

# lists of emojis and their tags
emojis = [bigSmile, grin, lol, lmao, ohNo, yeah, wink]
emojiNames = ['bigsmile', 'grin', 'lol', 'lmao', 'ohno', 'yeah', 'wink']

STATUS = True

# mainloop
while STATUS:
    menuOption = input('''
                          __.__                   --x to exit--
  ____   _____   ____    |__|__| __  _  _______ _______  ______
_/ __ \\ /     \\ /  _ \\   |  |  | \\ \\/ \\/ /\\___  \\_  __ \\/  ___/
\\  ___/|  Y Y  (  <_> )  |  |  |  \\     /  / __ \\|  | \\/\\___ \\ 
 \\___  >__|_|  /\\____/\\__|  |__|   \\/\\_/  (____  /__|  /____  >
     \\/      \\/      \\______|                  \\/           \\/ 
by r5ne                                                 v0.0.3

            --Enter 1 for Begin, 2 for Catalogue--            
''')
    if menuOption == '1':
        main()
    elif menuOption == '2':
        catalogue()
    elif menuOption.lower() == 'x':
        raise SystemExit()
    else:
        print('Unknown value given.')
        print('Restarting program...')
        time.sleep(1)
