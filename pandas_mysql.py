import pandas as pd
import sqlalchemy

# Create the connection
engine = sqlalchemy.create_engine('mysql+pymysql://username:password@hostname/dbname')

# Query the database
sql = "SELECT * FROM table_name;"
df = pd.read_sql_query(sql, engine)

# Print the results
print(df)