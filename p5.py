def writea(words):
    with open("quotes.txt", "w") as file:
        file.write(words)
def writeb(words):
    with open("quotes.txt", "a") as file:
        file.write(words)
def read():
    with open("quotes.txt", "r") as file:
        print(file)
