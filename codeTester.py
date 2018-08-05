import subprocess

def test(program, infile, outfile):

    #create command that tests the code
    command = [program, "<", infile]

    output = subprocess.check_output(command, shell=True)
    print(output)

def compile():
    print("e")
