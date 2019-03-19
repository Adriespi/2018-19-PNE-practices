class Seq:
    """A class for representing sequences"""

    def __init__(self, strbases):

        self.strbases = strbases


# length

    def len(self):

        return len(self.strbases)

#  seq complement
    def complement(self):

        seq = self.strbases
        complement_dict = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}

        bases = list(seq)

        bases = [complement_dict[base] for base in bases]

        return ''.join(bases)


# Reverse
    def reverse(self):

        return self.strbases[::-1]


#Number of nucleotid appearances

    def count_bases(self):

        seq = self.strbases
        dict_s = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
        count_a = seq.count('A')
        dict_s['A'] = count_a
        count_t = seq.count('T')
        dict_s['T'] = count_t
        count_c = seq.count('C')
        dict_s['C'] = count_c
        count_g = seq.count('G')
        dict_s['G'] = count_g

        return dict_s

# nucleotid percentage

    def perc(self):

        sequence = self.strbases
        tl = len(sequence)
        list_per = list()
        count_a = sequence.count('A')
        n_a = round(100.0 * count_a / tl, 1)
        list_per.append(n_a)
        count_t = sequence.count('T')
        n_t = round(100.0 * count_t / tl, 1)
        list_per.append(n_t)
        count_c = sequence.count('C')
        n_c = round(100.0 * count_c / tl, 1)
        list_per.append(n_c)
        count_g = sequence.count('G')
        n_g = round(100.0 * count_g / tl, 1)
        list_per.append(n_g)

        return list_per