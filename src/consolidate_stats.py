import pandas as pd
import glob

# localizar todos os csv de penalty stats

arquivos = glob.glob(
    "data/processed/penalty_stats_2024_part*.csv"
)

# adicionar arquivo da Nova Zelândia 
# concatenando nova zelandia dps pq trouxe info da seleção errada

arquivos.append(
    "data/processed/penalty_stats_new_zealand.csv"
)

print(
    f"Arquivos encontrados: {len(arquivos)}"
)

# lista para armazenar dfs

lista_dfs = []

# ler todos os arquivos

for arquivo in sorted(arquivos):

    print(
        f"Lendo: {arquivo}"
    )

    df = pd.read_csv(arquivo)

    lista_dfs.append(df)

# consolidar

df_final = pd.concat(
    lista_dfs,
    ignore_index=True
)

print(
    f"Linhas antes do dedupe: {len(df_final)}"
)

# remover duplicidades

df_final = df_final.drop_duplicates()

print(
    f"Linhas após dedupe: {len(df_final)}"
)

# salvar resultado final

output_path = (
    "data/processed/penalty_stats_full.csv"
)

df_final.to_csv(
    output_path,
    index=False
)

print(
    f"Arquivo salvo em: {output_path}"
)

# validações rápidas

print("\nSeleções:")

print(
    df_final["team_name"]
    .nunique()
)

print("\nJogadores:")

print(
    df_final["player_id"]
    .nunique()
)

print("\nTotal de registros:")

print(
    len(df_final)
)

print("\nSeleções encontradas:")

print(
    sorted(
        df_final["team_name"]
        .unique()
    )
)