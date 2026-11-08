m = int(input("Введіть m: "))
text = input("Введіть текст: ")

words = text.split()
current_line = ""

for word in words:
    if not current_line:
        current_line = word
    elif len(current_line) + 1 + len(word) <= m:
        current_line += " " + word
    else:
        print(current_line)
        current_line = word

if current_line:
    print(current_line)