# This application demonostrate dic function
# names  = ['Michael','Bob','Tracy']
# scores = [95,75,85]
#
# name = 'Bob'
#
# i = 0
# while i < 2:
#     if name == names[i]:
#         print('score of bob is', scores[i])
#         break
#     else:
#         i = i+1


names  = ['Michael','Bob','Tracy']

scores = [95,75,85]

d = {'Michael':95,'Bob':75,'Tracy':85}

print('input the name you want')

name = input()

print(d[name])