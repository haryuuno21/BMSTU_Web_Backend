from faker import Faker
import psycopg2
import time

start_time = time.time()
fake = Faker("ru_RU")

cur = None
conn = None

row_total = 100000
try:
    conn = psycopg2.connect(database="weather_stations_2", user="Haryuuno", password="qwe123",
    host="localhost", port="32768")
    print("Opened database successfully")
    cur = conn.cursor()

    for i in range(1, row_total + 1):
        short_name = fake.text(20)
        full_name = "Метеостанция " + short_name
        address = fake.street_address()
        chief_fio = fake.name_nonbinary()
        phone_number = fake.phone_number()
        sea_level = fake.random_number(3)

        cur.execute(
            "INSERT INTO stations (status,short_name, full_name, address, chief_fio,phone_number,sea_level) VALUES (%s, %s, %s, %s, %s, %s,%s)",
            ("A", short_name, full_name, address, chief_fio, phone_number,sea_level)
        )
        i += 1
    conn.commit()
    print("Records created successfully")

except Exception as e:
 print(f"An error occurred: {e}")

finally:
 if cur is not None:
    cur.close()
 if conn is not None:
    conn.close()

print(
 f"{row_total} строк в PostgreSQL за --- {(time.time() - start_time)} сек. ---")