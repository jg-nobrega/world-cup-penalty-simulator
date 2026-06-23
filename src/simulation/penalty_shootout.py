from take_penalty import (
    take_penalty
)

argentina = [
    0.90,
    0.82,
    0.78,
    0.74,
    0.70
]

france = [
    0.88,
    0.84,
    0.79,
    0.72,
    0.69
]

argentina_gk = 0.78
france_gk = 0.92

argentina_goals = 0
france_goals = 0

for i in range(5):

    if take_penalty(
        argentina[i],
        france_gk
    ):
        argentina_goals += 1

    if take_penalty(
        france[i],
        argentina_gk
    ):
        france_goals += 1

print(
    f"""
Argentina {argentina_goals}
França {france_goals}
"""
)