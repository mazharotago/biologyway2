#string = "atgctaccatcattagctaccata"


# validation

def validate_nucleotide(string_new, state):
    for nucleotide in string_new:
        if nucleotide == "G" or nucleotide == "C" or nucleotide == "T" or nucleotide == "A":
            pass
        else:
            return ("bad")





# nucleotidecounter
def nucleotide_counter(string):
    dictionary = {"G": 0, "C": 0, "T": 0, "A": 0}
    state = "good"


    string_novel = (string.replace(" ", "")).upper()
    string_new = (((string_novel.replace("\n\r","")).replace("\r\n","")).replace("\r","")).replace("\n","")

    state = validate_nucleotide(string_new, state)
    if state == "good" or state == None:
        for nucleotide in string_new:
            if nucleotide == "G" or nucleotide == "C" or nucleotide == "A" or nucleotide == "T":
                dictionary[nucleotide] = dictionary[nucleotide] + 1
        return(dictionary, string_new)
    else:
        return("Sorry Bad Sequence", string_new)

# Test


# nucleotide_counter(string)
