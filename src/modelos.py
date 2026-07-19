from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import pandas as pd

# Função para testar o modelo KNN
def testar_knn(X_train, X_test, y_train, y_test):

    valores_k = [3, 5, 7]

    resultados = []

    for k in valores_k:

        modelo = KNeighborsClassifier(
            n_neighbors=k
        )

        modelo.fit(
            X_train,
            y_train
        )

        previsao_treino = modelo.predict(
            X_train
        )

        previsao_teste = modelo.predict(
            X_test
        )

        acuracia_treino = accuracy_score(
            y_train,
            previsao_treino
        )

        acuracia_teste = accuracy_score(
            y_test,
            previsao_teste
        )

        resultados.append(
            {
                "modelo": "KNN",
                "k": k,
                "acuracia_treino": acuracia_treino,
                "acuracia_teste": acuracia_teste
            }
        )

    return pd.DataFrame(resultados)


# Função para testar o modelo de Árvore de Decisão
def testar_arvore(X_train, X_test, y_train, y_test):

    valores_depth = [3, 5, None]

    resultados = []

    for depth in valores_depth:

        modelo = DecisionTreeClassifier(
            max_depth=depth,
            random_state=42
        )

        modelo.fit(
            X_train,
            y_train
        )

        previsao_treino = modelo.predict(
            X_train
        )

        previsao_teste = modelo.predict(
            X_test
        )

        acuracia_treino = accuracy_score(
            y_train,
            previsao_treino
        )

        acuracia_teste = accuracy_score(
            y_test,
            previsao_teste
        )

        resultados.append(
            {
                "modelo": "Árvore de Decisão",
                "max_depth": depth,
                "acuracia_treino": acuracia_treino,
                "acuracia_teste": acuracia_teste
            }
        )

    return pd.DataFrame(resultados)