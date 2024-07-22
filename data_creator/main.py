import psycopg2
from faker import Faker


def create_fake_data():
    fake = Faker()

    # Connect to the PostgreSQL database
    conn = psycopg2.connect(
        host="postgres",
        database="sample_data_source",
        user="devuser",
        password="devpasswd"
    )
    cursor = conn.cursor()
    print("Connected to the database")
    print("Creating the customers table")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255),
            email VARCHAR(255),
            phone_number VARCHAR(255),
            city VARCHAR(255),
            country VARCHAR(255),
            company VARCHAR(255),
            job VARCHAR(255)
        )
    """)
    print("Table created successfully")

    # Create 100 entries of fake user data
    print("Creating 100 fake customers")
    for _ in range(100):
        name = fake.name()
        email = fake.email()
        phone_number = fake.phone_number()
        city = fake.city()
        country = fake.country()
        company = fake.company()
        job = fake.job()

        # Insert the data into the database
        cursor.execute(
            "INSERT INTO customers (name, email, phone_number, city, country, company, job) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s)",
            (name, email, phone_number, city, country, company, job)
        )
    
    print("100 fake customers created successfully")
    # Commit the changes and close the connection
    conn.commit()
    cursor.close()
    conn.close()


def create_tableau_customers_table():
    conn = psycopg2.connect(
        host="postgres",
        database="sample_tableau",
        user="devuser",
        password="devpasswd"
    )
    cursor = conn.cursor()
    print("Connected to the database")
    print("Creating the tableau_customers table")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255),
            email VARCHAR(255),
            phone_number VARCHAR(255),
            city VARCHAR(255),
            country VARCHAR(255),
            company VARCHAR(255),
            job_title VARCHAR(255)
        )
    """)
    print("Table created successfully")
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    create_fake_data()
    create_tableau_customers_table()