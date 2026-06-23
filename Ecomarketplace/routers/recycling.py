# Quick preview of how the tracking and educational endpoints look
@app.get("/carbon-savings/{user_id}")
async def get_carbon_savings(user_id: int):
    return {"user_id": user_id, "carbon_offset_kg": 12.5, "trees_equivalent": 1.2}

@app.get("/education/briquettes-vs-charcoal")
async def get_educational_content():
    return {
        "topic": "Carbonized Biomass Briquettes",
        "benefit_1": "Smoke-free alternative reducing respiratory risks",
        "benefit_2": "Higher thermal efficiency meaning it burns longer than traditional charcoal"
    }