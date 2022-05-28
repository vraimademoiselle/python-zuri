filename = "story.txt"
def read_file_content(filename):
    # [assignment] Add your code here 
    # Open the file as f.
    # The function readlines() reads the file.
    with open(filename) as f:
        content = f.readlines()

    # Show the file contents line by line.
    # We added the comma to print single newlines and not double newlines.
    # This is because the lines contain the newline character '\n'.
    for line in content:
        print(line)
    return "Hello World"

# read_file_content(filename)

def word_count():
    text = read_file_content("./story.txt")
    # text = read_file_content()

    #cleaning
    counts = dict()
    words = text.split()
    # words = [word.strip('.,!;()[]') for word in words]
    # words = [word.replace("'s", '') for word in words]

    #finding unique
    unique = []
    for word in words:
        if word not in unique:
            unique.append(word)

    #sort
    unique.sort()

    #print
    print(unique)
    return counts
word_count()