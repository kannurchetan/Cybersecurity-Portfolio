import pandas as pd

def risk_score(row):
    score = 0
    
    if row["action"] == "login_failed":
        score += 20
    if row["action"] == "download" and row["value"] > 5000:
        score += 50
    if row["user"] == "alice":
        score += 5
    
    return score

df = pd.read_csv("dataset/sample_logs.csv")
df["risk_score"] = df.apply(risk_score, axis=1)

df.to_csv("risk_output.csv", index=False)
print("Risk scoring completed. Output saved as risk_output.csv")
