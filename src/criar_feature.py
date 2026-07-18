def criar_features(df):

    df = df.copy()

    df["potencia"] = (
        df["velocidade_rotacao_rpm"] *
        df["torque_nm"]
    )

    return df