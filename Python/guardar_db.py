import pandas as pd
from sqlalchemy import create_engine

# Define your PostgreSQL connection details
db_url = "postgresql+psycopg2://username:password@host:port/database"

# Create SQLAlchemy engine
engine = create_engine(db_url)

# Sample DataFrame
data = {'id': [1, 2, 3], 'name': ['Alice', 'Bob', 'Charlie'], 'age': [25, 30, 35]}
df = pd.DataFrame(data)

# Save DataFrame to PostgreSQL table
df.to_sql('your_table_name', con=engine, if_exists='replace', index=False)