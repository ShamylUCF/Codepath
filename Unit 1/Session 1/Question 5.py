def concatenate(words):
    resultString = ""

    # for x in words:
    #     resultString += x

    for i in range(0,len(words)):
        resultString += words[i]

    print(resultString)

words = ["vengeance", "darkness", "batman"]
concatenate(words)