import pandas as pd

# Carrega base pontuada

df = pd.read_csv(
    "data/processed/player_pool_scored.csv"
)

top5_final = []

# Percorre cada seleção

for team_name in sorted(
    df["team_name"].unique()
):

    team_df = df[
        df["team_name"] == team_name
    ].copy()

    selected = []

    # 1. Jogadores com histórico
   

    history_players = (
        team_df[
            team_df["has_history"] == True
        ]
        .sort_values(
            by="final_score",
            ascending=False
        )
    )

    for _, row in history_players.iterrows():

        row = row.copy()

        row["selection_reason"] = (
            "history"
        )

        selected.append(row)

        if len(selected) == 5:
            break

   
    # 2. Completa com atacantes
   

    if len(selected) < 5:

        selected_ids = [
            p["player_id"]
            for p in selected
        ]

        attackers = (
            team_df[
                (team_df["position"] == "Attacker")
                &
                (~team_df["player_id"].isin(selected_ids))
            ]
        )

        for _, row in attackers.iterrows():

            row = row.copy()

            row["selection_reason"] = (
                "fallback_attacker"
            )

            selected.append(row)

            if len(selected) == 5:
                break

    
    # 3. Completa com meio-campo
    

    if len(selected) < 5:

        selected_ids = [
            p["player_id"]
            for p in selected
        ]

        midfielders = (
            team_df[
                (team_df["position"] == "Midfielder")
                &
                (~team_df["player_id"].isin(selected_ids))
            ]
        )

        for _, row in midfielders.iterrows():

            row = row.copy()

            row["selection_reason"] = (
                "fallback_midfielder"
            )

            selected.append(row)

            if len(selected) == 5:
                break

    # Ranking interno

    for rank, player in enumerate(
        selected,
        start=1
    ):

        player["penalty_rank"] = rank

        top5_final.append(player)

# Consolida

df_top5 = pd.DataFrame(
    top5_final
)

# Ordena

df_top5 = df_top5.sort_values(
    [
        "team_name",
        "penalty_rank"
    ]
)

# Salva

output_path = (
    "data/processed/top5_penalty_takers.csv"
)

df_top5.to_csv(
    output_path,
    index=False
)

# Validações

#  print(
#     "\nQuantidade de seleções:"
# )

# print(
#     df_top5["team_name"]
#     .nunique()
# )

# print(
#     "\nQuantidade de jogadores:"
# )

# print(
#     len(df_top5)
# )

# print(
#     "\nJogadores por seleção:"
# )

# print(
#     df_top5
#     .groupby("team_name")
#     .size()
# )

# print(
#     "\nArquivo salvo:"
# )

# print(output_path)



df_top5_tunisia = df_top5[
    df_top5["team_name"] == "Tunisia"
]

print(df_top5_tunisia)


df_top5_inglaterra = df_top5[
    df_top5['team_name'] == 'England'
]

print(df_top5_inglaterra)