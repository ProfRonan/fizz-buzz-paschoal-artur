#Receber o valor do usuário
user = int(input("Digite um número: \n"))

#Estabelecendo condições
if user % 3 == 0 and user % 5 == 0: 
    print("FizzBuzz")
else: 
    if user % 3 == 0 :
        print("Fizz")
    elif user % 5 == 0 :
        print("Buzz")
    else: 
        print(user)
