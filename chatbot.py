while True:

    message = input("\nYou: ").lower().strip()


    # ---------------- GREETINGS ----------------

    greetings = [
        "hi",
        "hello",
        "hey",
        "namaste",
        "namaskar",
        "namste"
    ]


    if message in greetings:

        print("\nBot: Hello 👋")
        print("Bot: Are you bored?")
        print("Bot: What are you doing today?")
        print("Bot: Can I help you?")


    # ---------------- OPTIONAL WISHES ----------------

    elif message == "good morning":

        print("\nBot: Good Morning ☀️")
        print("Bot: Are you bored?")
        print("Bot: What are you doing today?")
        print("Bot: Can I help you?")


    elif message == "good afternoon":

        print("\nBot: Good Afternoon 🌤️")
        print("Bot: Are you bored?")
        print("Bot: What are you doing today?")
        print("Bot: Can I help you?")


    elif message == "good night":

        print("\nBot: Good Night 🌙")
        print("Bot: Are you bored?")
        print("Bot: What are you doing today?")
        print("Bot: Can I help you?")


    # ---------------- BORED ----------------

    elif "bored" in message:

        print("\nBot: Let's refresh your mood 😊")
        print("Bot: Choose one:")
        print("• songs")
        print("• books")
        print("• joke")


    elif "songs" in message:

        print("\nBot: Relaxing songs 🎵")
        print("1. Weightless")
        print("2. River Flows In You")
        print("3. Perfect")


    elif "books" in message:

        print("\nBot: Recommended books 📚")
        print("1. Atomic Habits")
        print("2. The Alchemist")


    elif "joke" in message:

        print("\nBot: Joke 1")
        print("Why do programmers prefer dark mode?")
        print("Because light attracts bugs 😄")

        print("\nBot: Joke 2")
        print("Why was the computer cold?")
        print("Because it left its Windows open 😂")


    # ---------------- WHAT ARE YOU DOING ----------------

    elif "doing" in message:

        print("\nBot: Nice 😊")
        print("Bot: Keep doing your work.")
        print("Bot: Well done.")
        print("Bot: Keep learning.")
        print("Bot: Small progress matters.")


    # ---------------- HELP ----------------

    elif "help" in message:

        print("\nBot: Tell me where you are stuck.")
        print("Bot: Follow my guidance.")
        print("Bot: Explain your problem.")
        print("Bot: I'll help step by step.")


    # ---------------- EXIT ----------------

    elif message in ["bye", "exit"]:

        print("\nBot: Goodbye 👋")

        break


    # ---------------- DEFAULT ----------------

    else:

        print("\nBot: Sorry, I didn't understand.")
        print("Bot: Try saying hi.")
