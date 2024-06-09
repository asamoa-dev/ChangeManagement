import snowflake.connector

def get_snowflake_connection():
    conn = snowflake.connector.connect(
        user='CMS_USER',                 # 実際のユーザー名
        password='CMS_PASSWORD',         # 実際のパスワード
        account='lw19390.japan-east.azure',  # アカウント識別子とリージョン情報
        warehouse='CMS_WH',              # 実際のウェアハウス名
        database='CMS_DATABASE',         # 実際のデータベース名
        schema='CMS_SCHEMA'              # 実際のスキーマ名
    )
    return conn

# 接続テスト
try:
    conn = get_snowflake_connection()
    print("Connection successful!")
    conn.close()
except Exception as e:
    print(f"Failed to connect: {e}")