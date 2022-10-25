def instruction():
    print("\t--------------------------------------------------------------------------------------------------------")
    print("\t                                              ПРАВИЛА                                                   ")
    print("\t--------------------------------------------------------------------------------------------------------")
    print("Игроки по очереди ставят на свободные ячейки от 1 до 9 знаки (один всегда крестики, другой всегда нолики)."
      "\n"
      "Первый, выстроивший в ряд 3 своих фигуры по вертикали, горизонтали или диагонали, выигрывает."
      "\n"
      "Первый ход делает игрок, ставящий крестики.")
    print("\n")
    print("Формат поля: ")
    print("\n")
    print("\t    |   |")
    print(f"\t  1 | 2 | 3")
    print("\t ___|___|___")
    print("\t    |   |")
    print(f"\t  4 | 5 | 6")
    print("\t ___|___|___")
    print("\t    |   |")
    print(f"\t  7 | 8 | 9")
    print("\t    |   |")
    print("\n")
instruction()

print("\n")

val=[" " for i in range(9)]

def show():
    print("\n")
    print("\t    |   |")
    print(f"\t  {val[0]} | {val[1]} | {val[2]}")
    print("\t ___|___|___")
    print("\t    |   |")
    print(f"\t  {val[3]} | {val[4]} | {val[5]}")
    print("\t ___|___|___")
    print("\t    |   |")
    print(f"\t  {val[6]} | {val[7]} | {val[8]}")
    print("\t    |   |")
    print("\n")

def check():
    while True:
        chance = int(input("Введите номер ячейки: "))
        if chance < 1 or chance > 9:
            print("Выход за пределы! Введите ещё раз!")
            continue
        if val[chance-1] != " ":
            print("Клетка занята! Введите ещё раз!")
            continue
        return chance
def win():
        if val[0] == val[1] == val[2] == "X" or  val[3] == val[4] == val[5] == "X" or val[6] == val[7] == val[8] == "X" \
                or val[0] == val[4] == val[8] == "X" or val[2] == val[4] == val[6] == "X":
            return True
        if val[0] == val[1] == val[2] == "O" or  val[3] == val[4] == val[5] == "O" or val[6] == val[7] == val[8] == "O" \
                or val[0] == val[4] == val[8] == "O" or val[2] == val[4] == val[6] == "O":
            return True

count = 0
while True:
    count += 1
    if count%2==1:
        print('Ход игрока "X"')
        chance = check()
        val[chance-1]="X"
        show()
        a = win()
        if a:
            print('Выиграл игрок "X"')
            break

    if count%2==0:
        print('Ход игрока "O"')
        chance = check()
        val[chance - 1] = "O"
        show()
        a = win()
        if a:
            print('Выиграл игрок "O"')
            break
    if count==9:
        print("Ничья!")
        break



