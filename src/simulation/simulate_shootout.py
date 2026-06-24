import random
import pandas as pd

from take_penalty import (
    take_penalty
)


TOP5_PATH = (
    "/home/joao/world-cup-penalty-simulator/data/processed/top5_penalty_takers_normalized.csv"
)

GK_PATH = (
    "/home/joao/world-cup-penalty-simulator/data/processed/starting_goalkeepers_normalized.csv"
)


def get_team_takers(
    team_name,
    df_takers
):

    team_players = (
        df_takers[
            df_takers["team_name"]
            ==
            team_name
        ]
        .sort_values(
            "penalty_rank"
        )
    )

    return (
        team_players[
            "normalized_score"
        ]
        .tolist()
    )


def get_goalkeeper_score(
    team_name,
    df_goalkeepers
):

    goalkeeper = (
        df_goalkeepers[
            df_goalkeepers["team_name"]
            ==
            team_name
        ]
    )

    return float(
        goalkeeper[
            "normalized_goalkeeper_score"
        ].iloc[0]
    )


def simulate_shootout(
    team_a,
    team_b,
    verbose=False
):

    df_takers = pd.read_csv(
        TOP5_PATH
    )

    df_goalkeepers = pd.read_csv(
        GK_PATH
    )

    team_a_takers = get_team_takers(
        team_a,
        df_takers
    )

    team_b_takers = get_team_takers(
        team_b,
        df_takers
    )

    team_a_gk = get_goalkeeper_score(
        team_a,
        df_goalkeepers
    )

    team_b_gk = get_goalkeeper_score(
        team_b,
        df_goalkeepers
    )

    # ==================================
    # DIAGNÓSTICO DOS SCORES UTILIZADOS
    # ==================================

    if verbose:

        print(
            "\n--- DADOS UTILIZADOS ---"
        )

        print(
            f"\n{team_a} cobradores:"
        )

        print(
            team_a_takers
        )

        print(
            f"{team_a} goleiro:"
        )

        print(
            team_a_gk
        )

        print(
            f"\n{team_b} cobradores:"
        )

        print(
            team_b_takers
        )

        print(
            f"{team_b} goleiro:"
        )

        print(
            team_b_gk
        )

        print(
            "\n------------------------"
        )

    team_a_goals = 0
    team_b_goals = 0

    for i in range(5):

        if take_penalty(
            team_a_takers[i],
            team_b_gk
        ):
            team_a_goals += 1

        if take_penalty(
            team_b_takers[i],
            team_a_gk
        ):
            team_b_goals += 1

    if verbose:

        print(
            f"\nApós 5 cobranças:"
        )

        print(
            f"{team_a} {team_a_goals} x {team_b_goals} {team_b}"
        )

    if team_a_goals == team_b_goals:

        if verbose:

            print(
                "\nEmpate - iniciando morte súbita..."
            )

        round_number = 6

        while True:

            team_a_penalty = take_penalty(
                random.choice(
                    team_a_takers
                ),
                team_b_gk
            )

            team_b_penalty = take_penalty(
                random.choice(
                    team_b_takers
                ),
                team_a_gk
            )

            if team_a_penalty:
                team_a_goals += 1

            if team_b_penalty:
                team_b_goals += 1

            if verbose:

                print(
                    f"Rodada {round_number}: "
                    f"{team_a} {'Gol' if team_a_penalty else 'Erro'} | "
                    f"{team_b} {'Gol' if team_b_penalty else 'Erro'}"
                )

            if team_a_penalty != team_b_penalty:
                break

            round_number += 1

    if verbose:

        print(
            "\nResultado Final:"
        )

        print(
            f"{team_a} {team_a_goals} x {team_b_goals} {team_b}"
        )

    if team_a_goals > team_b_goals:
        return "A"

    else:
        return "B"


if __name__ == "__main__":

    simulate_shootout(
        "Argentina",
        "France",
        verbose=True
    )