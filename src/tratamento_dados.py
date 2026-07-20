import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Função para inspeção inicial de dados.
def tratar_dados(df):

    n_inicial = len(df)
    relatorio = {}

    # Remoção de registros duplicados
    n_duplicados = df.duplicated().sum()

    df = df.drop_duplicates()

    relatorio["duplicados_encontrados"] = n_duplicados
    relatorio["duplicados_removidos"] = n_duplicados


    # Identificação de valores ausentes
    valores_nulos = df.isnull().sum()

    relatorio["valores_nulos_iniciais"] = (
        valores_nulos[valores_nulos > 0].to_dict()
    )


    # Tratamento de valores ausentes
    # Utilizando mediana devido à presença de possíveis outliers

    colunas_numericas = df.select_dtypes(
        include=["int64", "float64"]
    ).columns


    for coluna in colunas_numericas:

        quantidade_nulos = df[coluna].isnull().sum()

        if quantidade_nulos > 0:

            df[coluna] = df[coluna].fillna(
                df[coluna].median()
            )

            relatorio[f"{coluna}_nulos_tratados"] = quantidade_nulos


    # Verificação final
    nulos_finais = df.isnull().sum()

    relatorio["valores_nulos_finais"] = (
        nulos_finais[nulos_finais > 0].to_dict()
    )


    n_final = len(df)

    relatorio["registros_iniciais"] = n_inicial
    relatorio["registros_finais"] = n_final
    relatorio["registros_removidos_total"] = (
        n_inicial - n_final
    )


    # Relatório de tratamento
    print(
        "\n" + "=" * 30 +
        " RELATÓRIO DE TRATAMENTO DE DADOS " +
        "=" * 30
    )

    for chave, valor in relatorio.items():
        print(f"{chave}: {valor}")


    return df, relatorio

def gerar_boxplots(df):

    variaveis = [
        "temperatura_ar_k",
        "temperatura_processo_k",
        "velocidade_rotacao_rpm",
        "torque_nm",
        "desgaste_ferramenta_min"
    ]

    fig, axes = plt.subplots(3, 2, figsize=(12, 10))
    axes = axes.flatten()

    for i, coluna in enumerate(variaveis):
        sns.boxplot(y=df[coluna], ax=axes[i])
        axes[i].set_title(coluna)

    for j in range(len(variaveis), len(axes)):
        fig.delaxes(axes[j])

    plt.tight_layout()

    plt.savefig(
        "../images/boxplots_variaveis.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()