import os
import random
from colorama import init, Fore, Style  # Импортируем необходимые модули
init(autoreset=True)  # Инициализируем Colorama для автоматического сброса стилей


# Фразы приветствия и реакции на разные события
os.system('cls')  # Очищаем экран
f_0 = ["Приветствую на поле боя!","Добро пожаловать в игру!","Приветствую, соперник!","Готовься к сражению!","Приготовься к битве!"]
f_1 = ["Кто ты воин?","Готов ли ты к битве?","Ты готов принять вызов?","Время показать свои навыки!","Пусть бой начнется!","Подними свое оружие и покажи свою силу!"]
f_2 = ["Время приключений! Игра начинается, герой!","Погнали, дружище! Время вступить в бой!","Собирай оружие, дерзай! Начинаем игру!","Пришло время испытать свою судьбу, давай начнем!","Отважный воин, готов ли ты к вызову? Игра начинается!"]
f_lose = ["Как жаль, что ты выиграл. Но буду готов к реваншу.", "Эх, проиграл опять. Ты и так сильный, а я... Ну ладно.", "Поражение ... Уверен, это была удача, не более.", "Моё самолюбие немного поцарапано, но я смирюсь с поражением.", "Неплохо сыграл, но в следующий раз я буду готов к твоим хитростям."]
f_win = ["Хорошая попытка, но в этот раз моя удача была сильнее.","Спасибо за игру! Ты дал мне достойный бой.","Не расстраивайся, это была просто игра. В следующий раз повезет тебе (но это не точно).","Поражение - это часть игры. Не везет всегда, но продолжай стараться.","Отличная попытка! Уверен, в следующий раз тебе повезет больше (но это не точно)."]
f_wrong_input = ["Неверный формат ответа.","Формат неправильный.","Ошибка ввода.","Пожалуйста, введите корректный формат.","Неправильный ввод."]


# Получаем имя соперника
print(Fore.BLUE + random.choice(f_0))   # Выводим случайную приветственную фразу
opponent_name = input('\nНапиши свое имя ... ')  # Просим ввести имя соперника
print()
print(Fore.BLUE + random.choice(f_1) + '\n... хотя уже ничего не играет роли 😈(buhaha)') # Выводим случайную фразу после ввода имени


# Информация об игре
steps = 0  # Шаги
battle_count = 1  # Количество битв
my_score = 0  # Мой счет
opponent_score = 0  # Счет соперника
last_winner = 0  # Последний победитель (0 - никто, 1 - я, 2 - соперник)
ships = []  # Список кораблей
placement_strategy = 1  # Стратегия размещения кораблей
position = [0, 1]  # 0 - горизонтальное, 1 - вертикальное размещение
side = ['right', 'left']  # Стороны
front = ['right', 'left']  # Направления
right_front = ['422', '224']  # Форматы размещения справа
left_front = ['332', '233', '323']  # Форматы размещения слева


clean_board_coords = {(1,1):0,(1,2):0,(1,3):0,(1,4):0,(1,5):0,(1,6):0,(1,7):0,(1,8):0,(1,9):0,(1,10):0,(2,1):0,(2,2):0,(2,3):0,(2,4):0,(2,5):0,(2,6):0,(2,7):0,(2,8):0,(2,9):0,(2,10):0,(3,1):0,(3,2):0,(3,3):0,(3,4):0,(3,5):0,(3,6):0,(3,7):0,(3,8):0,(3,9):0,(3,10):0,(4,1):0,(4,2):0,(4,3):0,(4,4):0,(4,5):0,(4,6):0,(4,7):0,(4,8):0,(4,9):0,(4,10):0,(5,1):0,(5,2):0,(5,3):0,(5,4):0,(5,5):0,(5,6):0,(5,7):0,(5,8):0,(5,9):0,(5,10):0,(6,1):0,(6,2):0,(6,3):0,(6,4):0,(6,5):0,(6,6):0,(6,7):0,(6,8):0,(6,9):0,(6,10):0,(7,1):0,(7,2):0,(7,3):0,(7,4):0,(7,5):0,(7,6):0,(7,7):0,(7,8):0,(7,9):0,(7,10):0,(8,1):0,(8,2):0,(8,3):0,(8,4):0,(8,5):0,(8,6):0,(8,7):0,(8,8):0,(8,9):0,(8,10):0,(9,1):0,(9,2):0,(9,3):0,(9,4):0,(9,5):0,(9,6):0,(9,7):0,(9,8):0,(9,9):0,(9,10):0,(10,1):0,(10,2):0,(10,3):0,(10,4):0,(10,5):0,(10,6):0,(10,7):0,(10,8):0,(10,9):0,(10,10):0}


