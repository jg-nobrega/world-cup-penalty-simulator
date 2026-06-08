from dotenv import load_dotenv
import os
import requests
import pandas as pd
import time

# Carrega variáveis de ambiente
load_dotenv()

# Obtém chave da API
API_KEY = os.getenv("API_KEY")

# Endpoint da API
URL = "https://v3.football.api-sports.io/players/squads"

# Headers da requisição
HEADERS = {
    "x-apisports-key": API_KEY
}


# Busca a convocação de uma seleção
def get_squad(team_id):

    params = {
        "team": team_id
    }

    max_retries = 3

    for attempt in range(max_retries):

        response = requests.get(
            url=URL,
            headers=HEADERS,
            params=params
        )

        print(f"\nConsultando seleção {team_id}")
        print(f"Status Code: {response.status_code}")

        # Trata limite de requisições
        if response.status_code == 429:

            wait_time = 60

            print(
                f"Rate limit atingido para seleção {team_id}"
            )

            print(
                f"Aguardando {wait_time} segundos..."
            )

            time.sleep(wait_time)

            continue

        # Trata outros erros HTTP
        if response.status_code != 200:

            print(
                f"Erro HTTP para seleção {team_id}"
            )

            print(response.text)

            return None

        data = response.json()

        # Trata resposta vazia
        if len(data["response"]) == 0:

            print(
                f"Nenhum dado encontrado para seleção {team_id}"
            )

            return None

        team_name = data["response"][0]["team"]["name"]

        players = data["response"][0]["players"]

        df = pd.DataFrame(players)

        df = df.rename(
            columns={
                "id": "player_id"
            }
        )

        df["team_name"] = team_name
        df["team_id"] = team_id

        print(
            f"{team_name} carregada com sucesso"
        )

        print(
            f"Jogadores encontrados: {len(df)}"
        )

        return df

    print(
        f"Falha após {max_retries} tentativas para seleção {team_id}"
    )

    return None


# Lê arquivo de seleções
teams = pd.read_csv(
    "data/raw/team_ids.csv"
)

# Lista para armazenar DataFrames
all_squads = []

# Lista para armazenar falhas
failed_teams = []

# Percorre todas as seleções
for team_id in teams["team_id"]:

    team_id = int(team_id)

    df_team = get_squad(team_id)

    if df_team is not None:

        all_squads.append(df_team)

    else:

        failed_teams.append(team_id)

    # Respeita limite da API
    time.sleep(7)

# Consolida resultados
if len(all_squads) > 0:

    df_squads = pd.concat(
        all_squads,
        ignore_index=True
    )

    print("\nResumo")

    print(
        f"Total de jogadores: {len(df_squads)}"
    )

    print(
        f"Total de seleções: {df_squads['team_name'].nunique()}"
    )

    print("\nShape do DataFrame")

    print(df_squads.shape)

    print("\nPrimeiras linhas")

    print(df_squads.head())

    # Salva dataset consolidado
    df_squads.to_csv(
        "data/processed/all_squads.csv",
        index=False
    )

    print("\nArquivo salvo com sucesso")

    print(
        "data/processed/all_squads.csv"
    )

else:

    print(
        "\nNenhuma seleção foi carregada."
    )
    
# Exibe falhas
print("\nSeleções com erro:")

if len(failed_teams) == 0:

    print("Nenhuma")

else:

    for team in failed_teams:

        print(team)

        print(df_squads["team_name"].nunique())