def converter(letra):
    maiusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    minusculas = "abcdefghijklmnopqrstuvwxyz"
    
    for i in range(26):
        if maiusculas[i] == letra:
            return minusculas[i]
    
    return letra

def substring(texto, busca):
    tam_texto = 0
    for c in texto:
        tam_texto = tam_texto + 1
        
    tam_busca = 0
    for c in busca:
        tam_busca = tam_busca + 1
        
    if tam_busca > tam_texto:
        return False
        
    limite = tam_texto - tam_busca + 1
    
    for i in range(limite):
        match = True
        for j in range(tam_busca):
            char_texto = converter(texto[i + j])
            char_busca = converter(busca[j])
            
            if char_texto != char_busca:
                match = False
                break
        
        if match:
            return True
            
    return False

biblioteca = []

for i in range(5):
    titulo = input()
    autor = input()
    ano = int(input())
    
    livro = {}
    livro['titulo'] = titulo
    livro['autor'] = autor
    livro['ano'] = ano
    
    biblioteca.append(livro)
    
termo_busca = input()

for livro in biblioteca:
    if substring(livro['titulo'], termo_busca):
        print(livro)