# Функции для управления состоянием игры и размещения кораблей
def battle_status():
    os.system('cls')
    print('🧱'*30)
    print(f'\t{Fore.YELLOW + Style.BRIGHT}Битва : {battle_count}')
    if last_winner == 0:
        print(f'\t{Fore.YELLOW + Style.BRIGHT}Счет  : \tЯ: {my_score}\t\t{opponent_name}: {opponent_score}')
    elif last_winner == 1:
        print(f'\t{Fore.YELLOW + Style.BRIGHT}Счет  : \tЯ: {my_score} 👑\t\t{opponent_name}: {opponent_score}')
    elif last_winner == 2:
        print(f'\t{Fore.YELLOW + Style.BRIGHT}Счет  : \tЯ: {my_score}\t\t{opponent_name}: {opponent_score} 👑')
    print('🧱'*30)


def find_possible_4ship_positions():
    wave_1 = [(4,1),(8,1),(10,3),(10,7),(1,4),(1,8),(3,10),(7,10)]
    wave_2 = [(2,3),(2,7),(3,2),(7,2),(9,4),(9,8),(8,9),(4,9)]
    wave_3 = [(3,6),(6,3),(8,5),(5,8)]
    wave_4 = [ (4,5),(5,4),(7,6),(6,7)]
    find_possible_4ship_positions = [wave_1,wave_2,wave_3,wave_4]
    possible_positions = []
    for i in find_possible_4ship_positions:
        for j in i:
            if opponent_board[j] == 0:
                possible_positions.append(j)
    return possible_positions


def find_possible_3_2ship_positions():  
    possible_positions_list = [(1,2),(1,4),(1,6),(1,8),(1,10),(2,1),(2,3),(2,5),(2,7),(2,9),(3,2),(3,4),(3,6),(3,8),(3,10),(4,1),(4,3),(4,5),(4,7),(4,9),(5,2),(5,4),(5,6),(5,8),(5,10),(6,1),(6,3),(6,5),(6,7),(6,9),(7,2),(7,4),(7,6),(7,8),(7,10),(8,1),(8,3),(8,5),(8,7),(8,9),(9,2),(9,4),(9,6),(9,8),(9,10),(10,1),(10,3),(10,5),(10,7),(10,9)]
    possible_positions = []
    for i in possible_positions_list:
        if opponent_board[i] == 0:
            possible_positions.append(i)
    return possible_positions


def mark_ship_contour(coordinate,player_board):
    v_left = (coordinate[0]-1,coordinate[-1]-1)
    v_v = (coordinate[0]-1,coordinate[-1])
    v_right = (coordinate[0]-1,coordinate[1]+1)
    left = (coordinate[0],coordinate[-1]-1)
    right = (coordinate[0],coordinate[-1]+1)
    n_left = (coordinate[0]+1,coordinate[-1]-1)
    n_v = (coordinate[0]+1,coordinate[-1])
    n_right = (coordinate[0]+1,coordinate[-1]+1)   
    ship_contour = [v_left,v_v,v_right,left,right,n_left,n_v,n_right]
    for i in ship_contour:
        if i in player_board:
            if player_board[i] == 0:
                player_board[i] = 'x'


def check_circle(coordinate):
    v_left = (coordinate[0]-1,coordinate[-1]-1)
    v_v = (coordinate[0]-1,coordinate[-1])
    v_right = (coordinate[0]-1,coordinate[1]+1)
    left = (coordinate[0],coordinate[-1]-1)
    right = (coordinate[0],coordinate[-1]+1)
    n_left = (coordinate[0]+1,coordinate[-1]-1)
    n_v = (coordinate[0]+1,coordinate[-1])
    n_right = (coordinate[0]+1,coordinate[-1]+1) 
    ship_contour = [v_left,v_v,v_right,left,right,n_left,n_v,n_right]
    for i in ship_contour:
        if i in my_board:
            if my_board[i] == 1:
                return 0
    else:
        return 1
    

