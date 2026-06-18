import pandas as pd

# Leitura do score bruto

df = pd.read_csv(
    "data/processed/raw_penalty_score_players.csv"
)

# Ajuste suave pela taxa de conversão

df["conversion_factor"] = (
    0.7
    +
    (
        0.3
        *
        df["conversion_rate"]
    )
)

# Score final

df["final_score"] = (
    df["weighted_score"]
    *
    df["conversion_factor"]
)

# Ordena ranking

df = df.sort_values(
    by="final_score",
    ascending=False
)

# Salva resultado

output_path = (
    "data/processed/penalty_score_players_v3.csv"
)

df.to_csv(
    output_path,
    index=False
)

# Validação

print("\nTOP 20 COBRADORES\n")

print(
    df[
        [
            "player_name",
            "team_name",
            "weighted_score",
            "conversion_rate",
            "conversion_factor",
            "final_score"
        ]
    ]
    .head(20)
)

print(
    f"\nJogadores avaliados: "
    f"{len(df)}"
)

print(
    "\nArquivo salvo em:"
)

print(output_path)