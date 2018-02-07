# raw_data = open("dataset.txt")


"""
import re

x = "Maz123har"


raw_data = open('data.txt')
sequences = {}
new_key = ""

for line in raw_data:
  current_key= []
  
  if re.findall("^>", line):
    #print ((re.findall(">[a-zA-Z ]*", line)))
    current_key = ((re.findall(">[a-zA-Z ]*", line)))
    #print (current_key[0])
    new_key = current_key[0]
    sequences[new_key] = ""
  else:
   # print (sequences)
    #print (new_key)
    #print (line, "This")
    sequences[new_key] = sequences[new_key]+(line.replace(" ",""))
    
print (sequences)

"""
import re
def data_org(string):
    sequences = {}
    seq_name_string = ""

    string = str(string)
    new_string= string.replace("\r\n","\n")
    new_list = new_string.split("\n")
    #return (sequences.keys())
    #return (new_list)
    total_lines = len(new_list)

    for line in new_list:





        if re.findall("^>", line):
            #return (line)
            seq_name = re.findall("^>.*",line)

            seq_name_string = (seq_name[0]).replace(">","")

            #return (seq_name_string)
            if seq_name_string in sequences.keys():
                return ("Multiple sequences are having same name - change name")
            else:
                sequences[seq_name_string]=""
        elif sequences=={}:
            if re.findall("\S",line):
                return ("function breaks")
            else:
                pass

        else:
            sequences[seq_name_string]=sequences[seq_name_string]+line

    return sequences

def evaluation(data):

    int_seq = data
    #return (int_seq)
    int_keys=int_seq.keys()
    for key in int_keys:
        int_seq[key]=(((int_seq[key]).replace("/n","")).replace(" ","")).upper()
        #return (int_seq[key])
        for nucleotide in int_seq[key]:
            if nucleotide == "G" or nucleotide == "C" or nucleotide == "T" or nucleotide == "A":
                pass
            else:
                return ("bad sequence")

    return (int_seq)


def gc_content(output):

    int_seq_data = output
    gc_cont_percent = {}
    #return (int_seq_data)
    if int_seq_data == {}:
        return ("No sequence(s) added")
    else:


        for key in int_seq_data.keys():


            gc_counter= 0
            total_counter = 0

            seq = (int_seq_data[key])

            for nucleotide in seq:
                if nucleotide == "G" or nucleotide == "C":
                    gc_counter = gc_counter+1
                    total_counter =total_counter+1
                else:
                    total_counter = total_counter+1

            if total_counter == 0:

                return ("EmptySequence_Error")
            else:
                percent_gc_content = (gc_counter/total_counter)*100

                gc_cont_percent[key] ="{0:.2f}".format(percent_gc_content)
    return (gc_cont_percent)




