import supabase_utils

from supabase_utils import create_record, read_record_by_id, read_records, update_record, delete_record


# Create a new record
new_record = {"name": "Wai", "email": "wai@example.com"}
create_record(new_record)

# Read all records
read_records()

# Read a specific record by ID
read_record_by_id(1)

# Update a record by ID
updated_data = {"name": "Harry", "email": "harry@example.com"}
update_record(1, updated_data)

    # Delete a record by ID
    #delete_record(1)