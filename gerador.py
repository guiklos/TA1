import time
start_t = time.time()
a=2022
semente=16807
modulo=(2**31)-1
for n in range(60000000):
    num_aleatorio = (semente * a) % modulo
    a=num_aleatorio
    x=num_aleatorio/modulo
    b=str(x)
    with open("dados.txt", "a") as arquivo:
        arquivo.write(b)
        arquivo.write("\n")
print(time.time() - start_t)