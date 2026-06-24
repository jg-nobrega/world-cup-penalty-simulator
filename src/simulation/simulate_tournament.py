import pandas as pd

from simulate_matchup import (
    simulate_matchup
)

print(simulate_matchup.__code__.co_filename)

ROUND_32_PATH = (
    "/home/joao/world-cup-penalty-simulator/data/raw/round_of_32_predictions.csv"
)



df = pd.read_csv(
    ROUND_32_PATH
)


winners = []

for _, row in df.iterrows():

    result = simulate_matchup(
        row["team_a"],
        row["team_b"],
        #verbose=False
    )

    winners.append(
        result["winner"]
    )

    print(
        f"{row['team_a']} x {row['team_b']} "
        f"-> "
        f"{result['winner']}"
    )


print(
    "\nClassificados:"
)

for winner in winners:

    print(
        winner
    )