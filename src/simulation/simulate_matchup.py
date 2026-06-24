import random

from simulate_shootout import (
    simulate_shootout
)


def simulate_matchup(
    team_a,
    team_b,
    simulations=10000,
    verbose=True
):

    team_a_wins = 0
    team_b_wins = 0

    for _ in range(simulations):

        winner = simulate_shootout(
            team_a,
            team_b,
            verbose=False
        )

        if winner == "A":

            team_a_wins += 1

        else:

            team_b_wins += 1

    team_a_probability = (
        team_a_wins
        /
        simulations
    )

    team_b_probability = (
        team_b_wins
        /
        simulations
    )

    difference = abs(
        team_a_probability
        -
        team_b_probability
    )

    # -----------------------------
    # ESCOLHA DO VENCEDOR OFICIAL
    # -----------------------------

    matchup_winner = random.choices(
        [
            team_a,
            team_b
        ],
        weights=[
            team_a_probability,
            team_b_probability
        ]
    )[0]

    if verbose:

        print(
            f"\n{team_a}: {team_a_probability:.2%}"
        )

        print(
            f"{team_b}: {team_b_probability:.2%}"
        )

        print(
            f"\nDiferença: {difference:.2%}"
        )

        if difference < 0.05:

            print(
                "Confronto extremamente equilibrado"
            )

        elif difference < 0.15:

            print(
                "Leve favoritismo"
            )

        elif difference < 0.30:

            print(
                "Favoritismo relevante"
            )

        else:

            print(
                "Grande favoritismo"
            )

        print(
            f"\nClassificado: {matchup_winner}"
        )

    return {

        "team_a": team_a,

        "team_b": team_b,

        "team_a_probability":
            team_a_probability,

        "team_b_probability":
            team_b_probability,

        "difference":
            difference,

        "winner":
            matchup_winner

    }


if __name__ == "__main__":

    resultado = simulate_matchup(
        "France",
        "Portugal"
    )

    print(resultado)