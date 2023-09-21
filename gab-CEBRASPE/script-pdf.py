    # nome_arquivo = "BANRISUL_001_003_01-GAB.PDF"  # Substitua pelo nome do arquivo PDF
import PyPDF2
import os
import pandas as pd

def extrair_dados_pdf(nome_arquivo):
    # Abre o arquivo PDF
    with open(nome_arquivo, 'rb') as arquivo_pdf:
        leitor_pdf = PyPDF2.PdfReader(arquivo_pdf)
        
        # Inicializa variáveis para armazenar os dados
        dados_prova = []
        nome_da_prova = None

        # Percorre as páginas do PDF
        for pagina_num, pagina in enumerate(leitor_pdf.pages):
            texto = pagina.extract_text()
            
            print(f"=== Página {pagina_num + 1} ===")
            print(texto)

            # Verifica se a página contém o nome da prova
            if "EDITAL" in texto:
                nome_da_prova = texto.strip()
                print(f"Nome da prova: {nome_da_prova}")

            # Divide o texto em partes com base em quebras de linha
            partes = texto.split("\n")
            for parte in partes:
                parte = parte.strip()
                if parte:
                    if parte.isdigit():
                        questao = int(parte)
                    else:
                        resposta = parte
                        dados_prova.append({"Questão": questao, "Resposta": resposta})
                        print(f"Questão: {questao}, Resposta: {resposta}")

        return nome_da_prova, dados_prova

def criar_planilha(nome_arquivo, dados_prova):
    # Cria um DataFrame com os dados da prova
    df = pd.DataFrame(dados_prova)

    # Define o nome da planilha
    nome_planilha = "analise_dados.xlsx"

    # Salva os dados em uma planilha Excel
    df.to_excel(nome_planilha, index=False)

    print(f"Os dados foram salvos em {nome_planilha}")

if __name__ == "__main__":
    nome_arquivo = "BANRISUL_001_003_01-GAB.PDF"  # Substitua pelo nome do arquivo PDF
    nome_da_prova, dados_prova = extrair_dados_pdf(nome_arquivo)
    criar_planilha(nome_da_prova, dados_prova)
