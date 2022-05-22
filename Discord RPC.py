import rpc
import time
from time import mktime

print("Discord RPC Script. Made By Sasandara Dilmina")
client_id = '937680281945669752'  # Client ID
rpc_obj = rpc.DiscordIpcClient.for_platform(client_id)
print("Connected to Discord RPC. Made By Sasandara Dilmina")

time.sleep(5)
start_time = mktime(time.localtime())
while True:
    activity = {
            "state": "Your State",  # State
            "details": "Your Details",  # Details
            "timestamps": {
                "start": start_time
            },
            "assets": {
                "small_text": "Your Small Text",  # Small Text
                "small_image": "Your Small Image",  # Small Image
                "large_text": "Your Large Text",  # Large Text
                "large_image": "Your Large Image"  # Name of the Large Image
            }
        }
    rpc_obj.set_activity(activity)
    time.sleep(900)
