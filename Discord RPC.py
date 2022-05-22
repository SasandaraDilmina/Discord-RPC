import rpc
import time
from time import mktime

print("Discord RPC Script. Made By Sasandara Dilmina")
client_id = '937680281945669752'  # Your application's client ID.
rpc_obj = rpc.DiscordIpcClient.for_platform(client_id)
print("Connected to Discord RPC. Made By Sasandara Dilmina")

time.sleep(5)
start_time = mktime(time.localtime())
while True:
    activity = {
            "state": "By Sasandara Dilmina",  # Enter the State
            "details": "45K+ Downloads",  # Enter the Details
            "timestamps": {
                "start": start_time
            },
            "assets": {
                "small_text": "The Meteorite",  # Enter the Small Text
                "small_image": "logo",  # Name of the Small Image
                "large_text": "The Meteorite",  # Enter the Large Text
                "large_image": "logo"  # Name of the Large Image
            }
        }
    rpc_obj.set_activity(activity)
    time.sleep(900)
