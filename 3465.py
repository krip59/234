# Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных
def readall(nm):
    with open(nm, 'r', encoding='utf8') as txt_file:
        for line in txt_file:
            print(line.strip())

def write_1(nm):
    str_new1 = input('Фамилия: ')
    str_new2 = input('Имя: ')
    str_new3 = input('Отчество: ')
    str_new4 = input('Телефон: ')
    str_new = '\n' + str_new1 + ', ' + str_new2+ ', ' + str_new3+ ', ' + str_new4
    with open(nm, 'a', encoding='utf8') as txt_file:
        txt_file.write(str_new)

def find_item(nm):
    item = input('Характеристика: ')
    with open(nm, 'r', encoding='utf8') as txt_file:
        for line in txt_file:
            if item.lower() in line.lower():
                print(line.strip())


def find_item_2(nm):
    item = input('Что ищем: ')
    item_type = int(input('Введите номер (0-фамилия, 1-имя, 2-отчество, 3-телефон): '))
    with open(nm, 'r', encoding='utf8') as txt_file:
        for line in txt_file:
            line = line.split(', ')
            if item.lower() in line[item_type].lower():
                print(*line)


def sort_data(nm):
    list_1 = []
    item_type = int(input('Введите номер (0-фамилия, 1-имя, 2-отчество, 3-телефон): '))
    with open(nm, 'r', encoding='utf8') as txt_file:
        for line in txt_file:
            line = line.split(', ')
            list_1.append(line)
    list_1.sort(key=lambda person: person[item_type])
    with open(nm, 'w', encoding='utf8') as txt_file:
        for line in list_1:
            line = ', '.join(line)
        txt_file.write(line)


def adding_and_removing (nm):      #Функция измениния данных
  with open(nm, "r", encoding="UTF-8") as file:
        data = sorted(file.readlines())
        readall('data.txt')

        numberContact = int(
            input("Введите номер контакта для изменения или 0 что бы вернуться в главное меню  ")
        )
        print(data[numberContact - 1].rstrip().split(","))
        if numberContact != 0:
            newLastName = input("Введите новое Фамилию: ")
            newName = input("Введите имя : ")
            newMiddleName = input('Введите отчевство: ')
            newPhone = input("Введите новый номер телефона: ")
            data[numberContact - 1] =(
                newLastName + "," + newName + "," + newMiddleName + ", "+ newPhone + "\n"
            )
            with open(nm, "w", encoding="UTF-8") as file:
                file.write("".join(data))
                print("\nКонтакт был успешно изменен!")
                input("\n--- нажмите любую клавишу ---")
        else:
            return


def deleteContact (nm):                           #Функция для удаления контакта
      with open(nm, "r+", encoding="UTF-8") as file:
        data = sorted(file.readlines())
        readall(nm)

        numberContact = int(
            input("Введите номер контакта которого хотите удалить или введите 0 для выхода в главное меню: ")
        )
        if numberContact != 0:
            print(f"Удаление записи: {data[numberContact-1].rstrip().split(',')}\n")
            data.pop(numberContact - 1)
            with open(nm, "w", encoding="UTF-8") as file:
                file.write("".join(data))

        else:
            return


# write_1('data.txt')
# readall('data.txt')
# find_item('data.txt')
# adding_and_removing('data.txt')
# deleteContact('data.txt')