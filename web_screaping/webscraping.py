import os
import requests
from bs4 import BeautifulSoup
import zipfile
import concurrent.futures
from urllib.parse import urljoin

# URL de origem dos PDFs
url = 'https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos'

def fetch_page(url):
    """Realiza a requisição HTTP para obter o conteúdo da página."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        print("Requisição bem-sucedida!")
        return response
    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar a URL: {e}")
        return None

def download_pdf(pdf_link):
    """Baixa um arquivo PDF a partir de um link."""
    try:
        pdf_name = pdf_link.split('/')[-1]
        pdf_path = os.path.join('downloads', pdf_name)
        
        pdf_response = requests.get(pdf_link)
        pdf_response.raise_for_status()
        
        with open(pdf_path, 'wb') as f:
            f.write(pdf_response.content)
        
        print(f"PDF {pdf_name} baixado com sucesso!")
        return pdf_path
    except requests.exceptions.RequestException as e:
        print(f"Erro ao baixar o PDF {pdf_link}: {e}")
        return None

def create_zip(zip_path):
    """Compacta todos os arquivos da pasta 'downloads' em um arquivo ZIP."""
    try:
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for pdf in os.listdir('downloads'):
                pdf_file_path = os.path.join('downloads', pdf)
                zipf.write(pdf_file_path, os.path.basename(pdf_file_path))
        print(f"Arquivos compactados em {zip_path}")
        return True
    except Exception as e:
        print(f"Erro ao criar o ZIP: {e}")
        return False

def main():
    """Função principal para buscar PDFs, baixá-los e compactá-los."""
    response = fetch_page(url)
    if not response:
        return
    
    soup = BeautifulSoup(response.text, 'html.parser')
    links_pdfs = []
    
    for a in soup.find_all('a', href=True):
        href = a['href']
        if 'Anexo' in a.text and href.endswith('.pdf'):
            pdf_link = urljoin(url, href)
            links_pdfs.append(pdf_link)
    
    if not links_pdfs:
        print("Nenhum PDF foi identificado corretamente.")
        return
    
    if not os.path.exists('downloads'):
        os.makedirs('downloads')
        print("\nCriando pasta 'downloads'.")
    
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(download_pdf, link) for link in links_pdfs]
        downloaded_pdfs = [future.result() for future in futures if future.result() is not None]
    
    zip_path = "Compactacao_anexos.zip"
    if downloaded_pdfs:
        if create_zip(zip_path):
            with zipfile.ZipFile(zip_path, 'r') as zipf:
                zip_content = zipf.namelist()
                print("\nConteúdo do ZIP:")
                for item in zip_content:
                    print(f"- {item}")
        else:
            print("\nErro ao compactar os arquivos.")
    else:
        print("\nNenhum PDF foi baixado, não há arquivos para compactar.")

if __name__ == "__main__":
    main()
