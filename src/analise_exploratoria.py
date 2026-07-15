import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Função para inspeção inicial de dados.

def inspecionar_dados(df):
    
    print("\n" + "=" * 30 + " Inspeção Inicial dos Dados " + "=" * 30)
    df.info()
    print("\n" + "=" * 30 + " Tamanho do Dataset " + "=" * 30 + f"\n{df.shape}")
    print("\n" + "=" * 30 + " Colunas do Dataset " + "=" * 30 + f"\n{list(df.columns)}")
    print("\n" + "=" * 30 + " Estatísticas do Dataset " + "=" * 30 + f"\n{df.describe()}")
    print("\n" + "=" * 30 + " Valores Nulos " + "=" * 30 + f"\n{df.isnull().sum()}")
    print("\n" + "=" * 30 + " Fim da Inspeção Inicial dos Dados " + "=" * 30 + "\n")

def grafico_distribuicao_falhas(df):

    plt.figure(figsize=(8,5))

    sns.countplot(
        data=df,
        x="falha_maquina"
    )

    plt.title("Distribuição da Ocorrência de Falhas")
    plt.xlabel("Falha da Máquina (0 = Normal / 1 = Falha)")
    plt.ylabel("Quantidade de registros")

    plt.savefig(
        "../images/distribuicao_falhas.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()



def grafico_distribuicao_variaveis(df):

    variaveis = [
        "temperatura_ar_k",
        "temperatura_processo_k",
        "velocidade_rotacao_rpm",
        "torque_nm",
        "desgaste_ferramenta_min"
    ]

    df[variaveis].hist(
        figsize=(12,8),
        bins=30
    )

    plt.suptitle("Distribuição das Variáveis Operacionais")

    plt.savefig(
        "../images/distribuicao_variaveis.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()

def grafico_correlacao(df):

    variaveis_numericas = df.select_dtypes(
        include=["int64", "float64"]
    )

    plt.figure(figsize=(12,8))

    sns.heatmap(
        variaveis_numericas.corr(),
        annot=True,
        cmap="coolwarm",
        fmt=".2f"
    )

    plt.title("Mapa de Correlação de Pearson")

    plt.savefig(
        "../images/correlacao_pearson.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()