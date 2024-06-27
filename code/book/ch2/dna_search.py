import time
from enum import IntEnum

Nucleotides = IntEnum("Nucleotides", ("A", "C", "G", "T"))

gene_str = "ACGTGGCTCTCTAACGTACGTACGTACGGGGTTTATATATACCCTAGGACTCCCTTT"


def string_to_gene(s: str):
    gene = []
    for i in range(0, len(s), 3):
        if (i + 2) >= len(s):
            break
        codon = [Nucleotides[s[i]], Nucleotides[s[i + 1]], Nucleotides[s[i + 2]]]
        gene.append(codon)
    return gene


def _print_time(function):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = function(*args, **kwargs)
        end = time.time()
        print(f"{function.__name__} took {end - start} seconds")
        return result

    return wrapper


my_gene = string_to_gene(gene_str)


def linear_contains(gene, key_codon) -> bool:
    for codon in gene:
        if codon == key_codon:
            return True
    return False


codon1 = [Nucleotides.A, Nucleotides.C, Nucleotides.T]
codon2 = [Nucleotides.A, Nucleotides.C, Nucleotides.A]
codon3 = [Nucleotides.C, Nucleotides.G, Nucleotides.T]


test = [1, 3, 2, 5, 2, 4]


@_print_time
def reorder(gene):
    for i in range(len(gene)):
        for j in range(i + 1, len(gene)):
            if gene[i] > gene[j]:
                gene[i], gene[j] = gene[j], gene[i]
    return gene


@_print_time
def selectsort(gene):
    for i in range(len(gene) - 1):
        min_index = i
        for j in range(i + 1, len(gene)):
            if gene[j] < gene[min_index]:
                min_index = j
        gene[i], gene[min_index] = gene[min_index], gene[i]
    return gene


# re = reorder(test)
# re1 = selectsort(re)
# print(f"re: {re}, re1: {re1}")


def quicksort(gene):
    if len(gene) < 2:
        return gene
    else:
        pivot = gene[0]
        less = [i for i in gene[1:] if i <= pivot]
        greater = [i for i in gene[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)


@_print_time
def shellsort(gene):
    gap = len(gene) // 2
    while gap > 0:
        for i in range(gap, len(gene)):
            temp = gene[i]
            j = i
            while j >= gap and gene[j - gap] > temp:
                gene[j] = gene[j - gap]
                j -= gap
            gene[j] = temp
        gap //= 2
    return gene


@_print_time
def bubblesort(gene):
    for i in range(len(gene) - 1):
        for j in range(len(gene) - 1 - i):
            if gene[j] > gene[j + 1]:
                gene[j], gene[j + 1] = gene[j + 1], gene[j]
    return gene


def bisearch(gene, key_codon):
    low = 0
    high = len(gene) - 1
    while low < high:
        mid = (low + high) // 2
        if key_codon == gene[mid]:
            return True
        elif key_codon > gene[mid]:
            low = mid + 1
        else:
            high = mid
    return False


@_print_time
def do(func, gene):
    for i in [codon1, codon2, codon3]:
        print(func(gene, i))


class CompressedGen:
    def __init__(self, gene: str):
        self._comporess(gene)

    def _comporess(self, gene: str):
        self.bit_start = 1
        for i in gene.upper():
            self.bit_start <<= 2
            if i == "A":
                self.bit_start |= 0b00
            elif i == "C":
                self.bit_start |= 0b01
            elif i == "G":
                self.bit_start |= 0b10
            elif i == "T":
                self.bit_start |= 0b11
            else:
                raise ValueError(f"Invalid Nucleotides:{i}")

    def _decompress(self):
        self.str_gene = ""
        while self.bit_start > 1:
            bit: int = self.bit_start & 0b11
            if bit == 0b00:
                self.str_gene += "A"
            elif bit == 0b01:
                self.str_gene += "C"
            elif bit == 0b10:
                self.str_gene += "G"
            elif bit == 0b11:
                self.str_gene += "T"
            self.bit_start >>= 2

    def get_gene_bit(self):
        return self.bit_start

    def __str__(self):
        return self.str_gene[::-1]


if __name__ == "__main__":
    # do(bisearch, order_gene)
    # do(linear_contains, my_gene)
    com = CompressedGen(gene_str)
    com._decompress()
    print(com)
