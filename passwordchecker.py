import re
import random
import string


def strength_meter(score):
    bars = "█" * (score * 2)
    empty = "░" * (10 - score * 2)

    percentage = score * 20

    return f"[{bars}{empty}] {percentage}%"


def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add uppercase letters.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add lowercase letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Add numbers.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Add special characters.")

    if score == 5:
        level = "Strong"
    elif score >= 3:
        level = "Medium"
    else:
        level = "Weak"

    return level, score, feedback


def ask(question):
    while True:
        answer = input(question + " (y/n): ").lower().strip()

        if answer in ["y", "yes"]:
            return True

        elif answer in ["n", "no"]:
            return False

        print("Enter y or n.")


def generate_password():
    while True:
        try:
            length = int(
                input("\nPassword Length (8–20): ")
            )

            if 8 <= length <= 20:
                break

            print("Length must be between 8 and 20.")

        except:
            print("Enter numbers only.")

    use_number = ask("Use numbers")
    use_upper = ask("Use mixed uppercase/lowercase")
    use_special = ask("Use special characters")

    chars = string.ascii_lowercase

    if use_upper:
        chars += string.ascii_uppercase

    if use_number:
        chars += string.digits

    if use_special:
        chars += "!@#$%^&*()_+-=[]{}"

    password = ""

    while True:
        password = "".join(
            random.choice(chars)
            for _ in range(length)
        )

        level, score, _ = check_password_strength(password)

        if score >= 3:
            break

    return password


def menu():

    while True:

        print("\n" + "=" * 50)
        print("PASSWORD STRENGTH CHECKER & GENERATOR")
        print("=" * 50)

        print("\n1 → Check Password")
        print("2 → Generate Password")
        print("3 → Exit")

        choice = input("\nSelect option: ").strip()

        if choice == "1":

            password = input(
                "\nEnter Password: "
            )

            level, score, feedback = (
                check_password_strength(password)
            )

            print("\nPassword:", password)
            print("Strength:", level)
            print("Meter:", strength_meter(score))

            if feedback:
                print("\nSuggestions:")

                for i in feedback:
                    print("•", i)

        elif choice == "2":

            password = generate_password()

            level, score, _ = (
                check_password_strength(password)
            )

            print("\nGenerated Password:")
            print(password)

            print("\nStrength:", level)
            print(
                "Meter:",
                strength_meter(score)
            )

        elif choice == "3":

            print(
                "\nExiting Program..."
            )

            print(
                "Thank you for using Password Tool"
            )

            break

        else:
            print(
                "\nInvalid Option."
            )


if __name__ == "__main__":
    menu()