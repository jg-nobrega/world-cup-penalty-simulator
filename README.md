# world-cup-penalty-simulator

Simulating the FIFA World Cup knockout stage assuming every match is decided by penalty shootouts.

## Objective

The goal is to estimate which national teams would have the highest probability of winning the World Cup if every knockout match were decided by penalties.

## Project Status

🚧 In Development

## Main Assumptions

* All knockout matches finish tied.
* Every match is decided by penalty shootouts.
* Team strength is based on penalty takers and goalkeepers.
* Psychological and external factors are not considered.

## Player Selection Methodology

### Penalty Takers

A player pool was created using the official squads of the selected national teams.

Penalty records were collected from multiple domestic and international competitions through the API-Football service and consolidated into a single dataset.

The final penalty score considers:

* penalties scored;
* penalties missed;
* competition weight;
* conversion rate.

After calculating the score, the top 5 penalty takers of each national team are selected for the simulation.

### Goalkeepers

Goalkeeper performance is evaluated using:

* average rating;
* minutes played;
* saves;
* penalties saved.

A goalkeeper score is calculated for every available goalkeeper in the player pool.

The highest-ranked goalkeeper from each national team is selected as the starting goalkeeper for the simulation.

### Important Note

This project does not use official lineups, coach decisions, player reputation, or subjective evaluations.

Therefore, the selected penalty takers and goalkeepers may differ from real-life World Cup lineups, reflecting only the statistical methodology adopted by the simulator.

## Planned Features

* Team and player data collection through football APIs
* Penalty taker performance scoring
* Goalkeeper penalty-saving scoring
* Monte Carlo tournament simulations
* Probability rankings for each national team

## Next Steps

* Build the penalty taker vs goalkeeper matchup model
* Calculate scoring probabilities for each penalty attempt
* Simulate full penalty shootouts
* Simulate the entire World Cup knockout bracket
* Run Monte Carlo simulations to estimate title probabilities

## Tech Stack

* Python
* Pandas
* Football APIs
* GitHub

## Author

João Gabriel Nóbrega
