import pandas as pd

# Leitura do score final

df = pd.read_csv(
    "/home/joao/world-cup-penalty-simulator/data/processed/score/raw_goalkeeper_score_v2.csv"
)

# Ordena por seleção e score

df = (
    df
    .sort_values(
        [
            "team_name",
            "final_goalkeeper_score"
        ],
        ascending=[
            True,
            False
        ]
    )
)

# Ranking dentro da seleção

df["goalkeeper_rank"] = (
    df.groupby(
        "team_name"
    )
    .cumcount()
    + 1
)

# Mantém apenas o titular

df_starting_goalkeepers = (
    df[
        df["goalkeeper_rank"] == 1
    ]
    .copy()
)

# Ordena para visualização

df_starting_goalkeepers = (
    df_starting_goalkeepers
    .sort_values(
        "team_name"
    )
)

# Salva

output_path = (
    "data/processed/starting_goalkeepers.csv"
)

df_starting_goalkeepers.to_csv(
    output_path,
    index=False
)

# Validações

print(
    "\nQuantidade de seleções:"
)

print(
    df_starting_goalkeepers[
        "team_name"
    ].nunique()
)

print(
    "\nQuantidade de goleiros:"
)

print(
    len(
        df_starting_goalkeepers
    )
)

print(
    "\nTitulares:"
)

print(
    df_starting_goalkeepers[
        [
            "team_name",
            "player_name",
            "final_goalkeeper_score"
        ]
    ]
)

print(
    "\nArquivo salvo:"
)

print(
    output_path
)