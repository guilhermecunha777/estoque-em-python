import csv
import os
from repositories import produto_repository

def gerar_relatorio_cvs():
    produtos = produto_repository.listar_produtos()
    
    if not produtos:
        print("\n nenhum produto encontrado para gerar o relatorio.\n")
        return
    
    caminho_pasta = os.path.dirname(__file__)
    if not os.path.exists(caminho_pasta):
        os.makedirs(caminho_pasta)
    
    caminho_arquivo = os.path.join(caminho_pasta, "relatorios_estoque.csv")
    
    with open(caminho_arquivo, mode='w', newline='', encoding='utf-8') as arquivo_csv:
        writer = csv.writer(arquivo_csv)
        writer.writerow(["ID", "Nome", "Quantidade", "caminho da foto"])
    
        for produto in produtos:
            writer.writerow([produto.id, produto.nome, produto.quantidade, produto.caminho_foto])
    
    print(f"\n relatorio gerado com sucesso em: {caminho_arquivo}\n")
    