while True:
    s = input("Введіть рядок (або натисніть Enter для виходу): ")
    if s == "":  # Якщр користувач натискає Enter без введення рядка, програма завершується
        break
    s_clean = s.replace(" ", "").lower()
    is_pal = s_clean == s_clean[::-1]
    print(is_pal)