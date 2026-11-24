def send_alert(risk_level):

    print("\n===== VAJRAWATCH ALERT SYSTEM =====")

    if risk_level == "HIGH":
        print("DANGER! LIGHTNING RISK DETECTED!")
        print("PLEASE LEAVE THE OPEN FIELD.")
        print("MOVE TO A SAFE, ENCLOSED SHELTER.")

    elif risk_level == "MODERATE":
        print("CAUTION! THUNDERSTORM ACTIVITY.")
        print("AVOID TREES AND OPEN AREAS.")

    else:
        print("LOW RISK.")
        print("CONTINUE MONITORING WEATHER.")

    print("===================================")


# Test alerts
send_alert("HIGH")
