firstText = "          " 

for i in range (0 , 10):
    print(f'{firstText} {"*" * (1+i*2)}')
    firstText = (9-i) * " "

