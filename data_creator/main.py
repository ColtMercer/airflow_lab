import psycopg2
from faker import Faker

def create_fake_data():
    fake = Faker()

    # Connect to the PostgreSQL database
    conn = psycopg2.connect(
        host="localhost",
        database="sample_data_source",
        user="devuser",
        password="devpasswd"
    )
    cursor = conn.cursor()

    # Create 100 entries of fake user data
    for _ in range(100):
        name = fake.name()
        email = fake.email()
        phone_number = fake.phone_number()
        city = fake.city()
        country = fake.country()
        company = fake.company()
        job = fake.job()
        job_title = fake.job_title()

        # Insert the data into the database
        cursor.execute("INSERT INTO users (name, email, phone_number, city, country, company, job, job_title) VALUES (%s, %s, %s)", (name, email, phone_number, city, country, company, job, job_title))

    # Commit the changes and close the connection
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    create_fake_data()