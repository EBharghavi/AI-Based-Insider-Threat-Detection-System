def generate_alerts(df):
    threats = df[df["Anomaly"] == "Threat"]
    
    if len(threats) > 0:
        print("⚠️ ALERT! Suspicious Employees Detected:")
        print(threats[["employee_id", "login_hour", "download_mb"]])
    else:
        print("✅ No Threats Detected")