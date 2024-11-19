# Projeto: Download de Imagens a Partir de Dados JSON

Este projeto é um script em Python que processa arquivos JSON para extrair URLs de imagens e baixá-las para uma pasta local. Ele foi projetado para facilitar a automação de downloads em massa de imagens organizadas em JSON.

---

## Funcionalidades

1. **Leitura de Arquivos JSON**  
   O script lê arquivos JSON para encontrar URLs de imagens.

2. **Download de Imagens**  
   Baixa imagens das URLs encontradas no JSON, salvando-as localmente.

3. **Criação Automática de Pastas**  
   Garante que a pasta de destino para as imagens seja criada, caso não exista.

4. **Processamento de Múltiplos Arquivos**  
   Suporta o processamento de diversos arquivos JSON em uma única execução.

---

## Estrutura do JSON Esperado

O script foi desenvolvido para trabalhar com JSON no seguinte formato:

```json
[
  {
    "fotos": [
      {
        "path": {
          "full": "https://example.com/image1.jpg"
        }
      },
      {
        "path": {
          "full": "https://example.com/image2.jpg"
        }
      }
    ]
  },
  {
    "fotos": [
      {
        "path": {
          "full": "https://example.com/image3.jpg"
        }
      }
    ]
  }
]
```

Cada entrada no JSON pode conter um array de objetos `fotos`, cada um com um campo `path.full` contendo a URL da imagem.

---

## Requisitos

### Bibliotecas Necessárias
O script utiliza as seguintes bibliotecas padrão e externas:
- **json**: Para manipulação de arquivos JSON.
- **requests**: Para realizar requisições HTTP.
- **os**: Para manipulação do sistema de arquivos.

Certifique-se de que a biblioteca `requests` esteja instalada:
```bash
pip install requests
```

---

## Como Usar

1. **Organize seus arquivos JSON**  
   Insira os arquivos JSON (como `arquivo01.json`, `arquivo02.json`, etc.) na mesma pasta do script.

2. **Defina o destino das imagens**  
   Por padrão, as imagens serão salvas na pasta `imagens`. Você pode alterar a variável `pasta_destino` no código, se necessário.

3. **Execute o script**  
   Execute o script em seu terminal ou ambiente de desenvolvimento:
   ```bash
   python script.py
   ```

---

## Estrutura do Código

1. **Função `baixar_imagem(url, pasta_destino)`**  
   - Baixa a imagem de uma URL.
   - Salva a imagem na pasta especificada.
   - Exibe mensagens de sucesso ou erro.

2. **Função `processar_json(arquivo_json, pasta_destino)`**  
   - Lê o arquivo JSON.
   - Itera sobre as entradas, localizando URLs no campo `path.full`.
   - Chama a função `baixar_imagem` para cada URL encontrada.

3. **Execução Principal**  
   - Cria a pasta de destino, se necessário.
   - Processa múltiplos arquivos JSON sequencialmente.

---

## Exemplo de Saída

Ao executar o script, o terminal exibirá mensagens como:

```
Imagem baixada e salva como imagens/image1.jpg
Imagem baixada e salva como imagens/image2.jpg
https://example.com/image1.jpg
https://example.com/image2.jpg
```

Se houver falha no download de uma imagem:

```
Erro ao baixar a imagem: https://example.com/image404.jpg (Status: 404)
```

---

## Possíveis Melhorias

1. **Tratamento de Erros**  
   - Implementar um mecanismo para continuar a execução mesmo em caso de falha em algum download.

2. **Personalização de Nome de Arquivos**  
   - Adicionar opções para salvar imagens com nomes customizados.

3. **Logs Detalhados**  
   - Salvar logs em um arquivo para análise posterior.

4. **Execução Paralela**  
   - Utilizar bibliotecas como `concurrent.futures` para baixar imagens de forma assíncrona.

---
