import os

from supabase import Client, create_client

from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Initialize Supabase client using environment variables
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

TABLE_NAME = 'customers'

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def create_record(data: dict):
 try: 
        response = supabase.table(TABLE_NAME).insert(data).execute()
        print("Record created:", response)
        return response
 except Exception as e:
        print("Error creating record:", e)
        return None
        
def read_records():
    try:
        response = supabase.table(TABLE_NAME).select("*").execute()
        print("Records fetched:", response)
        return response
    except Exception as e:
        print("Error fetching records:", e)
        return None
    
def read_record_by_id(record_id : int):
    try:
        response = supabase.table(TABLE_NAME).select("*").eq("id", record_id).execute()
        print(f"Record with ID {record_id} fetched:", response)
        return response
    except Exception as e:
        print(f"Error fetching record with ID {record_id}:", e)
        return None
    
# UPDATE Operation (Update a record by ID)
def update_record(record_id: int, data: dict):
    try:
        response = supabase.table(TABLE_NAME).update(data).eq("id", record_id).execute()
        print(f"Record with ID {record_id} updated:", response)
        return response
    except Exception as e:
        print(f"Error updating record with ID {record_id}:", e)
        return None

# DELETE Operation (Delete a record by ID)
def delete_record(record_id: int):
    try:
        response = supabase.table(TABLE_NAME).delete().eq("id", record_id).execute()
        print(f"Record with ID {record_id} deleted:", response)
        return response
    except Exception as e:
        print(f"Error deleting record with ID {record_id}:", e)
        return None
