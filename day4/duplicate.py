raw_logs = ["ID01", "ID02", "ID01", "ID05", "ID02", "ID08", "ID01","ID08"]

unique_users = set(raw_logs)

print("Is ID05 in unique users?", "ID05" in unique_users)

print("Original log count:", len(raw_logs))
print("Unique user count:", len(unique_users))

print("Unique Users:", unique_users)
