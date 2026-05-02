def validate_ingredients(ingredients: str) -> str:
    from .light_spellbook import light_spell_allowed_ingredients
    allowed: list[str] = light_spell_allowed_ingredients()
    for ing in allowed:
        if ing in ingredients.lower():
            return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
