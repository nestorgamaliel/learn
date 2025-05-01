import pandas as pd
import psycopg2
from datetime import datetime
import re

# Database connection parameters
DB_NAME = "Lender"
DB_USER = "lender"
DB_PASSWORD = "lender1$"
DB_HOST = "localhost"
DB_PORT = "5432"

# Path to your txt file
txt_file_path = "pagos.txt"


def parse_txt_data(file_path):
    # Read the data, skipping the header line
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    # Skip the header
    data_lines = lines[1:]
    
    # Parse each line into a list of dictionaries
    payments = []
    for line in data_lines:
        # Split by tabs or multiple spaces
        fields = re.split(r'\t|\s+', line.strip())
        fields = [f for f in fields if f]  # Remove empty elements
        
        # Extract fields
        credito_id = int(fields[0])
        pago_id = int(fields[1])
        fecha = datetime.strptime(fields[2], '%Y-%m-%d').date()
        
        # Remove $ and convert to numeric
        monto = float(fields[3].replace('$', ''))
        
        payments.append({
            'pago_id': pago_id,
            'credito_id': credito_id,
            'fecha': fecha,
            'monto': monto
        })
    
    return payments

def insert_data_to_db(payments):
    try:
        # Connect to the database
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        cursor = conn.cursor()
        
        # Insert each payment
        for payment in payments:
            cursor.execute(
                """
                INSERT INTO public.pago (pago_id, credito_id, fecha, monto)
                VALUES (%s, %s, %s, %s);
                """,
                (payment['pago_id'], payment['credito_id'], payment['fecha'], payment['monto'])
            )
        
        # Commit transaction
        conn.commit()
        print(f"Successfully inserted {len(payments)} payments into the database.")
        
    except Exception as e:
        print(f"Error: {e}")
        if conn:
            conn.rollback()
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


if __name__ == "__main__":
    # Parse the txt file
    payments = parse_txt_data(txt_file_path)
    
    # Print summary of parsed data
    print(f"Parsed {len(payments)} payments from the file.")
    print("Sample data:")
    for i, payment in enumerate(payments[:3]):
        print(payment)
        if i >= 2:
            break
    
    # Confirm before inserting
    confirm = input("Do you want to insert this data into the database? (y/n): ")
    if confirm.lower() == 'y':
        insert_data_to_db(payments)
    else:
        print("Operation cancelled.")