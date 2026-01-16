

# epostanın basit, temel formatta kontrlünü yapar bu kısım

def validate_email(email: str) -> bool:
    if not email:
        return False
    return "@" in email and "." in email
