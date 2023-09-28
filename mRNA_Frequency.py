aminoAcid = input("Input Aminoacid : ") 

aminoAcid_list = []
# Seperate by letter and uppercase, put in list
for i in aminoAcid.upper():
    aminoAcid_list.append(i)

def mRNA(aminoacid):
    mRNA_list = []

    for i in aminoacid:
        if i == 'F':
            mRNA_list.append("UUU")
        elif i == 'L':
            mRNA_list.append("UUA")
        elif i == 'S':
            mRNA_list.append("UCU")
        elif i == 'Y':
            mRNA_list.append("UAU")
        elif i == 'C':
            mRNA_list.append("UGU")
        elif i == 'W':
            mRNA_list.append("UGG")
        elif i == 'P':
            mRNA_list.append("CCU")
        elif i == 'H':
            mRNA_list.append("CAU")
        elif i == 'Q':
            mRNA_list.append("CAA")
        elif i == 'R':
            mRNA_list.append("CGU")
        elif i == 'I':
            mRNA_list.append("AUU")
        elif i == 'M':
            mRNA_list.append("AUG")
        elif i == 'T':
            mRNA_list.append("ACU")
        elif i == 'N':
            mRNA_list.append("AAU")
        elif i == 'K':
            mRNA_list.append("AAA")
        elif i == 'V':
            mRNA_list.append("GUU")
        elif i == 'A':
            mRNA_list.append("GCU")
        elif i == 'D':
            mRNA_list.append("GAU")
        elif i == 'E':
            mRNA_list.append("GAA")
        elif i == 'G':
            mRNA_list.append("GGU")
        else:
            print("You didn't input DNA correctly.")
            break

    return mRNA_list
mRNA_list = mRNA(aminoAcid_list)

def frequency(mRNA):
    freq = {} #dictionary

    for i in mRNA:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    return freq
frequency_dict = frequency(mRNA_list)

print("".join(mRNA_list))
for keys,values in frequency_dict.items():
    print(keys, "=", values)