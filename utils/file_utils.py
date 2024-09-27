def read_names_from_csv(input_filepath:str)->list:
    """Used to read input from a csv file"""

    #Opening the file and creating a list of names
    f=open(input_filepath,"r")
    names=f.read().split('\n')
    f.close()
    return names

def write_names_to_file(names:str,output_path:str)->None:
    """Used to write output to a file"""

    #Writing names to the output file
    f = open(output_path, "w")
    f.write(names)
    f.close
 

