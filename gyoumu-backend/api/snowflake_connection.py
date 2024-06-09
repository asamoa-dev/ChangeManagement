import snowflake.connector

def get_snowflake_connection():
    conn = snowflake.connector.connect(
        user='CMS_USER',
        password='CMS_PASSWORD',
        account='lw19390.japan-east.azure',
        warehouse='CMS_WH',
        database='CMS_DATABASE',
        schema='CMS_SCHEMA'
    )
    return conn

