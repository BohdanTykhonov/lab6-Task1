def process_list():
    user_input = input("Введіть елементи списку через пробіл: ")
    user_list = user_input.split()
    user_list = [int(x) for x in user_list]

    odd_index_elements = [user_list[i] for i in range(1, len(user_list), 2)]

    user_list.extend(odd_index_elements)

    print("Список після доповнення:", user_list)

process_list()