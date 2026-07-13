
# Função para inspeção inicial de dados.

def inspecionar_dados(df):
    
    print("\n" + "=" * 30 + " Inspeção Inicial dos Dados " + "=" * 30)
    df.info()
    print("\n" + "=" * 30 + " Tamanho do Dataset " + "=" * 30 + f"\n{df.shape}")
    print("\n" + "=" * 30 + " Colunas do Dataset " + "=" * 30 + f"\n{list(df.columns)}")
    print("\n" + "=" * 30 + " Estatísticas do Dataset " + "=" * 30 + f"\n{df.describe()}")
    print("\n" + "=" * 30 + " Valores Nulos " + "=" * 30 + f"\n{df.isnull().sum()}")
    print("\n" + "=" * 30 + " Fim da Inspeção Inicial dos Dados " + "=" * 30 + "\n")
