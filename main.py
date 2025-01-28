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

def sort_on(dict):
    return dict["count"]

def dict_to_list(char_count:dict):
    """converts a dictionary of character counts to a list of dictionaries
    in the form:
    char_count_list = [
    {"char": "a", "count": 7},
    {"char": "b", "count": 10},
    {"char": "c", "count": 2}
]
    """

    char_count_list = []
    for key in char_count:
        if key.isalpha():
            char_count_list.append({"char": key, "count": char_count[key]})
    
    return char_count_list


def print_report(word_count: int, char_count: dict, title:str):
    char_count_list = dict_to_list(char_count)
    

    char_count_list.sort(reverse=True, key=sort_on)

    print(f"--- Begin report of books/{title} ---")
    print(f"{word_count} words found in the document \n")


    for dict in char_count_list:
        print(f"The '{dict['char']}' character was found {dict['count']} times")
    
    print("--- End report ---")


def main():

    path_pref = "/home/zero/workspace/github.com/Stephen-Hrrll/bookbot/books/"
    title = "frankenstein"
    extension = ".txt"

    path_to_file = path_pref + title + extension
    with open(path_to_file) as f:
        file_contents = f.read()

    word_count = count_words(file_contents)
    char_count = count_characters(file_contents)
    # print(file_contents)
    # print(count_words(file_contents))
    # print(count_characters(file_contents))
    print_report(word_count, char_count, title+extension)



if __name__ == "__main__":
    main()