import json
import requests
import os

def baixar_imagem(url, pasta_destino):
    response = requests.get(url)
    if response.status_code == 200:
        nome_arquivo = os.path.join(pasta_destino, os.path.basename(url))
        with open(nome_arquivo, 'wb') as file:
            file.write(response.content)
        print(f"Imagem baixada e salva como {nome_arquivo}")
    else:
        print(f"Erro ao baixar a imagem: {url} (Status: {response.status_code})")

def processar_json(arquivo_json, pasta_destino):
    with open(arquivo_json, 'r') as arquivo:
        dados = json.load(arquivo)
    for e in dados:
        for path in e.get('fotos', []):
            url = path.get('path', {}).get('full')
            if url:
                baixar_imagem(url, pasta_destino)
                print(url)

pasta_destino = "imagens"
os.makedirs(pasta_destino, exist_ok=True)

for arquivo_json in ['arquivo01.json', 'arquivo02.json']:
    processar_json(arquivo_json, pasta_destino)