import json
from jsonschema import validate
import jsonschema

# Load the schema
with open('./schema.json', 'r') as file:
    schema = json.load(file)

# Sample valid data
with open('./valid_data.json', 'r') as file:
    valid_data = json.load(file)

# Sample invalid data (with deliberate errors)
with open('./invalid_data.json', 'r') as file:
    invalid_data = json.load(file)

# Validation function to print all errors
def validate_data(data, schema):
    errors = list(jsonschema.Draft7Validator(schema).iter_errors(data))  # List all errors
    if not errors:
        print("Validation successful! Data is valid.")
        return True
    else:
        print("Validation errors:")
        for error in errors:
            print(f"Path: {' -> '.join(str(x) for x in error.path)}")
            print(f"Message: {error.message}")
            print("-" * 50)
        return False

# Test validation
print("Validating valid data:")
validate_data(valid_data, schema)

print("\nValidating invalid data:")
validate_data(invalid_data, schema)
