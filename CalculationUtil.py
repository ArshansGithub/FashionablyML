import random
random.seed()

TSHIRT_STANDARD_CO2_KG = 7
LONGSHIRT_STANDARD_CO2_KG = 10
SPORTSHIRT_STANDARD_C02_KG = 8

JEAN_STANDARD_CO2_KG = 33.4
CARGOPANT_STANDARD_CO2_KG = 18
CARGOSHORT_STANDARD_CO2_KG = 16
SPORTSHORT_STANDARD_C02_KG = 8
SWEATPANTS_STANDARD_CO2 = 19.4

HOODIE_STANDARD_CO2_KG = 18
JACKET_STANDARD_CO2_KG = 20
DENIMJACKET_STANDARD_CO2_KG = 35

TENSHOE_STANDARD_CO2_KG = 14
BOOTS_STANDARD_CO2_KG = 20

def getCO2(input):
    switchCO2 = {
        "tshirt": TSHIRT_STANDARD_CO2_KG,
        "longshirt": LONGSHIRT_STANDARD_CO2_KG,
        "sportshirt": SPORTSHIRT_STANDARD_C02_KG,
        "jeans": JEAN_STANDARD_CO2_KG,
        "cargopant": CARGOPANT_STANDARD_CO2_KG,
        "cargoshort": CARGOSHORT_STANDARD_CO2_KG,
        "sportshort": SPORTSHIRT_STANDARD_C02_KG,
        "sweatpant": SWEATPANTS_STANDARD_CO2,
        "hoodie": HOODIE_STANDARD_CO2_KG,
        "jacket": JACKET_STANDARD_CO2_KG,
        "denimjacket": DENIMJACKET_STANDARD_CO2_KG,
        "tennis": TENSHOE_STANDARD_CO2_KG,
        "boots": BOOTS_STANDARD_CO2_KG
    }
    return switchCO2.get(input, 0)

TSHIRT_STANDARD_H20_LITER = 2700
LONGSHIRT_STANDARD_H20_LITER = 2800
SPORTSHIRT_STANDARD_H20_LITER = 100

JEAN_STANDARD_H20_LITER = 10000
CARGOPANT_STANDARD_H20_LITER = 8500
CARGOSHORT_STANDARD_H20_LITER = 8000
SPORTSHORT_STANDARD_H20_LITER = 100
SWEATPANTS_STANDARD_H20_LITER = 10000

HOODIE_STANDARD_H20_LITER = 5000
JACKET_STANDARD_H20_LITER = 7500
DENIMJACKET_STANDARD_H20_LITER = 8000

TENSHOE_STANDARD_H20_LITER = 4000
BOOTS_STANDARD_H20_LITER = 8000

def getH20(input):
    switchH20 = {
        "tshirt": TSHIRT_STANDARD_H20_LITER,
        "longshirt": LONGSHIRT_STANDARD_H20_LITER,
        "sportshirt": SPORTSHIRT_STANDARD_H20_LITER,
        "jeans": JEAN_STANDARD_H20_LITER,
        "cargopant": CARGOPANT_STANDARD_H20_LITER,
        "cargoshort": CARGOSHORT_STANDARD_H20_LITER,
        "sportshort": SPORTSHORT_STANDARD_H20_LITER,
        "sweatpant": SWEATPANTS_STANDARD_H20_LITER,
        "hoodie": HOODIE_STANDARD_H20_LITER,
        "jacket": JACKET_STANDARD_H20_LITER,
        "denimjacket": DENIMJACKET_STANDARD_H20_LITER,
        "tennis": TENSHOE_STANDARD_H20_LITER,
        "boots": BOOTS_STANDARD_H20_LITER
    }
    return switchH20.get(input, 0)

TSHIRT_STANDARD_ELEC_KWH = 20
LONGSHIRT_STANDARD_ELEC_KWH = 25
SPORTSHIRT_STANDARD_ELEC_KWH = 25

JEAN_STANDARD_ELEC_KWH = 50
CARGOPANT_STANDARD_ELEC_KWH = 40
CARGOSHORT_STANDARD_ELEC_KWH = 35
SPORTSHORT_STANDARD_ELEC_KWH = 25
SWEATPANTS_STANDARD_ELEC_KWH = 5

HOODIE_STANDARD_ELEC_KWH = 35
JACKET_STANDARD_ELEC_KWH = 40
DENIMJACKET_STANDARD_ELEC_KWH = 50

