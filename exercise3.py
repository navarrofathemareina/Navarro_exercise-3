try:

    username = input("Enter username: ")
    age = input("Enter age: ")

    age = int(age)

    with open("users.txt", "a") as file:
        file.write(f"{username} - {age}\n")

    print("\nSaved Users:")
    with open("users.txt", "r") as file:
        print(file.read())

except ValueError:
    print("Error: Age must be a number!")
except FileNotFoundError:
    print("Error: File not found!")
finally:
    print("System complete.")
