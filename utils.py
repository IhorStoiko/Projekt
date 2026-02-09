from datetime import datetime

def validate_date(date_str, fmt="%Y-%m-%d"):
    """
    Validates and parses a date string.

    Args:
        date_str (str): Date string to validate.
        fmt (str, optional): Expected date format (default is "%Y-%m-%d").

    Returns:
        datetime.datetime or None: Parsed datetime object if valid, otherwise None.
    """
    try:
        return datetime.strptime(date_str, fmt)
    except ValueError:
        return None


def format_currency(amount):
    """
    Formats a numeric value as a currency string.

    Args:
        amount (float): Numeric value to format.

    Returns:
        str: Formatted string in the form "$123.45".
    """
    return f"${amount:.2f}"

