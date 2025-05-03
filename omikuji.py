import random
number=random.randint(1,100)

print('おみくじを引きます')

if number<=23: print('大吉')
elif number<=33: print('中吉')
elif number<=46: print('小吉')
elif number<=70: print('吉')
elif number<=89: print('末吉')
else: print('凶')