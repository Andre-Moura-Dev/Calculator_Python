def tabuada(numero):
    print(f"Tabuada do {numero}: ")
    for i in range(1,11):
        print(f"{numero} x {i} = {numero * i}")
        
numero_usuario = int(input("Informe um número para ver a tabuada: "))
tabuada(numero_usuario)