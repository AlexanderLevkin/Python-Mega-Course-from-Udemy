def water_state(temperature):
    if temperature <= 0:
        return "Solid"
    elif 0 < temperature < 100:
        return "Liquid"
    elif temperature >= 100:
        return "Gas"
