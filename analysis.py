def check():
    with open("decrypted_text.txt") as decrypted_text:
        decrypted_text = decrypted_text.read()
    with open("input_text") as input_text:
        input_text = input_text.read()
    with open("hack_text.txt") as hack_text:
        hack_text = hack_text.read()
    if decrypted_text == input_text and hack_text == input_text:
        print("Тексты совпадают")
    else:
        print("Тексты НЕ совпадают")

check()