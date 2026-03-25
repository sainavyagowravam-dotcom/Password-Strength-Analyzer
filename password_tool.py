from zxcvbn import zxcvbn

print("=== Password Strength Analyzer & Wordlist Generator ===")

# PASSWORD INPUT
password = input("Enter a password to analyze: ")

result = zxcvbn(password)
score = result['score']

print("\nPassword Strength Score (0-4):", score)

if score == 0:
    print("Very Weak Password")
elif score == 1:
    print("Weak Password")
elif score == 2:
    print("Medium Password")
elif score == 3:
    print("Strong Password")
else:
    print("Very Strong Password")

print("\nSuggestions:")
for s in result['feedback']['suggestions']:
    print("-", s)

# WORDLIST GENERATOR
print("\n--- Custom Wordlist Generator ---")
name = input("Enter your name: ")
year = input("Enter birth year: ")
pet = input("Enter pet name: ")

wordlist = [
    name,
    name + year,
    pet,
    pet + year,
    name + pet,
    name + "123",
    name + "@" + year,
    name.capitalize() + year
]

with open("custom_wordlist.txt", "w") as f:
    for word in wordlist:
        f.write(word + "\n")

print("\nWordlist saved as custom_wordlist.txt")