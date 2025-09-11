import json
from deep_translator import GoogleTranslator

def traduzir_notebook_markdown(entrada, saida, target="pt"):
    # Carregar notebook
    with open(entrada, "r", encoding="utf-8") as f:
        notebook = json.load(f)

    tradutor = GoogleTranslator(source="auto", target=target)

    # Percorrer as células
    for cell in notebook.get("cells", []):
        if cell.get("cell_type") == "markdown":
            novo_source = []
            for linha in cell.get("source", []):
                try:
                    if linha.strip():  # evita traduzir linhas em branco
                        traducao = tradutor.translate(linha)
                        novo_source.append(traducao + "\n")
                    else:
                        novo_source.append("\n")
                except Exception as e:
                    print(f"Erro ao traduzir linha: {e}")
                    novo_source.append(linha)
            cell["source"] = novo_source

    # Salvar novo arquivo
    with open(saida, "w", encoding="utf-8") as f:
        json.dump(notebook, f, ensure_ascii=False, indent=2)

    print(f"✅ Tradução concluída! Arquivo salvo em: {saida}")


if __name__ == "__main__":
    traduzir_notebook_markdown("C:/Users/ead/python_developer_qua491006/dados/03_projeto_kaggle/serial-murder-analysis.ipynb",
                                "C:/Users/ead/python_developer_qua491006/dados/03_projeto_kaggle/serial-murder-analysis_traduzido.ipynb")
