# Importing required packages and methods

import xml.etree.ElementTree as ET
from datetime import date,timedelta

'''
Travel generator Function which takes 2 inputs
x = Numbers of days to depart from current date
y = Numbers of days to retrun from current date
output_file is optional argument to write xml data, set  default to test_payload1.xml' as suggested
'''


def travel_generator(x,y,output_file='test_payload1.xml'):

 #Enforcing int types only   
    try:
        int(x) and int(y):

#Enforcing future date of travel as any negative int would male date of travel in past
        if x and y >= 0:
#Capturing current date            
            current_date = date.today()
#Generating departure_date and return_date based on current date and  input provided days
            departure_date = current_date + timedelta(x)
            return_date = current_date + timedelta(y)

#Generatng root xml 
            root_element = ET.Element("Data")

            travel_date = ET.Element("Travelling Dates")

            root_element.append(travel_date)
#Appending travel dates
            update_depart_date = ET.SubElement(travel_date, "DEPART")
            update_depart_date.text = departure_date

            update_return_date = ET.SubElement(travel_date, "RETURN")
            update_return_date.text = return_date

            tree = ET.ElementTree(root_element)
#Writinng xml data to file
            with open(output_file, mode='w') as xml_output:
                tree.write(xml_output)
        else:
            print("Travel dates hould be future, please input values greter than or equal to 0")
    except ValueError:
        print("Method only takes integers as input")