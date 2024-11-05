class KmerProcessor:
    def __init__(self, sequences, k):
        self.sequences = sequences
        self.k = k

    def generate_kmers(self):
        kmers = []
        for sequence in self.sequences:
            kmers.extend([sequence[i:i + self.k] for i in range(len(sequence) - self.k + 1)])
        return kmers
