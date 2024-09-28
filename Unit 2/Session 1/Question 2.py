def can_trust_message(message):
    alphabet = set()
    remove_whitespace = message.replace(" ", "")
    string = list(remove_whitespace)
    
    print(string)

    for i in range(len(string)):
        alphabet.add(string[i])
    
    if len(alphabet) == 26:
        return True
    return False

message1 = "sphinx of black quartz judge my vow"
message2 = "trust me"

print(can_trust_message(message1))
print(can_trust_message(message2))