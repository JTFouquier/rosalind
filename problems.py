




def dna(file_name):
    """

    :param file_name: file containing one DNA seq
    :return: counts of A, C, G, Ts
    """

    from collections import Counter

    with open(file_name) as fin:
        for dna_seq in fin:
            dna_seq_list = list(dna_seq.strip())
            counter = Counter(dna_seq_list)

            return print(counter['A'], counter['C'], counter['G'], counter['T'])


def rna(file_name):

    import re

    with open(file_name) as fin:
        for dna_seq in fin:

            return print(re.sub("T", "U", dna_seq))


def revc(file_name):

    complement_dict = {"A": "T", "T": "A", "C":"G", "G":"C"}


    with open(file_name) as fin:

        for dna_seq in fin:
            rev_complement = ""
            for i in dna_seq.strip():
                rev_complement += complement_dict[i]

            return print(rev_complement[::-1])



def fib(file_name):





    pass


def gc():
    pass


# dna("rosalind_dna.txt")
# rna("rosalind_rna.txt")
# revc("rosalind_revc.txt")

fib('5 3')