valorbanca = float(input("Digite o valor da banca: "))
valoraposta = float(input("Digite o valor da aposta inicial: "))

double = 0
quantiacinza = 0

while valorbanca > valoraposta:
    double += 1
    valorbanca-=valoraposta
    if(double >=2):
        valoraposta = valoraposta*2
        double = 0
    quantiacinza+=1

print("Quantidade de Cinza Aceitos: " + str(quantiacinza))