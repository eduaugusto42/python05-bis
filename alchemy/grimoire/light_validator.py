def validate_ingredients(ingredients: str) -> str:
    allowed = ["earth", "air", "fire", "water"]
    lower = ingredients.lower()
    valid = any(allowed_item in lower for allowed_item in allowed)
    status = "VALID" if valid else "INVALID"
    return f"{ingredients} - {status}"
