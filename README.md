# World Cup Penalty Simulator

Simulating the FIFA World Cup knockout stage under the assumption that every match is decided by penalty shootouts.

## Objective

Estimate each national team's probability of winning the FIFA World Cup using player statistics, goalkeeper performance and Monte Carlo simulations.

## Project Status

🚧 **Active Development**

### Progress

* ✅ Official squad collection
* ✅ Penalty records collection
* ✅ Competition weighting
* ✅ Penalty taker scoring model
* ✅ Goalkeeper scoring model
* ✅ Automatic selection of the top 5 penalty takers
* ✅ Automatic selection of the starting goalkeeper
* 🔄 World Cup knockout stage simulation

📍 For see the result: https://www.linkedin.com/in/joaognobrega/

## Methodology

### Penalty Takers

Penalty records were collected from multiple domestic and international competitions through API-Football.

Each player receives a score based on:

* Penalties scored
* Penalties missed
* Competition weight
* Conversion rate

The five highest-ranked players from each national team are automatically selected as penalty takers.

### Goalkeepers

Goalkeepers are evaluated using:

* Average rating
* Minutes played
* Saves
* Penalties saved

The highest-ranked goalkeeper becomes the starting goalkeeper for the simulation.

---

## Assumptions

* Every knockout match ends in a draw.
* Every match is decided by penalty shootouts.
* Player selection is fully data-driven.
* No subjective decisions, official lineups or player reputation are considered.

---

## Simulation Pipeline

1. Collect official squads.
2. Collect player statistics.
3. Calculate penalty taker scores.
4. Calculate goalkeeper scores.
5. Select the five penalty takers.
6. Select the starting goalkeeper.
7. Simulate penalty shootouts.
8. Simulate the World Cup knockout bracket.
9. Estimate title probabilities using Monte Carlo simulations.

---

## Tech Stack

* Python
* Pandas
* NumPy
* API-Football
* Git
* GitHub

---

## Author

**João Gabriel Nóbrega**

Data Analyst | Data Science & Analytics Student

This project explores statistical modeling, sports analytics and Monte Carlo simulation techniques applied to football.
