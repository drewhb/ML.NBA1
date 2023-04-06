import sqlite3

conn = sqlite3.connect('dataset.sqlite')
cursor = conn.cursor()


# # Try creating a new table
# cursor.execute("CREATE TABLE my_table (id INTEGER PRIMARY KEY, name TEXT)")
# conn.commit()

# Query sqlite_master to get a list of all tables
# cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
# table_names = cursor.fetchall()

# # Print the list of tables
# print("Tables:")
# for name in table_names:
#     print(name)

# conn.close()
# cursor = conn.cursor()

# cursor.execute('SELECT * FROM my_table')
# results = cursor.fetchall()

# for row in results:
#     print(row)

# conn.close()
import sqlite3
import pandas as pd

dataset = "dataset_2012-23"
con = sqlite3.connect("./dataset.sqlite")
data = pd.read_sql_query(f"SELECT * FROM \"{dataset}\" LIMIT 100", con, index_col="index")
con.close()

print(data.columns)

print()