def arrange_placement(position_, y, x):
    if position_ == 0:
        return (y,x+1)
    else:
        return (y+1,x)


def ship_4point(position,y,x):
    my_board[(y,x)] = 1
    cord = [(y,x)]
    for i in range(3):
        coordinate = arrange_placement(position, cord[-1][0], cord[-1][-1])
        cord.append(coordinate)
        my_board[coordinate] = 1
    for i in cord:
        mark_ship_contour(i,my_board)
    return cord


def check_ship_4point(position,y,x):
    cord = [(y,x)]
    for i in range(3):
        coordinate = arrange_placement(position, cord[-1][0], cord[-1][-1])
        cord.append(coordinate)
    return cord


def ship_3point(position,y,x):
    my_board[(y,x)] = 1
    cord = [(y,x)]
    for i in range(2):
        coordinate = arrange_placement(position, cord[-1][0], cord[-1][-1])
        cord.append(coordinate)
        my_board[coordinate] = 1
    for i in cord:
        mark_ship_contour(i,my_board)
    return cord


def check_ship_3point(position,y,x):
    cord = [(y,x)]
    for i in range(2):
        coordinate = arrange_placement(position, cord[-1][0], cord[-1][-1])
        cord.append(coordinate)
    if cord[-1][0] <= 10 and cord[-1][-1] <= 10:
        checks_3 = []
        for i in cord:
            check = check_circle(i)
            checks_3.append(check)
        if 0 in checks_3:
            return 0
        else:
            return 1
    else:
        return 0
    

def ship_2point(position,y,x):
    my_board[(y,x)] = 1
    cord = [(y,x)]
    coordinate = arrange_placement(position, cord[-1][0], cord[-1][-1])
    cord.append(coordinate)
    my_board[coordinate] = 1
    for i in cord:
        mark_ship_contour(i,my_board)
    return cord


def check_ship_2point(position,y,x):
    cord = [(y,x)]
    coordinate = arrange_placement(position, cord[-1][0], cord[-1][-1])
    cord.append(coordinate)
    if cord[-1][0] <= 10 and cord[-1][-1] <= 10:
        checks_2 = []
        for i in cord:
            check = check_circle(i)
            checks_2.append(check)
        if 0 in checks_2:
            return 0
        else:
            return 1
    else:
        return 0  


def ship_1point(y,x,player_board):
    my_board[(y,x)] = 1
    mark_ship_contour((y,x),player_board)
    return [(y,x)]


def check_ship_1point(y,x):
    cord = (y,x)
    check = check_circle(cord)
    return check
 

def func_row_right(position, c_1 , right_method):
    row_right = []
    for i in right_method:
        if i == '4':
            if len(row_right) == 0:
                four = ship_4point(position, c_1[0], c_1[-1])
                row_right.append(four)
            else:
                four = ship_4point(position, row_right[-1][-1][0]+2, row_right[-1][-1][-1])
                row_right.append(four)
            ships.append(four)
        elif i == '3':
            if len(row_right) == 0:
                three = ship_3point(position, c_1[0], c_1[-1])
                row_right.append(three)
            else:
                three = ship_3point(position, row_right[-1][-1][0]+2, row_right[-1][-1][-1])
                row_right.append(three)
            ships.append(three)
        elif i == '2':
            if len(row_right) == 0:
                two = ship_2point(position, c_1[0], c_1[-1])
                row_right.append(two)
            else:
                two = ship_2point(position, row_right[-1][-1][0]+2, row_right[-1][-1][-1])
                row_right.append(two)
            ships.append(two)


