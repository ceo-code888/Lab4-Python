while True:
    expr = input("Введіть вираз (або натисніть Enter для виходу): ")
    if expr == "":  # Вихід з програми при натисканні Enter
        break
        
    if '+' in expr:
        a, b = expr.split('+')
        res = int(a) + int(b)
    elif '-' in expr:
        a, b = expr.split('-')
        res = int(a) - int(b)
    elif '*' in expr:
        a, b = expr.split('*')
        res = int(a) * int(b)
        
    print(res)

