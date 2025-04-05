
# Teste de Nivelamento v.250321 - Solução Completa

Este repositório contém a solução para o processo seletivo técnico que envolve Web Scraping, Transformação de Dados, Banco de Dados e Desenvolvimento de API com interface web. As tarefas foram divididas em quatro etapas, cada uma atendendo aos requisitos especificados no documento oficial da seleção.

---

## ✨ Etapas Realizadas

### 1. 🕷️ Web Scraping

- Acesso automático ao site da ANS:
  - https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos
- Download dos arquivos PDF dos Anexos I e II.
- Compactação dos arquivos em formato `.zip`.

📁 Caminho: `web_scraping/`

---

### 2. 🔄 Transformação de Dados

- Extração da tabela completa do Anexo I (PDF).
- Salvamento dos dados em `.csv`.
- Substituição das siglas OD e AMB pelas descrições completas.
- Compactação do CSV em `Teste_GabrielaIsabel.zip`.

📁 Caminho: `transformacao_dados/`

---

### 3. 🧠 Banco de Dados

- Download dos dados financeiros dos últimos dois anos do repositório da ANS:
  - [Demonstrativos Contábeis](https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/)
  - [Dados Cadastrais das Operadoras Ativas](https://dadosabertos.ans.gov.br/FTP/PDA/operadoras_de_plano_de_saude_ativas/)
- Criação de estrutura de tabelas e importação via SQL.
- Consultas analíticas desenvolvidas em PostgreSQL, respondendo:
  - As 10 operadoras com maiores despesas com "EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS..." no último trimestre e no último ano.

📁 Caminho: `banco_de_dados/`

---

### 4. 🔎 API + Interface Web

- Desenvolvimento de servidor em Python para busca textual nos cadastros das operadoras.
- Interface em Vue.js conectada à API.
- Testes realizados com coleção no Postman.

📁 Caminhos:
- Backend: `backend/`
- Frontend (Vue): `frontend/`

---
