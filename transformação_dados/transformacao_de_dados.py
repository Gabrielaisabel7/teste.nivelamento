import pandas as pd
import pdfplumber
import zipfile
import os

# Caminho do arquivo PDF e nomes dos arquivos de saída
pdf_path = r"C:\Users\gabii\downloads\teste.nivelamento\downloads\Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf"
csv_filename = "Rol_de_Procedimentos.csv"
zip_filename = "Teste_Gabriela_Isabel.zip"

substituicoes = {
    "OD": "Odontológico",
    "AMB": "Ambulatorial"
}

def extrair_tabelas(pdf_path):
    """
    Extrai tabelas de um arquivo PDF e retorna uma lista de DataFrames.
    """
    tabelas = []
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                tables = page.extract_tables()
                for table in tables:
                    df = pd.DataFrame(table)
                    tabelas.append(df)
    except Exception as e:
        print(f"Erro ao extrair tabelas do PDF: {e}")
    return tabelas

def processar_tabelas(tabelas):
    """
    Processa as tabelas extraídas, limpando dados e aplicando substituições.
    Retorna um único DataFrame consolidado.
    """
    if not tabelas:
        print("Nenhuma tabela encontrada no PDF.")
        return pd.DataFrame() 

    df_final = pd.concat(tabelas, ignore_index=True)

    df_final = df_final.dropna(how='all')
    df_final = df_final.dropna(axis=1, how='all')

    df_final = df_final.fillna('') 
    for col in df_final.columns:
        df_final[col] = df_final[col].replace(substituicoes)

    return df_final

def salvar_csv(df, filename):
    """
    Salva o DataFrame processado em um arquivo CSV.
    """
    try:
        df.to_csv(filename, index=False, encoding='utf-8')
    except Exception as e:
        print(f"Erro ao salvar CSV: {e}")

def compactar_arquivo(csv_filename, zip_filename):
    """
    Compacta o arquivo CSV em um arquivo ZIP e remove o CSV original.
    """
    try:
        with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
            zipf.write(csv_filename, os.path.basename(csv_filename))
        os.remove(csv_filename)
    except Exception as e:
        print(f"Erro ao compactar arquivo: {e}")

# Execução do fluxo de processamento
tabelas_extraidas = extrair_tabelas(pdf_path)

if tabelas_extraidas:
    df_processado = processar_tabelas(tabelas_extraidas)
    
    if not df_processado.empty:
        salvar_csv(df_processado, csv_filename)
        compactar_arquivo(csv_filename, zip_filename)
        print(f"Processo concluído! Arquivo salvo como {zip_filename}")
    else:
        print("O DataFrame processado está vazio. Verifique o PDF.")
else:
    print("Nenhuma tabela foi extraída do PDF. Verifique o arquivo.")
