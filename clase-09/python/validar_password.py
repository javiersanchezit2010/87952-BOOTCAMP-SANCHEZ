
def validar_password(password):
    if len(password) < 10:
        return {"valid": False, "message": "Password must be at least 10 characters"}

    if len(password) > 20:
        return {"valid": False, "message": "Password must be at most 20 characters"}

    if " " in password:
        return {"valid": False, "message": "Password must not contain spaces"}

    if not any(c.isalpha() for c in password):
        return {"valid": False, "message": "Password must contain letters"}

    if not any(c.isdigit() for c in password):
        return {"valid": False, "message": "Password must contain numbers"}

    if not any(c.isupper() for c in password):
        return {"valid": False, "message": "Password must contain uppercase letters"}

    if not any(c.islower() for c in password):
        return {"valid": False, "message": "Password must contain lowercase letters"}

    if not any(not c.isalnum() for c in password):
        return {"valid": False, "message": "Password must contain a special symbol"}

    return {"valid": True, "message": "Password is valid"}