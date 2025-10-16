if __name__ == "__main__":
    
    text = "abcdef"
    #seznam = ["a","b","c","d","e","f"]

    #text[1]
    
    index = 0
    for znak in text:
        if index % 2 == 0:
            print(znak)
        index +=1

    index = 0
    while index < len(text):
        print(text[index])
        index += 1

