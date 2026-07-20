import pandas as pd

# Função para carregar o dataset a partir de um arquivo CSV com tratamento de erros.
def carregar_dataset(caminho):

    try: 
        return pd.read_csv(caminho)
    
    except FileNotFoundError:
        raise FileNotFoundError(f" O arquivo '{caminho}' não foi encontrado. Verifique se o caminho está correto.")
    
    except Exception as error:
        raise Exception(f"Ocorreu um erro ao carregar o dataset: {error}")