# for var in range(0,10):
#     print('Ola,mundo!')

# print('Saiu do laço')   
#---------------------------------
# for var in range(7, 0, -2):
#     print(var)
#-------------------------------------------------------

start = int(input('Digite o inicio do for:'))
end = int(input('Digite o final do for:'))
step = int(input('Digite o passo:'))

for var in range(start, end, step):
    print(var, end)
print('Saiu do laço')    