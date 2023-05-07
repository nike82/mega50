GAS = 100
LIQUID_SOLID = 0


def water_state(temperature):
    if LIQUID_SOLID < temperature < GAS:
        return "liquid"
    elif temperature <= LIQUID_SOLID:
        return "solid"
    return "gas"
