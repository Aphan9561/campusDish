ORDERINGS = [
    'Home Line',
    'Oven',
    'Fire And Ice',
    'Pasta',
    'Global Exchange',
    'Pizza',
    'True Balance',
    'Deli',
    'Sandwich Lab',
    'Global Kitchen',
    'Under the Hood',
    'Main Ingredient',
    'Trattoria',
    'Greens & Grains',
    'Waffle Station',
    'Grill/Fryer',
    'Grill',
    'Vegan',
    'Bakery',
    'One World',
    'Soups',
    "Farmer's Market",
    'Salad Bar'
]

def station_ordering_key(station_name: str) -> int:
    '''
    Returns an integer used to sort station names by relevance (basically Eric's personal preferences 😋)
    '''
    try:
        return ORDERINGS.index(station_name)
    except ValueError:# if 
        print(f"ValueError (NON-BREAKING) on station orderings. Key {station_name} is not in list")
        return -1