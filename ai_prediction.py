def predict_risk(distance, humidity, wind_speed):

    risk_score = 0

    if distance <= 5:
        risk_score += 50
    elif distance <= 10:
        risk_score += 30
    else:
        risk_score += 10

    if humidity >= 80:
        risk_score += 25
    elif humidity >= 60:
        risk_score += 15

    if wind_speed >= 30:
        risk_score += 25
    elif wind_speed >= 15:
        risk_score += 10

    print("\n===== AI RISK PREDICTION =====")
    print("Risk Score:", risk_score, "/ 100")

    if risk_score >= 70:
        risk_level = "HIGH"
    elif risk_score >= 40:
        risk_level = "MODERATE"
    else:
        risk_level = "LOW"

    print("Risk Level:", risk_level)

    return risk_level
