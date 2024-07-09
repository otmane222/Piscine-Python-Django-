from path import Path
 
def starto():
    try:
        Path.makedirs("dirct")
    except FileError as e:
        print(e)
    Path.touch('dirct/file')
    f = Path('dirct/file')
    f.write_lines(["lino", "lines"])
    print(f.read_text())

if __name__ == "__main__":
    starto()