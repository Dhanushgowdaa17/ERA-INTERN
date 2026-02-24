import sqlite3
import pandas as pd

#1. connect to database
conn = sqlite3.connect("internship.db")
cursor = conn.cursor()

#2. create mentors table
cursor.execute("""
CREATE TABLE IF NOT EXISTS mentors (
mentors_id INTEGER PRIMARY KEY,
mentors_name TEXT,
track TEXT
)
""")

#3. insert data into mentors table
mentor_data = [
  (1, "Dr. Rao", "Data Science"),
  (2, "Ms. Priya", "Web Dev"),
  (3, "Mr. Ahmed", "Cyber Security")
]
cursor.executemany("INSERT OR REPLACE INTO mentors VALUES (?, ?, ?)",
                   mentor_data
)
conn.commit()

#4. INNER JOIN query
join_query ="""
SELECT interns.name,
      interns.track,
      mentors.mentors_name
FROM interns
INNER JOIN mentors
ON interns.track = mentors.track
"""
#5. load result into pandas dataframe
df = pd.read_sql_query(join_query, conn)
print(df)

#6. close connection
conn.close()