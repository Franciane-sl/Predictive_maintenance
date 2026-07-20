# Predictive Maintenance

Projeto de classificação de falhas em máquinas industriais utilizando algoritmos de Machine Learning.

## Descrição

Sistema preditivo desenvolvido para identificar possíveis falhas em máquinas industriais utilizando dados de sensores operacionais.

O projeto aplica técnicas de análise de dados e aprendizado de máquina para classificar a ocorrência de falhas, utilizando os algoritmos:

- KNN (K-Nearest Neighbors)
- Árvore de Decisão

O objetivo é identificar o modelo com melhor desempenho para auxiliar na manutenção preditiva dos equipamentos.

---

# Dataset

O dataset utilizado contém **10.000 registros** de equipamentos industriais.

As principais variáveis utilizadas são:

| Variável | Descrição |
|---|---|
| tipo | Tipo de máquina (L, M, H) |
| temperatura_ar_k | Temperatura do ar em Kelvin |
| temperatura_processo_k | Temperatura do processo em Kelvin |
| velocidade_rotacao_rpm | Velocidade de rotação em RPM |
| torque_nm | Torque aplicado em Nm |
| desgaste_ferramenta_min | Tempo de desgaste da ferramenta em minutos |
| falha_maquina | Variável alvo: 0 (sem falha) ou 1 (com falha) |

---

# Estrutura do Projeto

```
Predictive_Maintenance/

├── data/
│   ├── manutencao_preditiva.csv
│   └── manutencao_preditiva_tratado.csv
│
├── models/
│   └── modelo_arvore.pkl
│
├── notebooks/
│   └── manutencao_preditiva.ipynb
│
├── src/
│   ├── carregamento.py
│   ├── tratamento.py
│   ├── preparacao_modelo.py
│   └── modelos.py
│
├── images/
│
└── requirements.txt
```

---

# Instalação

## Requisitos

- Python 3.8+
- pip

Instale as dependências do projeto:

```bash
pip install -r requirements.txt
```

## Dependências utilizadas

```
pandas
numpy
matplotlib
seaborn
scikit-learn
imbalanced-learn
joblib
```

---

# Como executar

O projeto foi desenvolvido utilizando Jupyter Notebook.

Execute:

```bash
jupyter notebook
```

Abra o notebook localizado na pasta:

```
notebooks/
```

Execute as células em sequência para reproduzir todo o pipeline de Machine Learning.

---

# Pipeline do Projeto

O desenvolvimento foi dividido nas seguintes etapas:

## Fase 1 - Análise e Tratamento dos Dados

Foram realizadas análises iniciais para verificar a qualidade dos dados.

Processos realizados:

- inspeção da estrutura do dataset;
- identificação de valores ausentes;
- tratamento de inconsistências;
- validação da qualidade dos dados.

---

## Fase 2 - Preparação dos Dados

Foram realizadas as seguintes etapas:

- separação das variáveis preditoras e variável alvo;
- remoção de colunas não utilizadas no treinamento;
- transformação das variáveis categóricas;
- preparação dos dados para os modelos de Machine Learning.

---

## Fase 3 - Feature Engineering

Foi criada uma nova variável chamada:

```
potencia
```

A variável foi gerada através da combinação das informações:

```
velocidade_rotacao_rpm * torque_nm
```

Essa nova característica representa uma informação adicional sobre o funcionamento dos equipamentos e pode auxiliar os modelos na identificação de padrões relacionados às falhas.

---

## Fase 4 - Divisão e Balanceamento dos Dados

Os dados foram separados em:

- variáveis preditoras (X);
- variável alvo (y).

A divisão entre treino e teste foi realizada utilizando:

```
stratify=y
```

mantendo a proporção das classes entre os conjuntos.

Após a divisão, foi aplicado:

```
SMOTE
```

somente nos dados de treinamento para balancear as classes e evitar vazamento de informações entre treino e teste.

---

## Fase 5 - Escalonamento das Variáveis

Foi aplicado o método:

```
StandardScaler
```

nas variáveis destinadas ao modelo KNN.

O processo utilizou:

- `fit_transform()` nos dados de treino;
- `transform()` nos dados de teste.

A Árvore de Decisão não utilizou escalonamento, pois o algoritmo realiza divisões baseadas em regras de decisão e não depende da escala dos atributos.

---

## Fase 6 - Ajuste de Parâmetros e Combate ao Overfitting

Foram avaliadas diferentes configurações dos modelos.

### KNN

Parâmetro analisado:

```
n_neighbors
```

Valores testados:

- K = 3
- K = 5
- K = 7

### Árvore de Decisão

Parâmetro analisado:

```
max_depth
```

Valores testados:

- max_depth = 3
- max_depth = 5
- max_depth = None

A análise comparou a acurácia nos dados de treino e teste para identificar possíveis sinais de overfitting.

---

# Resultados dos Modelos

Após os testes realizados com os dados de teste:

| Modelo | Configuração | Acurácia Teste |
|---|---|---|
| KNN | K = 3 | 92,6% |
| Árvore de Decisão | max_depth = None | 94,8% |

---

# Modelo Final Escolhido

A **Árvore de Decisão** foi escolhida como modelo final por apresentar o melhor desempenho no conjunto de teste.

Resultado obtido:

```
Acurácia: 94,8%
```

O modelo final treinado foi salvo em:

```
models/modelo_arvore.pkl
```

---

# Arquivos Importantes

| Arquivo | Descrição |
|---|---|
| data/manutencao_preditiva.csv | Dataset original |
| data/manutencao_preditiva_tratado.csv | Dataset após tratamento e engenharia de features |
| models/modelo_arvore.pkl | Modelo final treinado |
| notebooks/ | Notebook com todas as etapas do projeto |
| src/ | Funções utilizadas no pipeline |
| requirements.txt | Dependências do projeto |

---

# Boas Práticas Aplicadas

- Organização do projeto utilizando separação entre dados, código e modelos;
- Uso de funções para modularização do pipeline;
- Tratamento e validação dos dados;
- Engenharia de Features;
- Divisão treino/teste com estratificação;
- Aplicação do SMOTE somente no conjunto de treino;
- Prevenção de Data Leakage;
- Comparação entre diferentes modelos;
- Salvamento do modelo final treinado.

---

# Autora

Projeto desenvolvido por:

**Franciane Schier Leite**