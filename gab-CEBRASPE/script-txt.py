import os
import pandas as pd

def extrair_dados_txt(nome_arquivo):
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo_txt:
        linhas = arquivo_txt.readlines()
        
        dados_prova = []
        nome_da_prova = None
        questao = None

        for linha in linhas:
            linha = linha.strip()

            # Verifica se a linha contém o nome da prova
            if "EDITAL" in linha:
                nome_da_prova = linha
                print(f"Nome da prova: {nome_da_prova}")
            
            # Verifica se a linha é um número (representando uma questão)
            elif linha.isdigit():
                questao = int(linha)
            
            # Se a linha não for um número, considera como a resposta
            else:
                resposta = linha
                if questao is not None:
                    dados_prova.append({"Questão": questao, "Resposta": resposta})
                    print(f"Questão: {questao}, Resposta: {resposta}")

        return nome_da_prova, dados_prova

def criar_planilha(nome_arquivo, dados_prova):
    df = pd.DataFrame(dados_prova)
    nome_planilha = "analise_dados.xlsx"
    df.to_excel(nome_planilha, index=False)
    print(f"Os dados foram salvos em {nome_planilha}")

if __name__ == "__main__":
    nome_arquivo = "BANRISUL_001_003_01-GAB.txt"  # Substitua pelo nome do arquivo de texto
    nome_da_prova, dados_prova = extrair_dados_txt(nome_arquivo)
    criar_planilha(nome_arquivo, dados_prova)
