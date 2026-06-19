import pandas as pd

# Leitura dos dados

df = pd.read_csv(
    "/home/joao/world-cup-penalty-simulator/data/processed/pool/goalkeeper_stats_2024.csv"
)

# Trata valores nulos

df["minutes"] = (
    df["minutes"]
    .fillna(0)
)

df["rating"] = (
    pd.to_numeric(
        df["rating"],
        errors="coerce"
    )
)

df["saves"] = (
    df["saves"]
    .fillna(0)
)

df["goals_conceded"] = (
    df["goals_conceded"]
    .fillna(0)
)

df["penalties_saved"] = (
    df["penalties_saved"]
    .fillna(0)
)

# Considera rating apenas quando houve minutos

df["rating_valid"] = df["rating"]

df.loc[
    df["minutes"] == 0,
    "rating_valid"
] = None

# Consolida por goleiro

df_goalkeepers = (
    df.groupby(
        [
            "player_id",
            "player_name",
            "team_name"
        ],
        as_index=False
    )
    .agg(
        total_minutes=(
            "minutes",
            "sum"
        ),
        avg_rating=(
            "rating_valid",
            "mean"
        ),
        total_saves=(
            "saves",
            "sum"
        ),
        goals_conceded=(
            "goals_conceded",
            "sum"
        ),
        penalties_saved=(
            "penalties_saved",
            "sum"
        )
    )
)

df_goalkeepers["avg_rating"] = (
    df_goalkeepers["avg_rating"]
    .fillna(0)
)

# Normalização

max_minutes = (
    df_goalkeepers["total_minutes"]
    .max()
)

max_saves = (
    df_goalkeepers["total_saves"]
    .max()
)

df_goalkeepers["minute_factor"] = (
    df_goalkeepers["total_minutes"]
    /
    max_minutes
)

df_goalkeepers["save_factor"] = (
    df_goalkeepers["total_saves"]
    /
    max_saves
)

# Score bruto

df_goalkeepers["raw_goalkeeper_score"] = (
    (
        df_goalkeepers["avg_rating"]
        * 0.7
    )
    +
    (
        df_goalkeepers["save_factor"]
        * 2
    )
    +
    (
        df_goalkeepers["minute_factor"]
        * 1
    )
    +
    (
        df_goalkeepers["penalties_saved"]
        * 1
    )
)

# Fator de experiência

df_goalkeepers["experience_factor"] = (
    df_goalkeepers["total_minutes"]
    / 3000
)

df_goalkeepers["experience_factor"] = (
    df_goalkeepers["experience_factor"]
    .clip(
        upper=1
    )
)

# Score final

df_goalkeepers["final_goalkeeper_score"] = (
    df_goalkeepers["raw_goalkeeper_score"]
    *
    df_goalkeepers["experience_factor"]
)

# Ordena

df_goalkeepers = (
    df_goalkeepers
    .sort_values(
        by="final_goalkeeper_score",
        ascending=False
    )
)

# Salva

output_path = (
    "data/processed/goalkeeper_score_final.csv"
)

df_goalkeepers.to_csv(
    output_path,
    index=False
)

# Validações

print("\nTOP 20 GOLEIROS\n")

print(
    df_goalkeepers[
        [
            "player_name",
            "team_name",
            "final_goalkeeper_score",
            "avg_rating",
            "total_minutes",
            "experience_factor"
        ]
    ]
    .head(20)
)

print(
    f"\nTotal de goleiros: "
    f"{len(df_goalkeepers)}"
)

print(
    "\nArquivo salvo em:"
)

print(output_path)


