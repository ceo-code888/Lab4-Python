while True:
    s = input("Введіть бінарний рядок (порожній для виходу): ")
    if s == "":  # Вихід з циклу, якщо рядок порожній або користувач натиснув Enter без введення даних11
        break

    result = []
    zero_count = 0

    for char in s:
        if char == '0':
            zero_count += 1
        elif char == '1':
            letter = chr(ord('a') + zero_count)
            result.append(letter)
            zero_count = 0

    print("".join(result))