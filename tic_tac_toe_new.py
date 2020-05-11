# Spielersymbol bestimmen
player1 = 'x'
player2 = 'o'

field = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
turn = 0
isWinner = False
playerturn = 1

# Spieldfeld zeichnen
def drawField(field):
    print('----------' + '\n' + '|' + field[0] + ' |' + field[1] + ' | ' + field[2] + '|' + '\n' + '----------')
    print('|' + field[3] + ' |' + field[4] + ' | ' + field[5] + '|' + '\n' + '----------')
    print('|' + field[6] + ' |' + field[7] + ' | ' + field[8] + '|' + '\n' + '----------')

# Regeln bestimmen
def winGame(field):
    #Horizontal
    if field[0] == field[1] and field[1] == field[2] and field[0] != ' ':
        print(f'You won + field[0]!')
        return True
    elif field[3] == field[4] and field[4] == field[5] and field[3] != ' ':
        print(f'You won + field[3]!')
        return True
    elif field[6] == field[7] and field[7] == field[8] and field[6] != ' ':
        print(f'You won + field[6]!')
        return True

    #Vertikal
    if field[0] == field[3] and field[6] == field[2] and field[0] != ' ':
        print(f'You won + field[0]!')
        return True
    elif field[1] == field[4] and field[7] == field[5] and field[1] != ' ':
        print(f'You won + field[1]!')
        return True
    elif field[2] == field[5] and field[5] == field[8] and field[2] != ' ':
        print(f'You won + field[2]!')
        return True

    #Diagonal
    if field[0] == field[4] and field[4] == field[8] and field[0] != ' ':
        print(f'You won + field[0]!')
        return True
    elif field[2] == field[4] and field[4] == field[6] and field[2] != ' ':
        print(f'You won + field[2]!')
        return True

    #Gleichstand
    if turn == 9:
        print(f'It''s a draw!')
        return True

    return False

#Die belegten Felder als solche markieren
def occupiedFields(choice, occupied):
    if choice == 1:
        field[0] = occupied
    if choice == 2:
       field[1] = occupied
    if choice == 3:
        field[2] = occupied
    if choice == 4:
        field[3] = occupied
    if choice == 5:
        field[4] = occupied
    if choice == 6:
        field[5] = occupied
    if choice == 7:
        field[6] = occupied
    if choice == 8:
        field[7] = occupied
    if choice == 9:
        field[8] = occupied


#Die nicht belegten Felder kennzeichnen
def checkfreeFields(field):
    freeField = ' '
    if field[0] == ' ':
        freeField = freeField + ' 1,'
    if field[1] == ' ':
        freeField = freeField + ' 2'
    if field[2] == ' ':
        freeField = freeField + ' 3'
    if field[3] == ' ':
        freeField = freeField + ' 4'
    if field[4] == ' ':
        freeField = freeField + ' 5'
    if field[5] == ' ':
        freeField = freeField + ' 6'
    if field[6] == ' ':
        freeField = freeField + ' 7'
    if field[7] == ' ':
        freeField = freeField + ' 8'
    if field[8] == ' ':
        freeField = freeField + ' 9'
    return freeField

#Spielbeginn
print(f'Let us play tic tac toe! Pick a field of your choice and write its number when it is your turn!')
fieldnumbers = ['1', '2', '3','4', '5', '6', '7', '8', '9']
drawField(fieldnumbers)

while not isWinner:
    if playerturn == 1:
        drawField(field)
        freeField = checkfreeFields(field)
        choice = int(input(f'Player X, it''s your turn. Choose between the following options:' + freeField + ' '))
        occupiedFields(choice, player1)

    if playerturn == 2:
        drawField(field)
        freeField = checkfreeFields(field)
        choice = int(input(f'Player O, it''s your turn. Choose between the following options:' + freeField + ' '))
        occupiedFields(choice, player2)

    #Spielerwechsel
    if playerturn == 1:
        playerturn = 2
    else:
        playerturn = 1

    turn = turn + 1

    #Prüfen, ob einer der Spieler gewinnt
    isWinner = winGame(field)

drawField(field)
