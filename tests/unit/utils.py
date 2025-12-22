import re
from typing import Optional, Union
import uuid
import hashlib

def validate_email(email: str) -> bool:
    """
    Validates an email address using a regular expression.

    Args:
        email: The email address to validate.

    Returns:
        True if the email is valid, False otherwise.
    """
    email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(email_regex, email))

def generate_unique_id() -> str:
    """
    Generates a unique ID using UUID.

    Returns:
        A unique ID as a string.
    """
    return str(uuid.uuid4())

def hash_string(input_string: str) -> str:
    """
    Hashes a string using SHA-256.

    Args:
        input_string: The string to hash.

    Returns:
        The SHA-256 hash of the string.
    """
    hashed_string = hashlib.sha256(input_string.encode('utf-8')).hexdigest()
    return hashed_string

def format_phone_number(phone_number: str) -> str:
    """
    Formats a phone number to a standard format (e.g., +1-555-123-4567).

    Args:
        phone_number: The phone number to format.

    Returns:
        The formatted phone number.  Returns the original if formatting fails.
    """
    try:
        # Remove all non-digit characters
        digits_only = re.sub(r'\D', '', phone_number)

        # Check if it's a North American number (10 or 11 digits with a leading 1)
        if len(digits_only) == 11 and digits_only[0] == '1':
            country_code = '+1'
            area_code = digits_only[1:4]
            prefix = digits_only[4:7]
            line_number = digits_only[7:]
        elif len(digits_only) == 10:
            country_code = '+1'
            area_code = digits_only[0:3]
            prefix = digits_only[3:6]
            line_number = digits_only[6:]
        else:
            return phone_number # Return the original if we can't standardize.

        return f"{country_code}-{area_code}-{prefix}-{line_number}"
    except:
        return phone_number

def convert_to_float(value: Union[str, int, float, None]) -> Optional[float]:
    """
    Converts a value to a float.

    Args:
        value: The value to convert.

    Returns:
        The float representation of the value, or None if the value cannot be converted.
    """
    if value is None:
        return None
    try:
        return float(value)
    except (ValueError, TypeError):
        return None