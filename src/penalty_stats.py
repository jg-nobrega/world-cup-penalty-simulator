from dotenv import load_dotenv
import os
import time
import requests
import pandas as pd

# Carrega variáveis de ambiente
load_dotenv()

# Obtém chave da API
API_KEY = os.getenv("API_KEY")

# Endpoint da API
URL = "https://v3.football.api-sports.io/players"

# Headers da requisição
HEADERS = {
    "x-apisports-key": API_KEY
}

# Define lote a ser processado
START = 0
END = 50

# Carrega jogadores
df_players = pd.read_csv(
    "data/processed/player_pool.csv"
)

# Seleciona apenas o lote desejado
df_players = df_players.iloc[START:END]

# Total de jogadores do lote
total_players = len(df_players)

# Lista para armazenar resultados
results = []

# Loop dos jogadores
for idx, (_, row) in enumerate(
    df_players.iterrows(),
    start=1
):

    player_id = row["player_id"]
    player_name = row["name"]
    position = row["position"]
    team_name = row["team_name"]
    team_id = row["team_id"]

    print(
        f"[{idx}/{total_players}] "
        f"Consultando {player_name} ({player_id})"
    )

    params = {
        "id": player_id,
        "season": 2024
    }

    response = requests.get(
        url=URL,
        headers=HEADERS,
        params=params
    )

    print(
        f"Status Code: "
        f"{response.status_code}"
    )

    # Trata erro HTTP
    if response.status_code != 200:

        print(
            f"Erro na consulta "
            f"do jogador {player_id}"
        )

        try:
            print(response.json())
        except:
            pass

        continue

    data = response.json()

    # Verifica se retornou dados
    if not data["response"]:

        print(
            f"Sem dados para "
            f"{player_name}"
        )

        continue

    statistics = data["response"][0]["statistics"]

    # Percorre competições
    for stat in statistics:

        league_id = stat["league"]["id"]

        if league_id is None:
            league_id = 0

        league_name = stat["league"]["name"]
        season = stat["league"]["season"]

        penalties_scored = stat["penalty"]["scored"]
        penalties_missed = stat["penalty"]["missed"]

        # Trata nulos
        penalties_scored = penalties_scored or 0
        penalties_missed = penalties_missed or 0

        # Mantém apenas quem cobrou pênalti
        if penalties_scored > 0 or penalties_missed > 0:

            results.append({
                "player_id": player_id,
                "player_name": player_name,
                "position": position,
                "team_name": team_name,
                "team_id": team_id,
                "league_id": league_id,
                "league_name": league_name,
                "season": season,
                "penalties_scored": penalties_scored,
                "penalties_missed": penalties_missed
            })

    # Salva progresso após cada jogador
    df_partial = pd.DataFrame(results)

    df_partial.to_csv(
        "data/processed/penalty_stats_2024_part1.csv",
        index=False
    )

    # Evita limite da API
    time.sleep(7)

print("\nResumo Final")

print(
    f"Linhas encontradas: "
    f"{len(results)}"
)

print(
    "\nArquivo salvo:"
)

print(
    "data/processed/penalty_stats_2024_part1.csv"
)