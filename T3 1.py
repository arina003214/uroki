words =  []
for i in range(8):
    word = input(f"введите {i +1} слово:")
    words.append(word)
if 'молоко' in words:
    print("слово 'молоко' есть в списке")
else:
    print("слово 'молоко' нет в списке")
    