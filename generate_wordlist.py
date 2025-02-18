import random
import string

# Step 1: Define a small list of common passwords.
common_passwords = [
    "123456", "password", "12345678", "qwerty", "123456789", "12345", "1234",
    "111111", "1234567", "dragon", "123123", "baseball", "abc123", "football",
    "monkey", "letmein", "shadow", "master", "666666", "qwertyuiop", "123321",
    "mustang", "1234567890", "michael", "654321", "superman", "1qaz2wsx",
    "7777777", "121212", "000000", "loveme", "trustno1", "starwars", "hello",
    "freedom", "whatever", "qazwsx", "qwerty123", "batman", "zaq1zaq1"
]

def generate_variations(base_list, target_count=2000):
    # Start with the base passwords
    variations = set(base_list)
    # Keep generating new passwords until we have 'target_count' unique ones.
    while len(variations) < target_count:
        # Pick a random password from the base list.
        base = random.choice(base_list)
        # Generate a random suffix of 1 to 4 digits.
        suffix_length = random.randint(1, 4)
        suffix = ''.join(random.choices(string.digits, k=suffix_length))
        # Combine the base password with the suffix.
        variation = base + suffix
        variations.add(variation)
    return list(variations)

# Generate 2000 unique passwords.
all_passwords = generate_variations(common_passwords, 2000)

# Step 3: Write the generated passwords to a file.
with open("wordlists/common.txt", "w", encoding="utf-8") as f:
    for pwd in all_passwords:
        f.write(pwd + "\n")

print("Wordlist generated with", len(all_passwords), "passwords in 'wordlists/common.txt'.")
