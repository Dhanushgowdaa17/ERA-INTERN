import sqlite3

#1. Connect to the database(creates database if not exists)
conn = sqlite3.connect("internship.db")

#2. Create a cursor object to execute SQL commands
cursor = conn.cursor()

#3. Create the interns table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS interns (
  id INTEGER PRIMARY KEY,
  name text,
  track TEXT,
  stipend INTEGER
)
""")
#4. Insert dataset
intern_data = [
  (1, "Asha", "Data Science", 6000),
  (2, "Ravi", "Web Dev", 4000),
  (3, "Meena", "Data Science", 7000),
  (4, "Kiran", "Cyber Security", 5500),
  (5, "Arjun", "Web Dev", 3000),
  (6, "Sneha", "Data Science", 4500)
]

cursor.executemany("INSERT OR REPLACE INTO interns VALUES (?, ?, ?, ?)",intern_data)
conn.commit()

#Task 1: FILTER (WHERE)
print("Data Science interns with stipend > 5000:\n")

cursor.execute("""
SELECT  * FROM interns
WHERE track  = 'Data Science' AND stipend > 5000
""")

rows = cursor.fetchall()

for row in rows:
    print(row)

#Task 2: AGGREGATE  (GROUP BY - AVG)
print("\nAverage stipend per track:\n")

cursor.execute("""
SELECT track,AVG(stipend) AS avg_stipend
FROM interns
GROUP BY track
""")

rows = cursor.fetchall()

for row in rows:
    print(row)

#Task 3: COUNT interns per track:\n")
print("\nNumber of interns per track:\n")

cursor.execute("""
SELECT track,COUNT(*) AS total_interns
FROM interns
GROUP BY track
""")

rows = cursor.fetchall()

for row in rows:
    print(row)

#Close connection
conn.close()