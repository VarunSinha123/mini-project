# utils/security.py
def safe_str_cmp(a: str, b: str) -> bool:
    """
    Replace Werkzeug's deprecated safe_str_cmp
    """
    if len(a) != len(b):
        return False
    return a == b

# Then modify your LoginManager initialization to use this function
from utils.security import safe_str_cmp