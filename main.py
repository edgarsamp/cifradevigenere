"""
Aluno: Edgar Sampaio de Barros
Matricula: 160005213
"""

from cifraVigenere import Vigenere

def print_menu():
    print("-========== cifra de Vigenere ==========-")
    print("1 - Cifrar mensagem")
    print("2 - Decifrar mensagem")
    print("3 - Ataque de recuperação de senha")
    print("0 - Sair")
    print("Digite uma opção: ", end="")

def menu():
    while(True):
        print_menu()
        op = input()
        if op in ("1", "2", "3"):
            print(op)
            return op
        elif op == "0":
            break
        else:
            print("\n\n\n\n\nDigite uma opção válida")

def ler_arquivo():
    try:
        f = open("input.txt", encoding="utf-8")
        chave = f.readline().strip().lower()
        mensagem = f.read().strip().lower()
        return chave, mensagem
    except:
        print("Erro na leitura do arquivo input.txt")

def ler_arquivo_mensagem():
    try:
        f = open("input.txt", encoding="utf-8")
        mensagem = f.read().strip().lower()
        return mensagem
    except:
        print("Erro na leitura do arquivo input.txt")


def escrever_arquivo(mensagem):
    with open("output.txt", "w") as f:
        f.write("Mensagem: \n" + mensagem)


def escrever_arquivo_ataque(mensagem, chaves):
    with open("output.txt", "w") as f:
        f.write("Caso a mensagem esteja em portugues, a chave encontrada foi: " + chaves[0])
        f.write("\nDecifrando temos: \n" + Vigenere().decifrar(mensagem, chaves[0]))

        f.write("\n\nCaso a mensagem esteja em ingles, a chave encontrada foi: " + chaves[1])
        f.write("\nDecifrando temos: \n" + Vigenere().decifrar(mensagem, chaves[1]))
        
if __name__ == "__main__":
    op = menu()
    if op == "1":
        print("Digite a chave e a mensagem no arquivo input.txt, uma cada linha e nesta mesma ordem.")
        input()
        chave, mensagem = ler_arquivo()
        mensagem_cifrada = Vigenere().cifrar(mensagem, chave)
        escrever_arquivo(mensagem_cifrada)


    elif op == "2":
        print("Digite a chave e a mensagem no arquivo input.txt, uma cada linha e nesta mesma ordem.")
        input()
        chave, mensagem = ler_arquivo()
        mensagem_decifrada = Vigenere().decifrar(mensagem, chave)
        escrever_arquivo(mensagem_decifrada)

    elif op == "3":
        print("Digite mensagem no arquivo input.txt.")
        input()
        mensagem = ler_arquivo_mensagem()
        chaves = Vigenere().ataque(mensagem)
        escrever_arquivo_ataque(mensagem, chaves)
    
    print("Resultado está no arquivo output.txt")
