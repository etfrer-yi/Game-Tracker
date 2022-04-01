import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

BASEDIR = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(BASEDIR, 'postgres_configs.env'))

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DATABASE = "GameTracker"

def main():
    engine = create_engine(f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DATABASE}')
    bf1_df = pd.read_json('battlefield1stats.json').sort_values("Rank")
    bf4_df = pd.read_json('battlefield4stats.json').sort_values("Rank")
    bf_hardline_df = pd.read_json('battlefield_hardline_stats.json').sort_values("Rank")
    dfs = [bf1_df, bf4_df, bf_hardline_df]
    table_names = ["Battlefield1Stats", "Battlefield4Stats", "BattlefieldHardlineStats"]
    for i in range(len(dfs)):
        dfs[i] = dfs[i].round(2)
        dfs[i].to_sql(table_names[i], con=engine, if_exists="replace")

if __name__ == "__main__":
    main()