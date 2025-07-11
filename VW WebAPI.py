from weconnect import WebAPI
from credentials import USER, PASSWORD, S_PIN

# Initialisiere API
api = WebAPI(USER, PASSWORD, S_PIN)

# Fahrzeugliste abrufen
vehicles = api.get_vehicles()
vin = vehicles[0]['vin']  # VIN des ersten Fahrzeugs

# Standort abrufen
position = api.get_position(vin)
latitude = position['data']['latitude']
longitude = position['data']['longitude']

# Ladezustand abrufen
charger = api.get_charger(vin)
soc = charger['batteryStatus']['stateOfCharge']['content']

print(f"Standort: {latitude}, {longitude}")
print(f"SoC: {soc}%")
