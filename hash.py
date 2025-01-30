import numpy as np

strings = ["apple", "voadora", "banjo", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "xuru", "runin", "xamã", "mirtilho", "lemon", "mango", "nectarine", "orange", "papaya", "quince", "raspberry", "strawberry", "tangerine", "ugli", "voavanga", "maravilha", "IFCE", "maracanaú", "ceará", "manga", "rendemption", "bobo", "maluco"]

TABLE_SIZE = 32  
P = 37  
A, B = 3, 7  

def hash_somatorio(string):
    return sum(ord(c) for c in string)

def hash_polinomial(string, base=31):
    return sum(ord(c) * (base ** i) for i, c in enumerate(string))

def hash_deslocamento(string):
    hash_value = 0
    for c in string:
        hash_value = (hash_value << 5) - hash_value + ord(c)  # deslocamento e subtração
    return hash_value

def compressao_divisao(hash_value):
    return hash_value % TABLE_SIZE

def compressao_dobra(hash_value):
    str_hash = str(abs(hash_value))
    partes = [int(str_hash[i:i+2]) for i in range(0, len(str_hash), 2)]
    return sum(partes) % TABLE_SIZE

def compressao_mad(hash_value):
    return ((A * hash_value + B) % P) % TABLE_SIZE

def preencher_tabela(hash_func, compress_func):
    tabela = [None] * TABLE_SIZE
    colisoes = 0
    for string in strings:
        hash_value = hash_func(string)
        index = compress_func(hash_value)
        if tabela[index] is None:
            tabela[index] = string
        else:
            colisoes += 1
    return tabela, colisoes

def testar_metodos():
    metodos_hash = {
        "Somatório": hash_somatorio,
        "Polinomial": hash_polinomial,
        "Deslocamento": hash_deslocamento
    }
    metodos_compressao = {
        "Divisão": compressao_divisao,
        "Dobra": compressao_dobra,
        "MAD": compressao_mad
    }
    
    resultados = {}
    for h_name, h_func in metodos_hash.items():
        for c_name, c_func in metodos_compressao.items():
            tabela, colisoes = preencher_tabela(h_func, c_func)
            resultados[(h_name, c_name)] = colisoes
            print(f"Hash: {h_name}, Compressão: {c_name}, Colisões: {colisoes}")
    
    return resultados

if __name__ == "__main__":
    resultados = testar_metodos()
