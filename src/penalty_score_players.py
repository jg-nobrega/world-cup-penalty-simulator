import pandas as pd

# Leitura dos dados

df_stats = pd.read_csv(
    "data/processed/penalty_stats_full.csv"
)

df_weights = pd.read_csv(
    "data/raw/league_weights.csv"
)

# Junta o peso do campeonato

df = df_stats.merge(
    df_weights,
    on="league_name",
    how="left"
)

# Calcula score da linha

df["row_score"] = (
    (
        df["penalties_scored"]
        -
        df["penalties_missed"]
    )
    *
    df["score"]
)

# Consolida por jogador

df_players = (
    df.groupby(
        [
            "player_id",
            "player_name",
            "team_name"
        ],
        as_index=False
    )
    .agg(
        penalties_scored=(
            "penalties_scored",
            "sum"
        ),
        penalties_missed=(
            "penalties_missed",
            "sum"
        ),
        weighted_score=(
            "row_score",
            "sum"
        )
    )
)

# Calcula total de cobranças

df_players["total_penalties"] = (
    df_players["penalties_scored"]
    +
    df_players["penalties_missed"]
)

# Calcula taxa de conversão

df_players["conversion_rate"] = (
    df_players["penalties_scored"]
    /
    df_players["total_penalties"]
)

# Ordena ranking

df_players = (
    df_players
    .sort_values(
        by="weighted_score",
        ascending=False
    )
)

# Salva resultado

output_path = (
    "data/processed/raw_penalty_score_players.csv"
)

df_players.to_csv(
    output_path,
    index=False
)

# Validações

print("\nTOP 20 COBRADORES\n")

print(
    df_players[
        [
            "player_name",
            "team_name",
            "weighted_score",
            "conversion_rate"
        ]
    ]
    .head(20)
)

print(
    f"\nJogadores avaliados: "
    f"{len(df_players)}"
)

print(
    f"\nArquivo salvo em:"
)

print(output_path)