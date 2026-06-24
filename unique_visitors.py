visitors = ["ali", "sara", "ali", "hamza", "sara", "noor"]

# Convert list to set to remove duplicates
unique_visitors = list(set(visitors))

print(f"Unique visitors: {unique_visitors}")
print(f"Total unique count: {len(unique_visitors)}")