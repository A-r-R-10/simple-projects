from datetime import datetime
from json import dump, load, JSONDecodeError


def convert_time_to_dict():
    now = datetime.now()
    return {
        "year": now.year,
        "month": now.month,
        "day": now.day,
        "hour": now.hour,
        "minute": now.minute,
        "second": now.second
    }


def log_creator(contact_id, operation_type):
    log_entry = {
        "date and time": convert_time_to_dict(),
        "operation type": operation_type,
        "contact_id": contact_id
    }

    # Read existing logs
    try:
        with open("log.json") as file:
            logs = load(file)
    except (FileNotFoundError, JSONDecodeError):
        logs = []

    # Append new log
    logs.append(log_entry)

    # Write back to file
    with open("data/log.json", "w") as file:
        dump(logs, file, indent=4)
