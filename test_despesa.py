import os
from despensa import adicionar_alimento

def salvar_arquivo_de_texto():
    arquivo_teste = "teste.txt"
    
    # Garante que o arquivo de teste não existe antes de começar
    if os.path.exists(arquivo_teste):
        os.remove(arquivo_teste)
        
    # Executa a função
    adicionar_alimento("Feijao", 10, arquivo_teste)
    
    # Lê o arquivo para ver se funcionou
    with open(arquivo_teste, "r", encoding="utf-8") as f:
        conteudo = f.read()
        
    # Verifica se o texto está lá
    assert "Feijao,10" in conteudo
    
    # Apaga o arquivo de teste para deixar tudo limpo
    os.remove(arquivo_teste)