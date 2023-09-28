dna = input("Input DNA : ") 

dna_list = []
# Seperate by letter and uppercase, put in list
for i in dna.upper():
    dna_list.append(i)

def complement(dna):
    complement_list = []

    for i in dna:
        if i == 'T':
            complement_list.append('A')
        elif i == 'A':
            complement_list.append('T')
        elif i == 'G':
            complement_list.append('C')
        elif i == 'C':
            complement_list.append('G')
        else:
            print("You didn't input DNA correctly.")
            break
    return complement_list
complement_list = complement(dna_list)

def mRNA(complement):
    mRNA_list = []

    for i in complement:
        if i == 'T':
            mRNA_list.append('U')
        else:
            mRNA_list.append(i)
    return mRNA_list
mRNA_list = mRNA(complement_list)

def aminoAcid(mRNA):
    codon_list = []
    for i in range(0,len(mRNA), 3):
        codon = mRNA[i] + mRNA[i+1] + mRNA[i+2]
        codon_list.append(codon)
        i += 2
        if i+3 == len(mRNA):
            break

    aminoAcid_list = []
    for i in codon_list:
        if i == "AAA" or i == "AAG":
            aminoAcid_list.append("Lys (K)")
        elif i == "AAC" or i == "AAU":
            aminoAcid_list.append("Asn (U)")
        elif i == "ACA" or i == "ACC" or i == "ACG" or i == "ACU":
            aminoAcid_list.append("Thr (T)")
        elif i == "AGA" or i == "AGG":
            aminoAcid_list.append("Arg (R)")
        elif i == "AGC" or i == "AGU":
            aminoAcid_list.append("Ser (S)")
        elif i == "AUA" or i == "AUC" or i == "AUU":
            aminoAcid_list.append("Ile (I)")
        elif i == "AUG":
            aminoAcid_list.append("Start Met (M)")
        elif i == "CAA" or i == "CAG":
            aminoAcid_list.append("Gln (Q)")
        elif i == "CAC" or i == "CAU":
            aminoAcid_list.append("His (H)")
        elif i == "CCA" or i == "CCC" or i == "CCG" or i == "CCU":
            aminoAcid_list.append("Pro (P)")
        elif i == "CGA" or i == "CGC" or i == "CGG" or i == "CGU":
            aminoAcid_list.append("Arg (R)")
        elif i == "CUA" or i == "CUC" or i == "CUG" or i == "CUU":
            aminoAcid_list.append("Leu (L)")
        elif i == "GAA" or i == "GAG":
            aminoAcid_list.append("Glu (E)")
        elif i == "GAC" or i == "GAU":
            aminoAcid_list.append("Asp (D)")
        elif i == "GCA" or i == "GCC" or i == "GCG" or i == "GCU":
            aminoAcid_list.append("Ala (A)")
        elif i == "GGA" or  i == "GGC" or i == "GGG" or i == "GGU":
            aminoAcid_list.append("Gly (H)")
        elif i == "GUA" or i == "GUC" or i == "GUG" or i == "GUU":
            aminoAcid_list.append("Val (V)")        
        elif i == "UAA" or i == "UAG" or i == "UGA":
            aminoAcid_list.append("Stop")
        elif i == "UAC" or i == "UAU":
            aminoAcid_list.append("Tyr (Y)")
        elif i == "UCA" or i == "UCC" or i == "UCG" or i == "UCU":
            aminoAcid_list.append("Ser (S)")
        elif i == "UGC" or i == "UGU":
            aminoAcid_list.append("Cys (C)")
        elif i == "UGG":
            aminoAcid_list.append("Trp (W)")
        elif i == "UUA" or i == "UUG":
            aminoAcid_list.append("Leu (L)")
        elif i == "UUC" or i == "UUU":
            aminoAcid_list.append("Phe (F)")
    return aminoAcid_list
aminoAcid_list = aminoAcid(mRNA_list)


print("Complement: " + "".join(complement_list))
print("mRNA      : " + "".join(mRNA_list))
print("Amino Acid: " + " - ".join(aminoAcid_list))
