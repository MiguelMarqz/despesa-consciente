import os

def adicionar_alimento(nome, dias_restantes, nome_arquivo="despensa.txt"):
    """Salva o alimento e os dias para vencer em um arquivo de texto (.txt)."""
    # O modo "a" (append) adiciona o texto no final do arquivo sem apagar o resto
    with open(nome_arquivo, "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{nome},{dias_restantes}\n")

def checar_vencimentos(nome_arquivo="despensa.txt"):
    """Lê o arquivo de texto e avisa o que está perto de vencer."""
    if not os.path.exists(nome_arquivo):
        print("Sua despensa está vazia!\n")
        return

    print("\n--- STATUS DA DESPENSA ---")
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            linha = linha.strip() # Remove espaços e quebras de linha
            if linha: # Se a linha não estiver vazia
                nome, dias = linha.split(",")
                dias = int(dias)
                
                if dias <= 7:
                    print(f"⚠️ URGENTE: '{nome}' vence em {dias} dias!")
                else:
                    print(f"✅ TRANQUILO: '{nome}' ainda tem {dias} dias.")
    print("--------------------------\n")

def menu():
    """Mostra as opções na tela para o usuário."""
    while True:
        print("=== CONTROLE DE DESPENSA ===")
        print("1. Adicionar alimento")
        print("2. Ver o que está vencendo")
        print("3. Sair")
        
        opcao = input("Escolha (1, 2 ou 3): ")

        if opcao == "1":
            nome = input("O que você comprou? (ex: Leite): ")
            dias = input("Faltam quantos dias para vencer?: ")
            adicionar_alimento(nome, dias)
            print("Salvo com sucesso!\n")

        elif opcao == "2":
            checar_vencimentos()

        elif opcao == "3":
            print("Tchau! Evite o desperdício!")
            break
            
        else:
            print("Opção errada. Tente de novo.\n")

if __name__ == "__main__":
    menu()