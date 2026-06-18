import pandas as pd

df = pd.read_csv(
    "data/processed/raw_penalty_score_players.csv"
)

df["final_score"] = (
    df["weighted_score"]
    *
    df["conversion_rate"]
)

df = df.sort_values(
    by="final_score",
    ascending=False
)

df.to_csv(
    "data/processed/penalty_score_players_final.csv",
    index=False
)

print(
    df[
        [
            "player_name",
            "team_name",
            "weighted_score",
            "conversion_rate",
            "final_score"
        ]
    ]
    .head(20)
)