def func_row_left(position, c_2, left_method):
    row_left = []
    for i in left_method:
        if i == '4':
            if len(row_left) == 0:
                four = ship_4point(position, c_2[0], c_2[-1])
                row_left.append(four)
            else:
                four = ship_4point(position, row_left[-1][-1][0]+2, row_left[-1][-1][-1])
                row_left.append(four)
            ships.append(four)
        elif i == '3':
            if len(row_left) == 0:
                three = ship_3point(position, c_2[0], c_2[-1])
                row_left.append(three)
            else:
                three = ship_3point(position, row_left[-1][-1][0]+2, row_left[-1][-1][-1])
                row_left.append(three)
            ships.append(three)
        elif i == '2':
            if len(row_left) == 0:
                two = ship_2point(position, c_2[0], c_2[-1])
                row_left.append(two)
            else:
                two = ship_2point(position, row_left[-1][-1][0]+2, row_left[-1][-1][-1])
                row_left.append(two)
            ships.append(two)             


def func_front_1_2(position, front_1, c_1,c_2):
    if front_1 == 'right':  
        right_method = random.choice(right_front)
        left_method = random.choice(left_front)
        func_row_right(position, c_1 , right_method)
        func_row_left(position, c_2, left_method)
   
    elif front_1 == 'left':
        right_method = random.choice(left_front)
        left_method = random.choice(right_front)
        func_row_right(position, c_1 , right_method)
        func_row_left(position, c_2, left_method)
  

def func_ship_1point():
    cord_1 = []
    while True:
        if len(cord_1) == 4:
            break
        else:
            keys = list(my_board.keys())
            x = random.choice(keys)
            check = check_circle(x)
            if my_board[x] == 0 and check == 1:
                my_board[x] = 1
                mark_ship_contour(x,my_board)
                cord_1.append(x)
                ships.append([x])


def place_ships(placement_strategy):
    if placement_strategy == 1:
        position = 1
        c_1 = (1,1)
        c_2 = (1,10)
        front_1  =  random.choice(front) 
        func_front_1_2(position, front_1, c_1,c_2)
        func_ship_1point()
        ships.sort(key=len)
    elif placement_strategy == 2:
        position = 1
        koxm = random.choice(side)
        if koxm == 'right':
            c_1 = (1,1)
            c_2 = (1,3)
            front_1  = random.choice(front) 
            func_front_1_2(position, front_1, c_1,c_2)
            func_ship_1point()
        else:
            c_1 = (1,8)
            c_2 = (1,10)
            front_1  = random.choice(front) 
            func_front_1_2(position, front_1, c_1,c_2)
            func_ship_1point()
        ships.sort(key=len)
    elif placement_strategy == 3:
        #ship_4point
        n_4 = 0
        while True:
            if n_4 == 1:
                break
            c_A = random.choice(list(my_board.keys()))
            position =  random.choice(position)
            x = check_ship_4point(position, c_A[0], c_A[-1])
            if x[-1][0] <= 10 and x[-1][-1] <= 10:
                four = ship_4point(position, c_A[0], c_A[-1])
                n_4 += 1
                ships.append(four)
        #ship_3point
        n_3 = 0
        while True:
            if n_3 == 2:
                break
            keys = [x for x in list(my_board.keys()) if my_board[x] == 0]
            c_ship_3point = random.choice(keys)
            position =  random.choice(position)
            x = check_ship_3point(position, c_ship_3point[0], c_ship_3point[-1])
            if x:
                three = ship_3point(position, c_ship_3point[0], c_ship_3point[-1])
                n_3 += 1
                ships.append(three)
        #ship_2point
        n_2 = 0
        while True:
            if n_2 == 3:
                break
            keys = [x for x in list(my_board.keys()) if my_board[x] == 0]
            c_ship_2point = random.choice(keys)
            position =  random.choice(position)
            x = check_ship_2point(position, c_ship_2point[0], c_ship_2point[-1])
            if x:
                two = ship_2point(position, c_ship_2point[0], c_ship_2point[-1])
                n_2 += 1
                ships.append(two)
        #ship_1point
        n_1 = 0
        while True:
            if n_1 == 4:
                break
            keys = [x for x in list(my_board.keys()) if my_board[x] == 0]
            c_ship_1point = random.choice(keys)
            x = check_ship_1point(c_ship_1point[0], c_ship_1point[-1])
            if x:
                mek = ship_1point( c_ship_1point[0], c_ship_1point[-1],my_board)
                n_1 += 1  
                ships.append(mek)
        ships.sort(key=len)


