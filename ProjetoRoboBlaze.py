import pyautogui
import time
from PIL import ImageGrab
from pynput import mouse
from pynput.mouse import Listener
from datetime import datetime
import tkinter as tk
from threading import Thread
import sys


# Coordenada Crash: 
# Historico: (1337, 761) // Cor Verde: 4,212,124   Cinza: 52,61,73
# Crash Vermelho: (990, 439) Cor: 241,44,76
# Tempo de 2x = 11.5s
# Tempo de 3x = 18s
# Demais x = +3s/x
# Tempo de 10x = 39s
# Tempo de 20x = 63s

positionCrashCoordinate = 0
positionUltimoResultadoCoordinate = 0
positionComecar = 0
positionDobrar = 0
positionDividir = 0
positionEscrever = 0

root = None  # Variável global para a janela
labels = []

# Função para atualizar o label da interface gráfica
def update_label(index, novo_texto):
    # Verifica se o índice existe na lista de labels
    if index < len(labels):
        labels[index].config(text=novo_texto)
    else:
        print(f"Índice {index} não encontrado na lista de labels.")

def on_click(x, y, button, pressed):
    global positionCrashCoordinate, positionUltimoResultadoCoordinate, positionComecar, positionDobrar, positionDividir, positionEscrever
    if pressed:  # Quando o botão do mouse é pressionado
        if positionCrashCoordinate == 0:
            positionCrashCoordinate = (x, y)
            print(f"Coordenada do Crash salva: {positionCrashCoordinate}")
            update_label(0, "Clique para selecionar a posição do Resultado!")
        elif positionUltimoResultadoCoordinate == 0:
            positionUltimoResultadoCoordinate = (x, y)
            print(f"Coordenada do Resultado salva: {positionUltimoResultadoCoordinate}")
            update_label(0, "Clique para selecionar a posição do Comecar!")
        elif positionComecar == 0:
            positionComecar = (x, y)
            print(f"Coordenada do Comecar salva: {positionComecar}")
            update_label(0, "Clique para selecionar a posição do Dobrar!")
        elif positionDobrar == 0:
            positionDobrar = (x, y)
            print(f"Coordenada do Dobrar salva: {positionDobrar}")
            update_label(0, "Clique para selecionar a posição do Dividir!")
        elif positionDividir == 0:
            positionDividir = (x, y)
            print(f"Coordenada do Dividir salva: {positionDividir}")
            update_label(0, "Clique para selecionar a posição de Escrever!")
        elif positionEscrever == 0:
            positionEscrever = (x, y)
            print(f"Coordenada do Dividir salva: {positionEscrever}")
        
        # Se ambos os cliques foram feitos, fecha o Listener
        if positionCrashCoordinate != 0 and positionUltimoResultadoCoordinate and positionComecar and positionDobrar and positionDividir != 0 and positionEscrever != 0:
            return False  # Isso vai parar o Listener

def get_color_at_position(position):
    screenshot = ImageGrab.grab()
    color = screenshot.getpixel(position)
    return color

def cores_similares(cor1, cor2, margem):
    return all(abs(c1 - c2) <= margem for c1, c2 in zip(cor1, cor2))
    
def esperar_cliques():
    update_label(0, "Clique para selecionar a posição do Crash e do Resultado.")
    
    # Inicia o listener do mouse
    with Listener(on_click=on_click) as listener:
        listener.join()  # Aguarda até que ambos os cliques sejam feitos

    # Verifica se as posições foram selecionadas
    if positionCrashCoordinate != 0 and positionUltimoResultadoCoordinate != 0 and positionComecar != 0 and positionDobrar != 0 and positionDividir != 0 and positionEscrever != 0:
        print(f"Posição do Crash: {positionCrashCoordinate}")
        print(f"Posição do Resultado: {positionUltimoResultadoCoordinate}")
        print("Ambas as posições foram selecionadas.")
    else:
        update_label(0, "Não foi possível selecionar as posições. Fechando o programa.")
        root.quit()  # Fecha a janela Tkinter se as posições não forem selecionadas

