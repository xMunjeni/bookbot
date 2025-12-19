def number_of_words(text):
    words = text.split()
    return len(words)

def list_characters(input):
    processed_input = input.lower()
    character_count = {}
    for character in processed_input:
        if character in character_count:
            character_count[character] += 1
        else:
            character_count[character] = 1
    return (character_count)

def sorted_dict(input):
    summed_list= []
    x = input.items()
    for char in x:
        temp_dict = {
            "char" : char[0],
            "num" : char[1]
        }
        summed_list.append(temp_dict)
    sorted_list = sorted(summed_list, key=lambda x: x["num"], reverse=True)
    return(sorted_list)