# Отрисовка карты
def mapp():
    battle_status()
    for i in range(12):
        if i == 0 :
            for a in range(11):
                print(f'{Fore.YELLOW } {a}', end = '')
            print(' '*3+'🧱'*4+' '*3, end = '')
            for a in range(11):
                print(f'{Fore.YELLOW } {a}', end= '')      
            print()
        elif i == 11:
            print('🧱'*30)
        else:
            for j in range(31):
                if i == 10 and (j == 0 or j == 19):
                    print(f'{Fore.YELLOW}{i}', end= '|')
                elif j == 0 or j == 19:
                    print(f'{Fore.YELLOW } {i}', end= '|')
                elif j == 11 or j == 18:
                    print(' ', end = '')
                elif j == 12 or j == 17:
                    print('🧱', end = '')
                elif   12 < j < 17:
                    print('🩻', end = '')
                else:
                    if (i,j) in my_board:
                        if my_board[(i,j)] == 'k':
                            print('🔥', end = '')
                        elif my_board[(i,j)] == 'n':
                            print('🛟', end = '')
                        elif my_board[(i,j)] == 1:
                            print('❎', end = '')                            
                        else :
                            print('🌊', end = '')
                    elif j > 20:
                        if opponent_board[(i,j-20)] == 0:
                            print('🌊', end = '')
                        elif opponent_board[(i,j-20)] == 'x':
                            print('💢', end = '')
                        elif opponent_board[(i,j-20)] == 1:
                            print('🔥', end = '')                          
                        elif opponent_board[(i,j-20)] == 'y':
                            print('❌', end = '')
                        elif opponent_board[(i,j-20)] == 'n':
                            print('🛟', end = '')                        
            print()

# Атака
def k_ship_contour(cords):
    #up
    if cords[0] == 1 and cords[-1] == 1:
        ship_contour = [(1,2),(2,1)]
    elif cords[0] == 1 and cords[-1] == 10:
        ship_contour = [(1,9),(2,10)]
    elif cords[0] == 1 :
        ship_contour = [(cords[0]+1,cords[-1]),(cords[0],cords[-1]+1),(cords[0],cords[-1]-1)]

    #down
    elif cords[0] == 10 and cords[-1] == 1:
        ship_contour = [(10,2),(9,1)]
    elif cords[0] == 10 and cords[-1] == 10:
        ship_contour = [(10,9),(9,10)]
    elif cords[0] == 10 :
        ship_contour = [(cords[0]-1,cords[-1]),(cords[0],cords[-1]+1),(cords[0],cords[-1]-1)]           

    #middle
    elif cords[-1] == 1:
        ship_contour = [(cords[0]-1,cords[-1]),(cords[0]+1,cords[-1]),(cords[0],cords[-1]+1)]
    elif cords[-1] == 10:
        ship_contour = [(cords[0]-1,cords[-1]),(cords[0]+1,cords[-1]),(cords[0],cords[-1]-1)]

    #others
    else:
        ship_contour = [(cords[0]-1,cords[-1]),(cords[0]+1,cords[-1]),(cords[0],cords[-1]-1),(cords[0],cords[-1]+1)]
    
    possible_positionsy = []
    for i in ship_contour:
        if opponent_board[i] == 0:
            possible_positionsy.append(i)
    return possible_positionsy


