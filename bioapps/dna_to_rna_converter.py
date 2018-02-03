#string

def seq_evaluation(string):
    eval_state = "good"
    for nucleotide in string:
        if nucleotide=="G" or nucleotide=="C" or nucleotide=="A" or nucleotide=="T":
            if eval_state == "bad":
                return("bad")
            else:
                eval_state="good"
        else:
            return ("bad")
    return eval_state



def dna_to_rna_convert(string):
    dna_seq = string
    rna_seq = []
    transcription_temp = {'G': 'G', 'A': 'A', 'C': 'C', 'T': "U"}
    string_new = (((((dna_seq.replace("\n\r", "")).replace("\r\n", "")).replace("\r", "")).replace("\n", "")).upper()).replace(" ","")
    state = seq_evaluation(string_new)
    if state=="good":
        for i in string_new:
            rna_seq.append(transcription_temp[i])
        return(("".join(rna_seq)),state)
    else:
        return([string_new,state])


#string = 'GCTATTACTACCATACCTATATA'
#dna_to_rna_convert(string)