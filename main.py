def count_characters(text_str: str):
    """Takes a string of text from a book converts all characters to 
    lowercase and returns a dict with characters as the key and the 
    number of times that character appeared in the string. 
    (String) ==> {Char:Count}
    """
    char_count = {}

    for ch in text_str:
        ch_lower = ch.lower()
        if ch_lower not in char_count:
            char_count[ch_lower] = 1
        else:
            char_count[ch_lower] += 1

    return char_count

def count_words(text_str: str):
    str_list = text_str.split()
    count = 0

    for word in str_list:
        count += 1
    
    return count



def main():

    path_pref = "/home/zero/workspace/github.com/Stephen-Hrrll/bookbot/books/"
    title = "frankenstein"
    extension = ".txt"

    path_to_file = path_pref + title + extension
    with open(path_to_file) as f:
        file_contents = f.read()

    # print(file_contents)
    # print(count_words(file_contents))
    print(count_characters(file_contents))



if __name__ == "__main__":
    main()