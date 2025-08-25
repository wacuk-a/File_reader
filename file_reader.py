def read_file(name):
    try:
        f = open(name, "r")
        text = f.read()
        f.close()
        return text
    except:
        print("Could not open file!")
        return None

def change_text(t):
    return t.upper()

def write_file(name, stuff):
    f = open(name, "w")
    f.write(stuff)
    f.close()
    print("Saved to", name)

# main program
fname = input("File to read: ")
content = read_file(fname)

if content:
    new_content = change_text(content)
    newname = input("File to save new text: ")
    write_file(newname, new_content)
