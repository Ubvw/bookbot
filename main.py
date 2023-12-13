with open("books/frankenstein.txt", "r") as file:
    content = file.read()
    words = content.split()
    length = len(words)
    #get the number of words
    print("---  BEGIN REPORT OF BOOKS  ---")
    print(f"{length} words found in the document\n")

    #dictionary
    chars = {}
    for word in content:
        lowered = word.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    
    #sorting
    sorted_dict = {k: v for k, v in sorted(chars.items())}
    for key, value in sorted_dict.items():
        if key.isalpha():
            print(f"The '{key}' character was found {value} times.")
    print("---  END REPORT  ---")

