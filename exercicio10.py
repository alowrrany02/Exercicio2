def converter_para_inteiro(texto: str):
    """
    Converte uma string para inteiro com tratamento de erros
    
    Args:
        texto: String que será convertida para inteiro
    
    Returns:
        O valor inteiro convertido ou mensagem de erro se a conversão falhar
    """
    try:
        numero = int(texto)
        return numero
    except ValueError:
        return f"Erro: '{texto}' não é um número inteiro válido"


print(converter_para_inteiro("123"))  
print(converter_para_inteiro("-45"))   
print(converter_para_inteiro("12.5"))
print(converter_para_inteiro("abc"))
print(converter_para_inteiro("123a")) 