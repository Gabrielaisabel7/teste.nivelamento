from flask import Flask, jsonify, request
import pandas as pd
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Carrega o CSV e verifica as colunas disponíveis
df = pd.read_csv('C:/Users/gabii/Downloads/teste.nivelamento/banco_de_dados/dados/operadoras.csv', sep=';')
print("Colunas do CSV:", df.columns)
print(df.head())

df['Razao_Social'] = df['Razao_Social'].astype(str)
df['Cidade'] = df['Cidade'].astype(str)
df['UF'] = df['UF'].astype(str)

@app.route('/')
def home():
    return "Servidor Flask rodando com sucesso!"

@app.route('/buscar')
def buscar_operadoras():
    query = request.args.get('q', '').lower().strip()
    
    if not query:
        return jsonify({"erro": "Nenhum termo de busca foi fornecido."}), 400

    if 'Razao_Social' not in df.columns:
        return jsonify({"erro": "Coluna 'Razao_Social' não encontrada no CSV."}), 500
    
    resultados = df[df['Razao_Social'].str.lower().str.contains(query, na=False)]
    
    if resultados.empty:
        return jsonify({"mensagem": "Nenhum resultado encontrado."})
    
    print("Resultados da busca:", resultados[['Razao_Social', 'Cidade', 'UF']])
    
    return jsonify(resultados[['Razao_Social', 'Cidade', 'UF']].to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)
