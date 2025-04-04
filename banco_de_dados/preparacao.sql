-- Removendo possíveis duplicatas (versão otimizada para MySQL)
DELETE o FROM operadoras o
JOIN (
    SELECT Registro_ANS, MIN(ROWID) AS min_id
    FROM (
        SELECT Registro_ANS, ROW_NUMBER() OVER(PARTITION BY Registro_ANS ORDER BY Registro_ANS) AS row_num, ROWID
        FROM operadoras
    ) AS temp
    GROUP BY Registro_ANS
) AS dup ON o.Registro_ANS = dup.Registro_ANS
WHERE o.ROWID > dup.min_id;