def destroy(n_actual,cord_actual):
    if n_actual == 1:
        cord = cord_actual[-1]
        x = k_ship_contour(cord)
        next_cord = random.choice(x) 
    elif n_actual > 1:
        cord_actual.sort()
        ex = cord_actual[-2] 
        now = cord_actual[-1] 
        if ex[0] - now[0]: # uremn uxxahayac a texavorvac 
            if ((cord_actual[0][0] + 1, cord_actual[0][-1]) in opponent_board) and (opponent_board[(cord_actual[0][0] + 1, cord_actual[0][-1])] == 0):
                next_cord = (cord_actual[0][0] + 1, cord_actual[0][-1])
            elif ((cord_actual[0][0] - 1, cord_actual[0][-1]) in opponent_board) and (opponent_board[(cord_actual[0][0] - 1, cord_actual[0][-1])] == 0):
                next_cord = (cord_actual[0][0] - 1, cord_actual[0][-1])
            elif ((cord_actual[-1][0] + 1, cord_actual[-1][-1]) in opponent_board) and (opponent_board[(cord_actual[-1][0] + 1, cord_actual[-1][-1])] == 0):
                next_cord = (cord_actual[-1][0] + 1, cord_actual[-1][-1])
            elif ((cord_actual[-1][0] - 1, cord_actual[-1][-1]) in opponent_board) and (opponent_board[(cord_actual[-1][0] - 1, cord_actual[-1][-1])] == 0):
                next_cord = (cord_actual[-1][0] - 1, cord_actual[-1][-1])                                
        elif ex[-1] - now[-1]: # texavorvac a horizonakan
            if ((cord_actual[0][0] , cord_actual[0][-1]+1) in opponent_board) and (opponent_board[(cord_actual[0][0] , cord_actual[0][-1]+ 1)] == 0):
                next_cord = (cord_actual[0][0], cord_actual[0][-1] + 1)
            elif ((cord_actual[0][0], cord_actual[0][-1] - 1) in opponent_board) and (opponent_board[(cord_actual[0][0] , cord_actual[0][-1]- 1)] == 0):
                next_cord = (cord_actual[0][0] , cord_actual[0][-1]- 1)
            elif ((cord_actual[-1][0] , cord_actual[-1][-1]+ 1) in opponent_board) and (opponent_board[(cord_actual[-1][0] , cord_actual[-1][-1]+ 1)] == 0):
                next_cord = (cord_actual[-1][0] , cord_actual[-1][-1]+ 1)
            elif ((cord_actual[-1][0] , cord_actual[-1][-1]- 1) in opponent_board) and (opponent_board[(cord_actual[-1][0] , cord_actual[-1][-1]- 1)] == 0):
                next_cord = (cord_actual[-1][0] , cord_actual[-1][-1]- 1)  
    return next_cord


