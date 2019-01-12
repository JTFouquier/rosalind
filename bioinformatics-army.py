

from collections import Counter

### Python review using Rosalind.info

# with open, closes the file

"""
1
"""
def count_ACGTs_from_file(file_name):

    with open(file_name) as fin:
        for dna_seq in fin:
            dna_seq_list = list(dna_seq.strip())
            print(dna_seq_list)
            counter = Counter(dna_seq_list)

            print(counter['A'], counter['C'], counter['G'], counter['T'])



def biological_processes_from_protein(protein_ID):
    from Bio import ExPASy
    from Bio import SwissProt

    handle = ExPASy.get_sprot_raw(protein_ID)
    record = SwissProt.read(handle)

    print(dir(record))

    dir_list = list(dir(record))
    for i in dir_list:
        print(i)
        try:
            print(record[i[0]])
        except:
            pass



biological_processes_from_protein('Q5SLP9')



# count_ACGTs_from_file("rosalind_ini.txt")






