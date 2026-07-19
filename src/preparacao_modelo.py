import pandas as pd
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE
from sklearn.preprocessing import StandardScaler

# Função para separar as variáveis independentes (X) da variável dependente (y).
def separar_variaveis(df):

    colunas_remover = [
        "falha_maquina",
        "falha_twf",
        "falha_hdf",
        "falha_pwf",
        "falha_osf",
        "falha_rnf"
    ]

    X = df.drop(
        columns=colunas_remover
    )

    y = df["falha_maquina"]

    return X, y

# Função para preparar as variáveis categóricas.
def preparar_variaveis_categoricas(X):

    X = X.copy()

    X = X.drop(
        "id_produto",
        axis=1
    )

    X = pd.get_dummies(
        X,
        columns=["tipo"],
        drop_first=True
    )

    colunas_booleanas = X.select_dtypes(
        include="bool"
    ).columns

    X[colunas_booleanas] = X[colunas_booleanas].astype(int)

    return X

# Função para dividir os dados em conjuntos de treino e teste.
def dividir_dados(X, y):

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    return X_train, X_test, y_train, y_test


# Função para aplicar o SMOTE e balancear as classes do conjunto de treino.
def aplicar_smote(X_train, y_train):

    smote = SMOTE(
        random_state=42
    )

    X_train_balanceado, y_train_balanceado = smote.fit_resample(
        X_train,
        y_train
    )

    return X_train_balanceado, y_train_balanceado

# Função para aplicar o StandardScaler nas variáveis do modelo KNN.
def escalonar_variaveis(X_train, X_test):

    scaler = StandardScaler()

    X_train_escalonado = scaler.fit_transform(
        X_train
    )

    X_test_escalonado = scaler.transform(
        X_test
    )

    return X_train_escalonado, X_test_escalonado