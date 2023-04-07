cheeses = ["cheddar", "gouda", "camembert"]

def roll_call_dwarves(dwarf_names):
    for index in range(len(dwarf_names)):
        print(f"{index + 1}. {dwarf_names[index]}")

def summon_captain_planet(planeteer_calls):
    return [f"{call.capitalize()}!" for call in planeteer_calls]

def long_planeteer_calls(planeteer_calls):
    for call in planeteer_calls:
        if len(call) > 4:
            return True
    return False

def find_the_cheese(foods):
    for food in foods:
        if food in cheeses:
            return food
        
    return None
