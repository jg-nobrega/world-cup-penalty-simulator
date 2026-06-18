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

# Carrega goleiros
df_goalkeepers = pd.read_csv(
    "/home/joao/world-cup-penalty-simulator/data/processed/goalkeeper_pool.csv"
)

total_goalkeepers = len(df_goalkeepers)

print(
    f"Total de goleiros encontrados: "
    f"{total_goalkeepers}"
)

# Lista para armazenar resultados
results = []

# Loop dos goleiros
for idx, (_, row) in enumerate(
    df_goalkeepers.iterrows(),
    start=1
):

    player_id = row["player_id"]
    player_name = row["name"]
    position = row["position"]
    team_name = row["team_name"]
    team_id = row["team_id"]

    print(
        f"[{idx}/{total_goalkeepers}] "
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
            f"do goleiro {player_id}"
        )

        try:
            print(response.json())
        except:
            pass

        continue

    data = response.json()

    # Verifica retorno
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

        minutes = stat["games"]["minutes"] or 0

        rating = stat["games"]["rating"]

        goals_conceded = stat["goals"]["conceded"] or 0

        saves = stat["goals"]["saves"] or 0

        penalties_saved = stat["penalty"]["saved"] or 0

        results.append({
            "player_id": player_id,
            "player_name": player_name,
            "position": position,
            "team_name": team_name,
            "team_id": team_id,
            "league_id": league_id,
            "league_name": league_name,
            "season": season,
            "minutes": minutes,
            "rating": rating,
            "goals_conceded": goals_conceded,
            "saves": saves,
            "penalties_saved": penalties_saved
        })

    # Salva progresso após cada goleiro
    df_partial = pd.DataFrame(results)

    df_partial.to_csv(
        "data/processed/goalkeeper_stats_2024.csv",
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
    "data/processed/goalkeeper_stats_2024.csv"
)