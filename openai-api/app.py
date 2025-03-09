from persona import Persona

def main() -> None:
    user1 = Persona("Alice", "あなたは関東出身の日本人男性です。")
    user2 = Persona("Bob", "あなたは関西弁の日本人男性です。")

    # Testing on console
    user_input = input("あなた: ")
    response = user1.chat(user_input)
    print(user1.name, ":\n", response)
    print("\n")

    user_input = input("あなた: ")
    response = user2.chat(user_input)
    print(user2.name, ":\n", response)
    print("\n")

if __name__ == "__main__":
    main()
