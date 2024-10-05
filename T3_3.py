import time
print('-сколько у тебя щас денег?')
time.sleep(1)
m = open('m.txt', 'r')
text = m.read()
m.close
print(text)
mon = input('-какая у тебя зарптала?')
mon = int(mon)
print(12000+mon)
