import json
from deep_translator import GoogleTranslator

def traduzir_markdown_do_notebook(caminho_arquivo):
    try:
        # Carrega o notebook
        with open(caminho_arquivo, 'r', encoding='utf-8') as f:
            notebook = json.load(f)

        # Inicializa o tradutor
        tradutor = GoogleTranslator(source='auto', target='pt')

        # Percorre todas as células
        for celula in notebook['cells']:
            if celula['cell_type'] == 'markdown':
                texto_original = ''.join(celula['source'])
                try:
                    texto_traduzido = tradutor.translate(texto_original)
                    celula['source'] = [texto_traduzido]
                except Exception as e:
                    print(f"Erro ao traduzir célula: {e}")

        # Salva o notebook traduzido
        nome_traduzido = caminho_arquivo.replace(".ipynb", "_traduzido.ipynb")
        with open(nome_traduzido, 'w', encoding='utf-8') as f:
            json.dump(notebook, f, indent=2, ensure_ascii=False)

        print(f"Tradução concluída! Arquivo salvo como: {nome_traduzido}")

    except Exception as e:
        print(f"Erro ao processar o notebook: {e}")

# Exemplo de uso:
traduzir_markdown_do_notebook("serial-murder-analysis.ipynb")
