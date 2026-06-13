import os

for i in range(1, 6):

    ip = f"127.0.0.{i}"

    response = os.system(
        f"ping -c 1 -W 1 {ip} > /dev/null 2>&1"
    )

    if response == 0:
        print(f"{ip} -> Online")

    else:
        print(f"{ip} -> Offline")
