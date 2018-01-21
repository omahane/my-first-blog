name = 'Christian'

print('Hello, Django girls')
if 3 < 2:
    print('It works!')
else:
    print('3 is not less than 2')

def hi(n):
    print('Hello, ' + n)

hi(name)
hi("Carol")

girls = ['Carol','Ava','Melany','Anna','Lauren','Caroline']
for g in girls:
    print(g)

for i in range(1,4):
    print(girls[(i*2)-1])