def criar_janela_flutuante():
    global root  # Referência as variáveis globais para a janela

    # Função para fechar a janela e encerrar o programa
    def fechar():
        root.quit()  # Fecha a janela Tkinter
        sys.exit()   # Finaliza o programa

    # Criando a janela flutuante (root)
    root = tk.Tk()

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    window_width = 400  # ajuste conforme necessário
    window_height = 400

    x = screen_width - window_width
    y = screen_height - window_height

    root.geometry(f"{window_width}x{window_height}+{x}+{y}")  # Posição na tela (ajuste conforme necessário)

    root.title("Informações do Programa")
    root.configure(bg="lightblue")  # Cor de fundo
    root.attributes("-topmost", True)  # A janela ficará sempre no topo
    root.overrideredirect(True)  # Remove a barra de título

    # Adicionando o texto informativo
    label1 = tk.Label(root, text="Clique para selecionar a posição do crash!", font=("Arial", 10), bg="lightblue")
    label1.pack(pady=20)
    labels.append(label1)  # Adiciona à lista de labels

    # Adicionando o botão de fechar
    fechar_button = tk.Button(root, text="Fechar", command=fechar, font=("Arial", 10))
    fechar_button.pack(pady=10)

    root.mainloop()  # Inicia o loop da janela Tkinter

