import random
print("=== WELCOME TO HANGMAN ===")
words = [
    "python",
    "coding",
    "laptop",
    "student",
    "project",
    "django"
]
print("\nChoose Difficulty")
print("1. Easy")
print("2. Medium")
print("3. Hard")
level = input("Enter choice: ")
if level == "1":
    attempts = 8
elif level == "2":
    attempts = 6
else:
    attempts = 4
secret_word = random.choice(words)
guessed = []
hint_used = False
while attempts > 0:
    display = ""
    complete = True
    for letter in secret_word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "
            complete = False
    print("\nWord:", display)
    print("Attempts Left:", attempts)
    print("Type HINT once if needed")
    if complete:
        print("\nYOU WON 🎉")
        break
    guess = input(
        "\nEnter Letter: "
    ).lower()
    if guess == "hint":
        if hint_used:
           print("Hint already used")
        else:
            for letter in secret_word:
                if letter not in guessed:
                   guessed.append(letter)
                   print("Hint revealed:"+letter)
                   hint_used = True
                   break
        continue
    if len(guess) != 1:
        print("Enter ONE letter")
        continue
    if guess in guessed:
        print("Already guessed")
        continue
    guessed.append(guess)
    if guess in secret_word:
       print("Correct ✅")
    else:
        attempts -= 1
        print("Wrong ❌")
if attempts == 0:
    print("\nGAME OVER")
    print("Correct Word:", secret_word)


