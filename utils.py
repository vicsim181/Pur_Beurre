def int_input(min_nb, max_nb, message):
    while True:
        raw = input(message)
        if raw.isdigit():
            nb = int(raw) 
            if nb in range(min_nb, max_nb + 1):
                return nb
        print(f'Please enter an integer between {min_nb} and {max_nb}.')

