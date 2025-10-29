import logging #First time using it, usage may be incorrect
import sys
logging.basicConfig(level=logging.WARNING)

filename = "BinaryNumbers.txt"
def calculations(denary_values):
    maximum = (-1,-1)
    minimum = (-1,257)
    for value in enumerate(denary_values):
        if value[1] == maximum or value[1] == minimum:
            logging.warning("The minimum or Maximum value has been repeated the latest row number will be disgarded")
        if value[1] > maximum[1]:
            logging.info(f"New Highest value is {value[1]}")
            maximum = value
        if value[1] < minimum[1]:
            logging.info(f"New Lowest value is {value[1]}")
            minimum = value
    
    #Outputing Information
    print(f"Minimum value: {minimum[1]} Row: {minimum[0]}")
    print(f"Maximum value: {maximum[1]} Row: {maximum[0]}")

def convert_data(binary):
    denary_values = []
    for value in binary:
        valid = True
        if len(value) != 8:
            logging.error(f"Unable to process any non Byte sized data like ({value}), program will continue.")
            valid = False
        character_counter = 7
        denary_value = 0

        if valid == True:
            for character in value :
                if character == "1":
                    denary_value+= 2**character_counter
                character_counter-=1
            denary_values.append(denary_value)
            logging.debug(f"Line {value} was succesfuly converted to {denary_value}")
    logging.info("Values have been converted to denary")
    calculations(denary_values)
        


def get_data():
    try:
        with open(filename) as file: #Opens file only while in use, auto closes it
            binary = []
            for line in file: #Reads each line not using tons of memory in large datasets
                filtered_line = line.rstrip("\n") #Remove  Newline character
                binary.append(filtered_line)
                logging.debug(f"Line: {filtered_line} appeneded to array")
            logging.info("All values extracted from text file")
        convert_data(binary)
    except FileNotFoundError:
        logging.critical("File name incorrect or file nto open in working directory, exiting")
        sys.exit()



            
get_data()