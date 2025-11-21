# --- Clothing Recommendation Program ---

# Define the temperature thresholds for easy reading and changing
HOT_ENOUGH_FOR_TSHIRT = 22  # e.g., anything 22°C and above is T-shirt weather
COLD_ENOUGH_FOR_JACKET = 15 # e.g., anything 15°C and below needs a jacket

# 1. Get user input
try:
    # Use input() to get text and int() to convert it to a number
    temperature = int(input("What is the current outdoor temperature (°C)? "))
except ValueError:
    print("Invalid input. Please enter a whole number for the temperature.")
    exit()

print("\n--- Clothing Recommendation ---")

# 2. Use conditional statements
if temperature >= HOT_ENOUGH_FOR_TSHIRT:
    # Condition 1: Hot enough for a T-shirt
    print(f"☀️ At {temperature}°C, it's **HOT ENOUGH FOR LIGHT T-SHIRTS**!")
    print("Recommendation: Enjoy the sunshine! Maybe wear shorts.")

elif temperature <= COLD_ENOUGH_FOR_JACKET:
    # Condition 2: Cold enough for a jacket
    print(f"🥶 At {temperature}°C, it's **COLD ENOUGH FOR JACKETS**.")
    print("Recommendation: Better grab a warm jacket or a coat.")

else:
    # Condition 3: The temperature is in between the two thresholds (e.g., 16°C to 21°C)
    print(f"😎 At {temperature}°C, the weather is **MILD/IN-BETWEEN**.")
    print("Recommendation: A light sweater, hoodie, or a light jacket might be perfect.")

print("---------------------------------")