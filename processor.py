import json

class InvalidInputError(Exception):
    pass

def validate_input(data):
    if not isinstance(data, dict):
        raise InvalidInputError("Input must be a dictionary")
    if 'amount' not in data or not isinstance(data['amount'], (int, float)):
        raise InvalidInputError("Input must contain a numeric 'amount' field")
    if 'currency' not in data or not isinstance(data['currency'], str):
        raise InvalidInputError("Input must contain a string 'currency' field")

def process_transaction(data):
    validate_input(data)
    # Additional processing logic goes here
    return json.dumps({"status": "success", "data": data})

if __name__ == '__main__':
    sample_data = {"amount": 100, "currency": "BTC"}
    try:
        result = process_transaction(sample_data)
        print(result)
    except InvalidInputError as e:
        print(f"Error: {e}")