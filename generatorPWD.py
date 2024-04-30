import argparse
import random
import string

def gerar_senha(tamanho_senha:int=15, quantidade:int=+1) -> None:
    # Definir characteres
    randomlettersLower = string.ascii_lowercase
    randomletterUpper = string.ascii_uppercase
    randomNumber = string.digits
    randomEspecialChar = string.punctuation

    characters = randomlettersLower + randomNumber + randomletterUpper + randomEspecialChar

    # Gera senha baseado nas informações
    for _ in range(quantidade):
        password = ''.join(random.choice(characters) for i in range(tamanho_senha))
        print("Random password is:", password)

if __name__ == "__main__":
    # Receber argumentos dos usuário
    parser = argparse.ArgumentParser(description="Gerador de Senha Aleatória")
    parser.add_argument("--tamanho", type=int, default=15, help="Tamanho da senha a ser gerada (padrão: 15)")
    parser.add_argument("--quantidade", type=int, default=1, help="Quantidade de senhas a serem geradas (padrão: 10)")
    args = parser.parse_args()

    gerar_senha(args.tamanho, args.quantidade)
