import psycopg2 as psy
import random as rn




conn = psy.connect(host = "localhost", dbname="postgres", user="postgres",
                   password="916440", port=5432)

cur=conn.cursor()

### CREATE BASIC TABLE ###

#cur.execute("""CREATE TABLE IF NOT EXISTS transactions (
#    id INT PRIMARY KEY,
#    name VARCHAR(255),
#    item VARCHAR,
#    amount INT
#);
#""")

#cur.execute("""INSERT INTO transactions (id, name, item, amount) VALUES
#(1, 'Mike', shoes, 80),
#(2, 'Suzie', food, 100),
#(3, 'John', clothes, 50),
#(4, 'Amy', clothes, 400),
#(5, 'Lauren', food, 30);
#""")

### CREATE TABLE WITH JUST NUMBERS ###

cur.execute("""CREATE TABLE IF NOT EXISTS numbers (
    id INT PRIMARY KEY,
    num INT
);
""")

a=1

while a < 10:
    b = rn.randint(1, 300)
    cur.execute("""INSERT INTO numbers (id, num) VALUES
    (%s,%s);
    """, (a,b))
    a=a+1



cur.execute("""SELECT * FROM person WHERE name = 'Lauren';""")

print(cur.fetchone())

cur.execute("""SELECT * FROM person WHERE age > 30""")

for row in cur.fetchall():
    print(row)

cur.execute("""SELECT * FROM person WHERE name LIKE '%e'
AND name LIKE 'M%';""")

for item in cur.fetchall():
    print(item)


conn.commit()
cur.close()
conn.close()