# Основной код
for game in range(10):
    if my_score == 3:
        os.system('cls')
        phrase = random.choice(f_win) 
        battle_status()
        print(Fore.YELLOW + Style.BRIGHT + phrase)
        exit()
    elif opponent_score == 3:
        os.system('cls')
        phrase = random.choice(f_lose)
        battle_status()
        print(Fore.YELLOW + Style.BRIGHT + phrase)
        exit()
    else:
        my_board = clean_board_coords.copy()
        opponent_board = clean_board_coords.copy()
        opponent_ships = ['a','b','c','d','e','f','g','h','i','j']
        place_ships(placement_strategy) 
        my_ships = [] 
        for i in ships:
            for j in i:
                my_ships.append(j)
        if battle_count == 1:
            while True: 
                stepp = input(f'\nКто делает первый шаг ?\tЯ: 1\t{opponent_name}: 2 \n-->\t')
                if len(stepp) == 1 and stepp.isdigit() and (int(stepp) == 1 or int(stepp) == 2):
                    whose_step = int(stepp)
                    break
                else:
                    print(random.choice(f_wrong_input))
        else:
            whose_step == last_winner
        
        ex_step = [] 
        n_actual = 0 # Количество попаданий
        cord_actual = []

        while True:
            steps += 1
            mapp()
            print(f'{Fore.YELLOW }\t\t\tСделано шагов 🎯 {steps}\n')
            print(f'{Fore.YELLOW + Style.BRIGHT}🚢 -> a -> 4  |  b,c -> 3  |  d,e,f -> 2  |  g,h,i,j -> 1')
            print(f'{Fore.YELLOW + Style.BRIGHT}⛵️ -> {opponent_ships}\n')
            print(f'{Fore.YELLOW + Style.BRIGHT}⚓️ -> {len(my_ships)} точек')
            print('🧱'*30)

            if not opponent_ships:
                battle_count += 1
                last_winner = 1
                my_score += 1
                steps = 0
                ships.clear()
                break
            elif not my_ships:
                battle_count += 1
                last_winner = 2
                opponent_score += 1
                placement_strategy += 1
                steps = 0
                ships.clear()
                break

            elif whose_step % 2 != 0:
                if 'a' in opponent_ships:
                    if len(ex_step) == 0 or n_actual == 0:
                        wave = find_possible_4ship_positions()
                        my_step = random.choice(wave) 
                        print(f'{Fore.YELLOW}Мой ход -->  ', my_step)
                        ex_step.append(my_step)
                        step = my_step
                    elif n_actual:
                            next_cord = destroy(n_actual,cord_actual)
                            print(f'{Fore.YELLOW}Мой ход -->  ', next_cord)
                            ex_step.append(next_cord)
                            step = next_cord
                elif 'b' in opponent_ships or 'c' in opponent_ships or 'd' in opponent_ships or  'e' in opponent_ships or 'f' in opponent_ships:
                    if n_actual == 0:
                        step = find_possible_3_2ship_positions()
                        my_step = random.choice(step)
                        print(f'{Fore.YELLOW}Мой ход -->  ', my_step)
                        ex_step.append(my_step)
                        step = my_step
                    elif n_actual:
                            next_cord = destroy(n_actual,cord_actual)
                            print(f'{Fore.YELLOW}Мой ход -->  ', next_cord)
                            ex_step.append(next_cord)
                            step = next_cord
                elif 'g' or 'h' or 'i' or 'j' in opponent_ships:
                    while True:
                        point = random.choice(list(opponent_board.keys()))
                        if opponent_board[point] == 0:
                            break
                    print(f'{Fore.YELLOW}Мой ход -->  ', point)
                    ex_step.append(point)
                    step = point                  

                while True: #opponenti patasxan(yes/no/m,a)
                        patasxan = input(f'{Fore.YELLOW}Yes|No|M,A -->\t').lower()
                        if patasxan in 'yes':
                            opponent_board[step] = 'y'
                            n_actual += 1
                            cord_actual.append(step)
                            break
                        elif patasxan in 'no':
                            opponent_board[step] = 'n'
                            break
                        elif 'm,' in patasxan :
                            patasxan = patasxan.split(',')
                            if len(patasxan) == 2 and patasxan[-1].isalpha() :
                                tar = patasxan[-1].lower()
                                if tar in opponent_ships:
                                    opponent_ships.remove(tar)
                                    if tar in ['g','h','i','j']:
                                        opponent_board[step] = 1
                                        mark_ship_contour(step,opponent_board)
                                        break
                                    elif tar in ['a','b','c','d','e','f']:
                                        cord_actual.append(step)
                                        for i in cord_actual:
                                            opponent_board[i] = 1
                                        for f in cord_actual:
                                            mark_ship_contour(f,opponent_board)
                                        n_actual = 0
                                        cord_actual.clear()
                                        break
                                else:
                                    print(random.choice(f_wrong_input))
                            else:
                                print(random.choice(f_wrong_input))
                        else:
                            print(random.choice(f_wrong_input))
                whose_step += 1
            
            elif whose_step % 2 == 0:  #opponenti step 
                while True:
                    print(f'{Fore.YELLOW}Пример хода -->\tY,X')
                    opponent = input(f'{Fore.YELLOW}Ход {opponent_name} -->\t')
                    opponent = opponent.split(',')
                    if len(opponent) == 2 and opponent[0].isdigit() and opponent[-1].isdigit():
                        if (int(opponent[0]),int(opponent[-1])) in my_board:
                            opponent_step = (int(opponent[0]),int(opponent[-1]))
                            if my_board[opponent_step] == 'k' or my_board[opponent_step] == 'n':
                                print('Что ты творишь дважды стреляешь в одно и тоже место ?!')
                            else:
                                if my_board[opponent_step] == 1:
                                    my_board[opponent_step] = 'k'
                                    my_ships.remove(opponent_step)
                                else:
                                    my_board[opponent_step] = 'n'
                                whose_step += 1
                                break
                        else:
                            print(random.choice(f_wrong_input))                        
                    else:
                        print(random.choice(f_wrong_input))