with open('input.txt', 'r') as my_file:
    print(my_file.read(), '\n')


with open('input1.txt', 'r') as file:
    outfile_name = file.readline()

outfile = open(outfile_name, 'w')
outfile.write('Hello World')
outfile.close()
