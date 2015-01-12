__author__ = 'Leenix'

# Mapping between data id keys and Thingspeak fields
KEY_MAP = {
    "air_temp": "field1",
    "wall_temp": "field2",
    "surface_temp": "field3",
    "case_temp": "field4",
    "humidity": "field5",
    "illuminance": "field6",
    "sound": "field7",
    "battery": "field8"
}

# Mapping between unit ID and Thingspeak channel
CHANNEL_MAP = {
    "<id_here>": "<API_KEY_HERE>",
}

# Thingspeak server address (change if using a custom server)
# default: "api.thingspeak.com:80"
SERVER_ADDRESS = "api.thingspeak.com:80"
