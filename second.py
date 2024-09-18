def my_input(amount):
    try:
        if amount == -1:
            return int(input())
        else:
            print(f'введите {amount+1}: ')
            return int(input())
    except Exception as ex:
        print(ex)
