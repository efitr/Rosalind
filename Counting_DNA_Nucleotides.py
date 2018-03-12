
#+++++++++++++++++++++++++++++++++++++++ROSALIND CHALLENGE 1+++++++++++++++++++++++++++++++++++++++++++

'''  
Take a given DNA sequence and find it's nucleotide count
'''
'''
Text:
    "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
'''
def count_DNA_nucleotides():

    #First need to get every element on a list, has an specific element
    nucleotides = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
    

    num_adenine = 0
    num_guanine = 0
    num_cytocine = 0
    num_thymine = 0

    #Second iterate through each element and depending on what I find add +1 to the right element
    for nucleotide in nucleotides:
        if nucleotide == "A":
            num_adenine += 1
        if nucleotide == "G":
            num_guanine += 1
        if nucleotide == "C":
            num_cytocine += 1
        if nucleotide == "T":
            num_thymine += 1 

    return num_adenine, num_cytocine, num_guanine, num_thymine 


# def _main():
#     #t = open("intro_bioinformatics_armory.txt", "r", encoding="utf8")
#     print(count_DNA_nucleotides())
    

if __name__ == "__main__":
    print(count_DNA_nucleotides())
