import random

from penalty_simulation import (
    penalty_probability
)


def take_penalty(
    taker_score,
    goalkeeper_score
):

    probability = penalty_probability(
        taker_score,
        goalkeeper_score
    )

    result = (
        random.random()
        <
        probability
    )

    return result

for i in range(20):

    print(
        take_penalty(
            0.85,
            0.60
        )
    )
