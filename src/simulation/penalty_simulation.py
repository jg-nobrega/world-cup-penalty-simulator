def penalty_probability(
    taker_score,
    goalkeeper_score
):
    base_probability = 0.75

    score_difference = (
        taker_score
        -
        goalkeeper_score
    )

    probability = (
        base_probability
        +
        (
            score_difference
            * 0.25
        )
    )

    probability = max(
        0.55,
        min(
            0.95,
            probability
        )
    )

    return probability


# print(
#     penalty_probability(
#         0.85,
#         0.82
#     )
#)

# print(
#     penalty_probability(
#         0.34,
#         1.00
#     )
# )

# print(
#     penalty_probability(
#         1.00,
#         0.40
#     )
# )