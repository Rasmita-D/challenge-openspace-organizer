def read_names_from_csv(input_filepath):
    """Used to read input from a csv file"""
    f=open(input_filepath,"r")
    names=f.read().split('\n')
    return names

def write_names_to_file(names,output_path):
    """Used to write output to a file"""
    f = open(output_path, "w")
    f.write(names)
    f.close
 

