board = list(range(1, 10))

win_cond = [(1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7)]

def draw_board():
    print("-------------")
    for i in range(3):
        print('|', board[0 + i*3], '|', board[1 + i*3], '|', board[2 + i*3], '|')
    print('-------------')

def take_input(simvol):
    while True:
        value = input('Куда поставить: '+simvol + ' ? ')
        if not (value in '123456789'):
            print("Неверный ввод. Повторите попытку. ")
            continue
        value = int(value)
        if str(board[value - 1]) in 'XO':
            print("Клетка уже занята")
            continue
        board[value - 1] = simvol
        break

def check_win():
    for i in win_cond:
        if (board[i[0]-1]) == (board[i[1]-1]) == (board[i[2]-1]):
            return board[i[1]-1]
    else:
         return False

def main():
    nomer_xoda = 0
    while True:
        draw_board()
        if nomer_xoda % 2 == 0:
            take_input('X')
        else:
            take_input('O')
        if nomer_xoda > 3:
            winner = check_win()
            if winner:
                draw_board()
                print(winner, "Победитель!")
                break
        nomer_xoda += 1
        if nomer_xoda > 8:
            draw_board()
            print("Ничья!")
            break
main()





