import random
words = []
for i in range(6):
    a = input()
    if a not in words:
        words.append(a)
    else:
        while a in words:
           print('That is llready writen')
           a = input()
        words.append(a)
random.shuffle(words)
b = 1
c = 0
x = 10
while b != words[c-1] or x < 1:
    c = random.randint(1, 6)
    print('what is %s in list' % c)
    b = input()
    if b == words[c-1]:
        print('Correct!')
        break
    else:
        print('wrong')
    x = x - 1
print('[you got %s pints]' % x)
