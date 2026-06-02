# src/load_matchups.py

import pandas as pd

FILE_PATH = "data/raw/round_of_32_predictions.txt"


def load_matchups(file_path):

    matchups = []

    match_id = 1

    stage = "Round of 32"

    with open(file_path, "r", encoding="utf-8") as file:

        for line in file:

            line = line.strip()

            if not line:
                continue

            team_a, team_b = line.split(" x ")

            matchups.append(
                {
                    "match_id": match_id,
                    "stage": stage,
                    "team_a": team_a,
                    "team_b": team_b
                }
            )

            match_id +=1

    return matchups


matchups = load_matchups(FILE_PATH)

print(f"Total matchups loaded: {len(matchups)}")

df_matchups = pd.DataFrame(matchups)

print(df_matchups.head())