TENSHOE_STANDARD_ELEC_KWH = 30
BOOTS_STANDARD_ELEC_KWH = 50

def getElec(input):
    switchElec = {
        "tshirt": TSHIRT_STANDARD_ELEC_KWH,
        "longshirt": LONGSHIRT_STANDARD_ELEC_KWH,
        "sportshirt": SPORTSHIRT_STANDARD_ELEC_KWH,
        "jeans": JEAN_STANDARD_ELEC_KWH,
        "cargopant": CARGOPANT_STANDARD_ELEC_KWH,
        "cargoshort": CARGOSHORT_STANDARD_ELEC_KWH,
        "sportshort": SPORTSHORT_STANDARD_ELEC_KWH,
        "sweatpant": SWEATPANTS_STANDARD_ELEC_KWH,
        "hoodie": HOODIE_STANDARD_ELEC_KWH,
        "jacket": JACKET_STANDARD_ELEC_KWH,
        "denimjacket": DENIMJACKET_STANDARD_ELEC_KWH,
        "tennis": TENSHOE_STANDARD_ELEC_KWH,
        "boots": BOOTS_STANDARD_ELEC_KWH
    }
    return switchElec.get(input, 0)

def calculateCO2(items):
    total = 0
    for item in items:
        total += getCO2(item)
    return total

def calculateH20(items):
    total = 0
    for item in items:
        total += getH20(item)
    return total

def calculateElec(items):
    total = 0
    for item in items:
        total += getElec(item)
    return total

# Takes simple input in the form of a string containing
# all the parts of the outfit seperated by spaces
# ex. "boots cargoshort sportshirt jacket"
def getProductionCost(items):
    output = {
        calculateCO2(items),
        calculateH20(items),
        calculateElec(items)
    }
    return output

FUN_FACTS = {
    "Washing clothes releases over 500,000 tons of microfibers into the ocean each year! That's about the same as 500 billion plastic bottles",
    "The fashion industry is responsible for about 10 percent of carbon emissions",
    "25 percent of global chemical output originates from the textile industry.",
    "A t-shirt made in India produces 50 percent more carbon than a t-shirt made in Vietnam."
}

CHEMICALS_JEANS = {
    "sodium hypochlorite",
    "sodium hydroxide",
    "polyurethanic resins",
    "formaldehyde",
    "hydrochloric acid",
    "polyvinyl alcohol",
    "styrolmalec acid copolymers"
    "chlorine"
}

CHEMICALS_SPORTS = {
    "pthalates"
}

CHEMICALS_GENERAL = {
    "perfluorohexanesulfonic acid",
    "perfluorooctanesulfonic acid",
    "perflurooctanoic acid",
    "perfluorocarboxylic acid",
    "perfluorononanoic acid",
    "nonylphenol ethoxylates"
}

CO2_PER_KWH = 6.99 * pow(10, -4) * pow(10, -3)

WATER_PER_ITEM_PER_YEAR = 37.5
ELEC_PER_ITEM_PER_YEAR = 9.75
CO2_PER_ITEM_PER_YEAR = 9.75 * CO2_PER_KWH

def getUpkeepCost(items, years):
    output = {
        len(items) * WATER_PER_ITEM_PER_YEAR * years,
        len(items) * ELEC_PER_ITEM_PER_YEAR * years,
        len(items) * CO2_PER_ITEM_PER_YEAR * years
    }
    return output

def getRandomFromArray(arr):
    return arr[random.randint(0, len(arr))]

def getChemicals(items):
    chemicals = []
    i = 0
    if "jeans" in items:
        for j in range(random.randint(0, 6)):
            chemicals[i] = CHEMICALS_JEANS[j]
            i = i + 1
    if ("sportsshirt" in items) or ("sportsshort" in items):
            chemicals[i] = CHEMICALS_SPORTS[0]
            i = i + 1
    
    for j in range(random.randint(2, 6)):
        chemicals[i] = CHEMICALS_GENERAL[j]
        i = i + 1
    return chemicals

def getTotalCosts(input, years):
    items = input.split()
    productionCost = getProductionCost(items)
    upkeepCost = getUpkeepCost(items, years)
    chemicals = getChemicals(items)
    funfacts = getRandomFromArray(FUN_FACTS)
    output = {
        productionCost[0] + upkeepCost[0],
        productionCost[1] + upkeepCost[1],
        productionCost[2] + upkeepCost[2],
        funfacts,
        chemicals
    }
    return output