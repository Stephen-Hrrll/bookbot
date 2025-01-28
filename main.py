def main():

    path_pref = "/home/zero/workspace/github.com/Stephen-Hrrll/bookbot/books/"
    title = "frankenstein"
    extension = ".txt"

    path_to_file = path_pref + title + extension
    with open(path_to_file) as f:
        file_contents = f.read()

    print(file_contents)



if __name__ == "__main__":
    main()