import tkinter as tk
from tkinter import messagebox
from zxcvbn import zxcvbn

def analyze_password():
    password = password_entry.get()
    name = name_entry.get()
    year = year_entry.get()
    pet = pet_entry.get()

    if not password or not name or not year or not pet:
        messagebox.showerror("Error", "Please fill all fields")
        return

    result = zxcvbn(password)
    score = result['score']
    strength = ["Very Weak", "Weak", "Medium", "Strong", "Very Strong"]

    output = f"Password Strength: {strength[score]}\n\nSuggestions:\n"
    for s in result['feedback']['suggestions']:
        output += "- " + s + "\n"

    # Wordlist generation (c & d included)
    wordlist = []
    wordlist.append(name)
    wordlist.append(name + year)
    wordlist.append(name + "123")
    wordlist.append(pet)
    wordlist.append(pet + year)

    leet_name = name.replace("a", "@").replace("o", "0").replace("i", "1").replace("e", "3").replace("s", "5")
    wordlist.append(leet_name)
    wordlist.append(leet_name + year)

    wordlist.append(name + "@" + year)
    wordlist.append(name + "_" + year)

    with open("custom_wordlist.txt", "w") as f:
        for word in set(wordlist):
            f.write(word + "\n")

    messagebox.showinfo("Result", output + "\n\nWordlist saved as custom_wordlist.txt")

root = tk.Tk()
root.title("Password Strength Analyzer")
root.geometry("400x400")

tk.Label(root, text="Password Strength Analyzer", font=("Arial", 14, "bold")).pack(pady=10)

tk.Label(root, text="Enter Password").pack()
password_entry = tk.Entry(root, show="*", width=30)
password_entry.pack()

tk.Label(root, text="Your Name").pack()
name_entry = tk.Entry(root, width=30)
name_entry.pack()

tk.Label(root, text="Birth Year").pack()
year_entry = tk.Entry(root, width=30)
year_entry.pack()

tk.Label(root, text="Pet Name").pack()
pet_entry = tk.Entry(root, width=30)
pet_entry.pack()

tk.Button(root, text="Analyze Password", command=analyze_password, bg="green", fg="white").pack(pady=20)

root.mainloop()