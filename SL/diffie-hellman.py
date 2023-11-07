# Take user input
q=int(input('Enter q: '))
alpha=int(input('Enter alpha: '))
xa=int(input('Enter xa: '))
xb=int(input('Enter xb: '))

# Compute the YA and YB
ya=pow(alpha,xa,q)
yb=pow(alpha,xb,q)
print('Public of Ya: ',ya, ' Public of Yb: ',yb)

share_secretA=pow(yb,xa,q)
print('Shared secret key of A: ',share_secretA)
share_secretB=pow(ya,xb,q)
print('Shared secret key of B: ',share_secretB)

if share_secretA==share_secretB:
  print('Matched')
else:
  print('Try again')

print('Pair of Public Keys: ',(ya,yb))
print('Pair of Private Keys: ',(xa,xb))
print('Shared secret key of A & B: ',share_secretA)