-- Importação dos dados para a tabela "operadoras" a partir de um arquivo CSV  
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Relatorio_cadop.csv'  
INTO TABLE operadoras  
FIELDS TERMINATED BY ';'
ENCLOSED BY '"' 
LINES TERMINATED BY '\n' 
IGNORE 1 LINES; 

-- Importação dos dados para a tabela "demonstracoes_contabeis" a partir de um arquivo CSV  
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/demonstracoes.contabeis.csv'  
INTO TABLE demonstracoes_contabeis  
FIELDS TERMINATED BY ';' 
ENCLOSED BY '"' 
LINES TERMINATED BY '\n'
IGNORE 1 LINES  
(@DATA, registro_ans, codigo_conta_contabil, @descricao, @VL_SALDO_INICIAL, @VALOR)  
SET  
    data_competencia = STR_TO_DATE(@DATA, '%Y-%m-%d'), 
    trimestre        = QUARTER(STR_TO_DATE(@DATA, '%Y-%m-%d')),
    ano             = YEAR(STR_TO_DATE(@DATA, '%Y-%m-%d')),
    descricao_conta_contabil = TRIM(@descricao),
    valor           = REPLACE(@VALOR, ',', '.'),
    created_at      = NOW(); 
