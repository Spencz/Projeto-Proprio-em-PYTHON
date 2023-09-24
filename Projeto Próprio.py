import random
import string

def gerar_senha(comprimento=12):
    caracteres_especiais = '!@#$%^&*()_+-=[]{}|;:,.<>?'
    
    if comprimento < 8:
        comprimento = 8

    
    letras_maiusculas = ''.join(random.choices(string.ascii_uppercase, k=2))
    letras_minusculas = ''.join(random.choices(string.ascii_lowercase, k=2))
    numeros = ''.join(random.choices(string.digits, k=2))
    especiais = ''.join(random.choices(caracteres_especiais, k=2))
    
    
    todos_os_caracteres = letras_maiusculas + letras_minusculas + numeros + especiais
    senha_aleatoria = ''.join(random.choices(todos_os_caracteres, k=comprimento - 8))

    
    senha = letras_maiusculas + letras_minusculas + numeros + especiais + senha_aleatoria
    senha = ''.join(random.sample(senha, len(senha)))

    return senha

if __name__ == "__main__":
    comprimento_senha = int(input("Digite o comprimento da senha desejada: "))
    senha_gerada = gerar_senha(comprimento_senha)
    print("Senha gerada:", senha_gerada)
