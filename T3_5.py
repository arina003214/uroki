z = input('у васи в запасе:')
z = int(z)
d = input('но вася должен другу:')
d = int(d)
t = input('и еще должен своему тренеру:')
t = int(t)
print('если вася отдаст долги, то у него будет:', float(z)-float(d)-float(t),'рублей')