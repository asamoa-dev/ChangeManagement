import os
from dotenv import load_dotenv
import snowflake.connector

# 環境変数を読み込む
load_dotenv()

def get_snowflake_connection():
    conn = snowflake.connector.connect(
        user=os.getenv('SNOWFLAKE_USER'),
        password=os.getenv('SNOWFLAKE_PASSWORD'),
        account=os.getenv('SNOWFLAKE_ACCOUNT'),
        warehouse=os.getenv('SNOWFLAKE_WAREHOUSE'),
        database=os.getenv('SNOWFLAKE_DATABASE'),
        schema=os.getenv('SNOWFLAKE_SCHEMA')
    )
    return conn

if __name__ == "__main__":
    try:
        conn = get_snowflake_connection()
        print("Connection successful!")
        conn.close()
    except Exception as e:
        print(f"Failed to connect: {e}")