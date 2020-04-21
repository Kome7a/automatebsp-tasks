def concat_str(str1, str2):
    try:
        return str1 + str2
    except TypeError as error:
        print("Please insert a string.")
        print(f"Error: {error}")
        exit(1)
    finally:
        print("Thank you.")

print(concat_str("d", 2))
