import pandas as pd
df = pd.DataFrame({
    "Transmission": ["Automatic", "Manual", "Automatic", "Manual"],
    "Color": ["Red", "Blue", "Green", "Red"]
})
df["Transmission"] = df["Transmission"].map({
    "Manual": 0,
    "Automatic": 1
})
df = pd.get_dummies(df, columns=["Color"], drop_first=True)

print(df)