# Define os códigos ASCII do primeiro e último caracteres maiúsculos do alfabeto inglês.
FIRST_CHAR_CODE = ord("A")
LAST_CHAR_CODE = ord("Z")
CHAR_RANGE = LAST_CHAR_CODE - FIRST_CHAR_CODE + 1

def caesar_shift(message, shift):
    """
    Função para aplicar a cifra de César a uma mensagem.

    Parameters:
    message (str): A mensagem que será criptografada.
    shift (int): O número de posições a serem deslocadas no alfabeto.

    Returns:
    str: A mensagem criptografada.
    """
    result = ""  # Placeholder para armazenar o resultado da criptografia.
    
    # Converte cada caractere da mensagem para maiúsculo e aplica o deslocamento.
    for char in message.upper():
        if char.isalpha():  # Verifica se o caractere é uma letra.
            char_code = ord(char)  # Converte o caractere para o código ASCII.
            # Calcula o novo código do caractere após o deslocamento, com wrap-around.
            new_char_code = FIRST_CHAR_CODE + (char_code - FIRST_CHAR_CODE + shift) % CHAR_RANGE
            new_char = chr(new_char_code)  # Converte o novo código ASCII de volta para um caractere.
            result += new_char  # Adiciona o novo caractere ao resultado.
        else:
            result += char  # Se não for uma letra, adiciona o caractere original ao resultado.
    
    return result  # Retorna a mensagem criptografada.

def get_user_input():
    """
    Função para obter a entrada do usuário para a mensagem e a chave de deslocamento.

    Returns:
    tuple: Contendo a mensagem do usuário e a chave de deslocamento.
    """
    user_message = input("Messagem que será criptografada: ")  # Solicita a mensagem do usuário.
    
    # Loop para garantir que o usuário insira um valor inteiro válido para a chave de deslocamento.
    while True:
        try:
            user_shift_key = int(input("Chave Shift (números inteiros): "))  # Solicita a chave de deslocamento.
            break  # Sai do loop se a entrada for um inteiro válido.
        except ValueError:
            print("Por favor, coloque um valor válido na chave shift.")  # Mensagem de erro para entrada inválida.
    
    return user_message, user_shift_key  # Retorna a mensagem e a chave de deslocamento do usuário.

if __name__ == "__main__":
    user_message, user_shift_key = get_user_input()  # Obtém a entrada do usuário.
    cipher_text = caesar_shift(user_message, user_shift_key)  # Aplica a cifra de César à mensagem.
    print(f"Texto criptografado: {cipher_text}")  # Exibe a mensagem criptografada.
