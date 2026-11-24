import random
import time

def detect_lightning():
    print("\n===== VAJRAWATCH =====")
    print("AI Lightning Safety System")
    print("-------------------------")

    distance = random.randint(1, 20)

    print("Simulated lightning distance:", distance, "km")

    if distance <= 5:
        print("WARNING: EXTREME LIGHTNING RISK!")
        print("Farmer Alert: MOVE TO SAFE SHELTER!")
    elif distance <= 10:
        print("WARNING: HIGH LIGHTNING RISK!")
        print("Avoid open fields immediately.")
    else:
        print("LOW RISK: Continue monitoring.")

    print("-------------------------")

while True:
    detect_lightning()
    time.sleep(5)