def main():
    crash = 0
    verde = 0
    cinza = 0
    coratual = 0
    cinzasseguidos = 0
    maiorcinzasseguidos = 0
    cinzaacima11 = 0
    cinzaacima15 = 0

    quantidadeacimade10 = 0
    quantidademaximaatechegarum10 = 0
    quantidadesem10 = 0

    tempocrash = 0

    dataultimocrash = 0

    quantiasemdobrar = 0
    quantiadedobra = 0

    datainicio = 0
    tempototal = 0

    tempopararesgatar = 39
    multi=0

    valorbancainicial = float(input("Digite a sua banca Inicial: "))
    valorapostainicial = float(input("Valor da aposta inicial: "))
    valorbancaatual = valorbancainicial
    valorapostaatual = valorapostainicial

    algoritimo = 0
    
    # Inicia a janela flutuante em uma thread separada
    thread_janela = Thread(target=criar_janela_flutuante)
    thread_janela.start()

    print("Inicializando programa em 5 segundos...")
    # Certifique-se de que a thread que cria a janela flutuante terminou antes de continuar
    time.sleep(5)  # Aguarda o tempo suficiente para garantir que a janela foi criada e as labels foram inicializadas.

    try:
        # Aguarda os cliques para selecionar as posições
        esperar_cliques()

        pyautogui.moveTo(positionCrashCoordinate)
        time.sleep(1)
        pyautogui.moveTo(positionUltimoResultadoCoordinate)
        time.sleep(1)
        pyautogui.moveTo(positionComecar)
        time.sleep(1)
        pyautogui.moveTo(positionDobrar)
        time.sleep(1)
        pyautogui.moveTo(positionDividir)
        time.sleep(1)
        pyautogui.moveTo(positionEscrever)
        time.sleep(1)

        update_label(0, "Iniciando apostas!")

        label2 = tk.Label(root, text="Informações adicionais aqui", font=("Arial", 10), bg="lightblue")
        label2.pack(pady=1)
        labels.append(label2)

        label3 = tk.Label(root, text=f"Quantidade de Crash: {crash}", font=("Arial", 10), bg="lightblue")
        label3.pack(pady=1)
        labels.append(label3)

        label4 = tk.Label(root, text=f"Quantidade máxima de cinzas seguidos registrados: {maiorcinzasseguidos}", font=("Arial", 10), bg="lightblue")
        label4.pack(pady=1)
        labels.append(label4)

        label5 = tk.Label(root, text=f"Quantidade de Verdes: {verde}", font=("Arial", 10), bg="lightblue")
        label5.pack(pady=1)
        labels.append(label5)

        label6 = tk.Label(root, text=f"Quantidade de Cinzas: {cinza}", font=("Arial", 10), bg="lightblue")
        label6.pack(pady=1)
        labels.append(label6)

        label7 = tk.Label(root, text=f"Cinzas Acima/Igual 11x seguidos: {cinzaacima11}", font=("Arial", 10), bg="lightblue")
        label7.pack(pady=1)
        labels.append(label7)

        label8 = tk.Label(root, text=f"Cinzas Acima/Igual 15x seguidos: {cinzaacima15}", font=("Arial", 10), bg="lightblue")
        label8.pack(pady=1)
        labels.append(label8)

        label9 = tk.Label(root, text=f"Quantidade Acima/Igual a 10: {quantidadeacimade10}", font=("Arial", 10), bg="lightblue")
        label9.pack(pady=1)
        labels.append(label9)

        label10 = tk.Label(root, text=f"Quantidade máxima até chegar a 10: {quantidademaximaatechegarum10}", font=("Arial", 10), bg="lightblue")
        label10.pack(pady=1)
        labels.append(label10)

        label11 = tk.Label(root, text=f"Banca Atual: {valorbancaatual}", font=("Arial", 10), bg="lightblue")
        label11.pack(pady=1)
        labels.append(label11)

        label12 = tk.Label(root, text=f"Valor de Aposta Atual: {valorapostaatual}", font=("Arial", 10), bg="lightblue")
        label12.pack(pady=1)
        labels.append(label12)

        time.sleep(2)

        with open('lastedlog.txt', 'w') as file:
            data = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            file.write('Inicializando o Programa: ' + data)
            file.write('...')
        datainicio = datetime.now()
        # Lógica do processo de Crash
        while True:
                
            positionCrash = positionCrashCoordinate
            colorCrash = get_color_at_position(positionCrash)
            
            if cores_similares(colorCrash, (241, 44, 76), 30):
                update_label(1, f"Crash!")
                tempousado = 0
                quantiasemdobrar += 1
                if dataultimocrash != 0:
                    diferenca = datetime.now() - dataultimocrash
                    tempocrash = diferenca.total_seconds()
                else:
                    tempocrash = 0
                if algoritimo == 0:
                    tempopararesgatar = 11
                    multi=2
                    quantiapradobrar = 2
                else:
                    tempopararesgatar = 39
                    multi=10
                    quantiapradobrar = 8

                #Verificação da quantia acima ou igual a 10
                if tempocrash >= 39:
                    quantidadeacimade10 += 1
                    if quantidadesem10 > quantidademaximaatechegarum10:
                        quantidademaximaatechegarum10 = quantidadesem10
                    quantidadesem10 = 0
                else:
                    quantidadesem10 += 1

                if tempocrash >= tempopararesgatar:
                    if valorbancaatual > 0:
                        valorbancaatual = valorbancaatual + (valorapostaatual*multi)
                        valorapostaatual = valorapostainicial
                        quantiasemdobrar = 0
                        quantiadedobra = 0

                        pyautogui.moveTo(positionEscrever)
                        pyautogui.click()
                        for _ in range(5):
                            pyautogui.press('backspace')
                            time.sleep(0.1)
                            tempousado+=0.1
                        pyautogui.typewrite(str({valorapostainicial}), interval=0.1)
                        tempousado+=0.3
                    
                print(f"Crash em {tempocrash} segundos: " + datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
                crash += 1

                # Aguarda até a cor mudar
                while cores_similares(colorCrash, (241, 44, 76), 30):
                    colorCrash = get_color_at_position(positionCrash)
                    time.sleep(0.1)

                update_label(1, f"Iniciando Apostas!")

                print("Iniciando apostas: " + datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

                # Simula a posição do Resultado
                positionResultado = positionUltimoResultadoCoordinate
                colorResultado = get_color_at_position(positionResultado)

                # Verifica se a cor do resultado é similar a cinza ou verde
                if cores_similares(colorResultado, (46, 55, 67), 30):
                    cinza += 1
                    cinzasseguidos += 1
                    print(f"Cor Cinza! {colorResultado}")
                else:
                    verde += 1
                    if cinzasseguidos > maiorcinzasseguidos:
                        maiorcinzasseguidos = cinzasseguidos
                    if cinzasseguidos >= 15:
                        cinzaacima15 += 1
                    elif cinzasseguidos >= 11:
                        cinzaacima11 += 1
                    cinzasseguidos = 0
                    print(f"Cor Verde! {colorResultado}")

                print(f"Cor do resultado: {colorResultado}")

                with open('lastedlog.txt', 'a') as file:
                    data = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    file.write(f'\nResultado: ' + data)
                    file.write(f'\nQuantidade de Crash: {crash}')
                    file.write(f'\nQuantidade máxima de cinzas seguidos registrados: {maiorcinzasseguidos}')
                    file.write(f'\nQuantidade de Verdes: {verde}')
                    file.write(f'\nQuantidade de Cinzas: {cinza}')
                    file.write(f'\nCinzas Acima/Igual 11x seguidos: {cinzaacima11}')
                    file.write(f'\nCinzas Acima/Igual 15x seguidos: {cinzaacima15}')
                    file.write(f'\nQuantidade Acima/Igual a 10: {quantidadeacimade10}')
                    file.write(f'\nQuantidade máxima até chegar a 10: {quantidademaximaatechegarum10}')
                    file.write(f'\nBanca Atual: {valorbancaatual}')
                    file.write(f'\nValor de Aposta Atual: {valorapostaatual}')
                    file.write(f'...')

                if(quantiasemdobrar >= quantiapradobrar):
                    quantiasemdobrar=1
                    quantiadedobra+=1
                    valorapostaatual=valorapostaatual*2
                    print("Dobrando!")
                    pyautogui.moveTo(positionDobrar)
                    time.sleep(0.1)
                    tempousado+=0.1
                    pyautogui.click()

                valorbancaatual = valorbancaatual - valorapostaatual
                
                #Apertar em Apostar
                #pyautogui.moveTo(positionComecar)
                #time.sleep(0.1)
                #tempousado+=0.1
                #pyautogui.click()
                
                # Atualiza a label de quantidade de crashes
                update_label(2, f"Quantidade de Crash: {crash}")
                update_label(3, f"Quantidade máxima de cinzas seguidos registrados: {maiorcinzasseguidos}")
                update_label(4, f"Quantidade de Verdes: {verde}")
                update_label(5, f"Quantidade de Cinzas: {cinza}")
                update_label(6, f"Cinzas Acima/Igual 11x seguidos: {cinzaacima11}")
                update_label(7, f"Cinzas Acima/Igual 15x seguidos: {cinzaacima15}")
                update_label(8, f"Quantidade Acima/Igual a 10: {quantidadeacimade10}")
                update_label(9, f"Quantidade máxima até chegar a 10: {quantidademaximaatechegarum10}")
                update_label(10, f"Banca Atual: {valorbancaatual}")
                update_label(11, f"Valor de Aposta Atual: {valorapostaatual}")

                tempoespera = 5 - tempousado
                time.sleep(tempoespera)
                print("Novo jogo iniciado!" + datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
                dataultimocrash = datetime.now()
                update_label(1, f"Novo Jogo iniciado!")

            time.sleep(0.1)
    except KeyboardInterrupt:
        data = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        tempototal = datetime.now() - datainicio
        with open('lastedlog.txt', 'a') as file:
            file.write('Finalizando Programa: ' + data)
            file.write('Tempo de Ação: ' + tempototal.total_seconds())
        print("Programa encerrado.")
        print(f"Quantidade de Crash: {crash}")
        print(f"Quantidade máxima de cinzas seguidos registrados: {maiorcinzasseguidos}")
        print(f"Quantidade de Verdes: {verde}")
        print(f"Quantidade de Cinzas: {cinza}")
        print(f"Quantidade Acima/Igual a 10: {quantidadeacimade10}")
        print(f"Quantidade máxima até chegar a 10: {quantidademaximaatechegarum10}")

        # Encerra a janela flutuante após o término do programa
        root.quit()

if __name__ == "__main__":
    main()