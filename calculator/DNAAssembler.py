class DNAAssembler:
    def __init__(self, path):
        self.path = path

    def assemble_sequence(self):
        sequence = self.path[0]
        for node in self.path[1:]:
            sequence += node[-1]
        return sequence
