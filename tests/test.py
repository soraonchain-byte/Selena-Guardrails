from src.guardrails import guardrails_check

if __name__ == "__main__":
    text = input("Enter prompt: ")
    safe, message = guardrails_check(text)

    print(message)