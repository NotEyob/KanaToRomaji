import KanaINP

print("Hello there! ")
while True:
    choice = input("Which mode would you like to go into? Hiragana, or Katakana? ").lower().strip()
    if choice == "hiragana":
        choice2 = input("Would you like a quick CLI translation? (Yes/No) ").lower().strip()
        if choice2 == "yes":
            KanaINP.hiragana()
        else:
            continue
    elif choice == "katakana":
        choice3 = input("Would you like a quick CLI translation? (Yes/No) ").lower().strip()
        if choice3 == "yes":
            KanaINP.katakana()
        else:
            continue
    else:
        print("Nani?")
        continue
