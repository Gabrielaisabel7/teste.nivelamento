# ✅ Testes de Nivelamento v.250321

Este repositório contém as soluções completas para o processo seletivo técnico de nivelamento, versão 250321. Todos os testes foram desenvolvidos utilizando **Python** e **Vue.js**, abordando desde web scraping até integração com banco de dados e construção de uma API funcional com interface web.

---

## 🧪 1. Teste de Web Scraping

### Linguagem utilizada: Python

- **1.1.** Acesso automatizado ao site da ANS:  
  `https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos`

- **1.2.** Download automático dos Anexos I e II em formato PDF.

- **1.3.** Compactação dos dois anexos em um único arquivo `.zip`.

📁 Arquivos gerados:
anexo_I.pdf | anexo_II.pdf | compactação_anexos.zip

---

## 🔁 2. Teste de Transformação de Dados

### Linguagem utilizada: Python

- **2.1.** Extração da tabela "Rol de Procedimentos e Eventos em Saúde" do PDF do Anexo I, em **todas as páginas**.
- **2.2.** Conversão da tabela em um `.csv` estruturado.
- **2.3.** Compactação do arquivo CSV em `Teste_GabrielaIsabel.zip`.
- **2.4.** Substituição de siglas:
  - `OD → Odontologia`
  - `AMB → Ambulatorial`

📁 Arquivos gerados:
rol_procedimentos.csv > Teste_GabrielaIsabel.zip.

---


---

## 🗃️ 3. Teste de Banco de Dados

### Linguagem: SQL (compatível com PostgreSQL 14+)

#### Tarefas de Preparação:

- **3.1.** Download dos arquivos dos últimos 2 anos do repositório:  
  https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/

- **3.2.** Download dos dados cadastrais das operadoras em:  
  https://dadosabertos.ans.gov.br/FTP/PDA/operadoras_de_plano_de_saude_ativas/

#### Tarefas de Código:

- **3.3.** Criação das tabelas com `CREATE TABLE` baseadas no CSV.
- **3.4.** Importação dos dados com `COPY FROM` e controle de encoding.
- **3.5.** Queries analíticas:

📌 **Consultas desenvolvidas:**
- Top 10 operadoras com maiores despesas em:
  - **Último trimestre**
  - **Último ano**

## 🚀 4. Teste de API REST

### 📌 Linguagens utilizadas: Python (FastAPI) e Vue.js

- **4.1.** Desenvolvimento de uma API REST para exposição dos dados transformados.
- **4.2.** Implementação de endpoints para:
  - Listagem de procedimentos.
  - Consulta detalhada por código de procedimento.
  - Filtros avançados por categoria (Odontológico, Ambulatorial).
- **4.3.** Integração com banco de dados PostgreSQL.

📌 **Principais endpoints:**

```http
GET /procedimentos
GET /procedimentos/{codigo}
GET /procedimentos?categoria=Odontológico
```

📁 **Arquivos gerados:**  
`backimportacao.py` | `indexvue.html`

---

## 🎨 5. Teste de Interface Web

### 📌 Linguagem utilizada: Vue.js

- **5.1.** Criação de uma interface web responsiva para consulta de procedimentos.
- **5.2.** Consumo da API REST para exibição dos dados em tempo real.
- **5.3.** Implementação de filtros e paginação dinâmica.

📌 **Recursos desenvolvidos:**  
✔️ Tabela dinâmica com ordenação e pesquisa.  
✔️ Filtros por tipo de procedimento.  
✔️ Interface adaptável para desktop e mobile.

📁 **Arquivos gerados:**  
`App.vue` | `Procedimentos.vue` | `api.js` | 

---

## 📌 6. Como Executar o Projeto

### 🔧 Requisitos

- Python 3.10+
- PostgreSQL 14+
- Node.js 18+

📌 **Desenvolvido por Gabriela Isabel C Silva**
📌 *Conteúdo confidencial e restrito*
---
