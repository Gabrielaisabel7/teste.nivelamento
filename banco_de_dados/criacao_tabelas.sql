-- Criação da tabela "operadoras" para armazenar informações das operadoras de planos de saúde
CREATE TABLE operadoras (
    Registro_ANS VARCHAR(20) PRIMARY KEY,  
    CNPJ VARCHAR(20) NOT NULL,
    Razao_Social VARCHAR(255) NOT NULL,
    Nome_Fantasia VARCHAR(255),
    Modalidade VARCHAR(100),
    Logradouro VARCHAR(255),
    Numero VARCHAR(10),
    Complemento VARCHAR(255),
    Bairro VARCHAR(100),
    Cidade VARCHAR(100),
    UF CHAR(2),
    CEP VARCHAR(10),
    DDD VARCHAR(5),
    Telefone VARCHAR(20),
    Fax VARCHAR(20),
    Endereco_eletronico VARCHAR(255),
    Representante VARCHAR(255),
    Cargo_Representante VARCHAR(255),
    Regiao_de_Comercializacao VARCHAR(255),
    Data_Registro_ANS DATE
);

-- Criação da tabela "demonstracoes_contabeis" para armazenar dados financeiros das operadoras
CREATE TABLE demonstracoes_contabeis (
    id INT AUTO_INCREMENT PRIMARY KEY, 
    registro_ans VARCHAR(20),
    codigo_conta_contabil VARCHAR(50),
    descricao_conta_contabil VARCHAR(255),
    valor DOUBLE,
    data_competencia DATE,
    trimestre INT,
    ano INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (registro_ans) REFERENCES operadoras(Registro_ANS)
);

-- Índices para otimizar consultas
CREATE INDEX idx_cnpj ON operadoras (CNPJ);
CREATE INDEX idx_contabeis ON demonstracoes_contabeis (registro_ans, ano, trimestre, descricao_conta_contabil);  

