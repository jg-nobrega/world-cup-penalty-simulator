import pandas as pd

#chama a base dos convoados
df = pd.read_csv(
    "/home/joao/world-cup-penalty-simulator/data/processed/all_squads.csv"
)

#consideramos como batedores somente atacantes e meio campistas para não sobrecarregar as requisições
df_candidates = df[
    df["position"].isin(
        ['Midfielder', 'Attacker']
    )
]

#filtra os campos
df_candidates = df_candidates[
    [
        "player_id",
        "name",
        "position",
        "team_name",
        "team_id"
    ]
]

print(df_candidates.shape)
print(df_candidates.head())

#exporta o resultado para csv
df_candidates.to_csv(
    "data/processed/player_pool.csv",
    index=False
)

print(
    df_candidates["position"]
    .value_counts()
)
print(
    df_candidates
    .groupby("team_name")
    .size()
    .sort_values()
)