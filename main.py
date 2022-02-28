from theatre import theatre
import sys
import os


# return list of reservation requests
def readFile(filename: str):
    res = []
    with open(filename, 'r') as f_in:
        # read each line of the input file
        for line in f_in:
            # split into a list
            content = line.split()
            # append reservation code and count
            res.append([content[0], content[1]])
    # return list of all reservations
    return res

# write output file
def writeFile(filename: str, contents: list):
    with open(filename, 'w') as f_out:
        for line in contents:
            print(line, file = f_out)


 

def main():
    if len(sys.argv) < 2:
        print('Please enter a file to read')
        return None
    test = theatre()
    print(test)
    file = sys.argv[1]
    res = readFile(file)
    ofile = file[:file.find('.')] + '.out'
    content = []
    for req in res:
        seats = ','.join(test.reserve(int(req[1])))
        if seats:
            content.append(req[0] + ' ' + seats)
        else:
            print(req[0], 'failed')
    writeFile(ofile, content)
    print(test)
    return os.path.abspath(ofile)



main()
