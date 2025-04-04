-- Consulta 1: Top 10 operadoras com maiores despesas no último trimestre
SELECT 
    dc.registro_ans,  
    op.razao_social,
    SUM(dc.valor) AS total_despesas  
FROM demonstracoes_contabeis dc
JOIN operadoras op ON dc.registro_ans = op.Registro_ANS
WHERE TRIM(dc.descricao_conta_contabil) LIKE 'EVENTOS/SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE%'
AND dc.trimestre = (SELECT MAX(trimestre) FROM demonstracoes_contabeis WHERE ano = (SELECT MAX(ano) FROM demonstracoes_contabeis))  
AND dc.ano = (SELECT MAX(ano) FROM demonstracoes_contabeis)  
GROUP BY dc.registro_ans, op.razao_social  
ORDER BY total_despesas DESC  
LIMIT 10;

-- Consulta 2: Top 10 operadoras com maiores despesas no último ano
SELECT 
    dc.registro_ans,  
    op.razao_social,
    SUM(dc.valor) AS total_despesas  
FROM demonstracoes_contabeis dc  
JOIN operadoras op ON dc.registro_ans = op.Registro_ANS
WHERE TRIM(dc.descricao_conta_contabil) IN (
    'EVENTOS/SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA À SAÚDE',
    'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR',
    'VARIAÇÃO DA PROVISÃO DE EVENTOS/SINISTROS OCORRIDOS E NÃO AVISADOS DE ASSISTÊNCIA A SAÚDE'
)  
AND dc.ano = (SELECT MAX(ano) FROM demonstracoes_contabeis)  
GROUP BY dc.registro_ans, op.razao_social  
ORDER BY total_despesas DESC  
LIMIT 10;


