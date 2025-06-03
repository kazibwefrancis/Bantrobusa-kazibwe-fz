class AddressFormatter:
    def format_address(self, street, city, state, zip_code, country="USA"): # country has a default value
        
        address_lines = [
            street,
            f"{city}, {state} {zip_code}",
            country
        ]
        return "\n".join(address_lines)

# Create an instance
formatter = AddressFormatter()

# Format a US address (country defaults to "USA")
address1 = formatter.format_address("123 Main St", "Anytown", "CA", "90210")
print("Shipping Address 1:")
print(address1)
# Output:
# Shipping Address 1:
# 123 Main St
# Anytown, CA 90210
# USA

print("\n") # For spacing

# Format an international address
address2 = formatter.format_address("456 Oak Rd", "Otherville", "ON", "M5V 2E8", country="Canada")
print("Shipping Address 2:")
print(address2)
# Output:
# Shipping Address 2:
# 456 Oak Rd
# Otherville, ON M5V 2E8
# Canada
