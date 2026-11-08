import random

def generate_yearly_lottery_codes(total_days=365):
    yearly_entries = {}
    
    for day in range(1, total_days + 1):
        # Generates a random integer from 0000 to 9999
        # :04d ensures the number always outputs as 4 digits with leading zeros
        lottery_code = f"{random.randint(0, 9999):04d}"
        
        # Store using the day number as the key
        yearly_entries[f"Day {day}"] = lottery_code
        
    return yearly_entries

# Generate 365 entries
lottery_calendar = generate_yearly_lottery_codes(365)

# Print a small sample (first 10 days) to see the results
print("--- First 10 Days Sample ---")
for day, code in list(lottery_calendar.items())[:10]:
    print(f"{day}: {code}")

# Total verification check
print(f"\nTotal entries generated: {len(lottery_calendar)}")
