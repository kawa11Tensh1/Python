import random

a = {'rock': 'paper', 'paper': 'scissors', 'scissors': 'rock'}
rps = ['rock', 'paper', 'scissors']

you = str(input('Choose rock, scissors or paper: '))
comp = random.randint(0, len(rps) - 1)
print('Artificial intelligence has chosen:', rps[comp])

if you == rps[comp]:
    print('Draw:/')
else:
    for i, j in a.items():
        if you == i and comp == j:
            print('You won!')
        else:
            print('Bruh, you lost...')
            break