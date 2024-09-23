
#nucleotide class definition
#this is a doubly linked list, each 'nucleotide' has a 'next', 'previous' and 'complement' property
#all initially set to None except for the nitrogenous base value passed at instantiation

class Nucleotide:
    def __init__(self,value, end_direction = None):
        self.value = value
        self.next = None
        self.previous = None
        self.complement = None
        self.end_direction = end_direction
        self.gene_marker = None
        self.promoter_marker = None



    #DNA_Polymerase class definition, no constructor at the moment
#
class DNA_Polymerase:
    def __init__(self):
        pass

    def DNA_Replication(self, strand):

        complement_sequence = strand.generate_complement_sequence()

        new_strand = DNAStrand()


        for i in range(len(complement_sequence)):
            new_nucleotide = complement_sequence[i]
            if new_strand.head == None:
                new_strand.head = new_nucleotide
                new_strand.tail = new_nucleotide



            else:
                new_strand.tail.next = new_nucleotide
                new_nucleotide.previous = new_strand.tail
                new_strand.tail = new_nucleotide
            new_strand.length +=1


        return new_strand


class RNA_Polymerase:
    def __init__(self):
        pass

    def RNA_Transcription(self, strand, gene):
        RNA_dict = {'A': 'U', 'T': 'A', 'G': 'C', 'C': 'G'}

        # Find the start of the gene
        temp = strand.head
        while temp:
            if temp.gene_marker == f"{gene} start":
                break
            temp = temp.next

        # Check if the gene start was found
        if not temp or temp.gene_marker != f"{gene} start":
            print("Gene could not be found in this strand")
            return None

        # Start transcription from the gene start
        gene_transcriber = temp
        mRNA_transcript = RNAStrand()

        # Transcribe until the gene end is found
        while gene_transcriber and gene_transcriber.previous.gene_marker != f"{gene} end":
            if gene_transcriber.value in RNA_dict:
                new_nucleotide = Nucleotide(RNA_dict[gene_transcriber.value])

                # Append the new nucleotide to the mRNA strand
                if mRNA_transcript.head is None:
                    mRNA_transcript.head = new_nucleotide
                    mRNA_transcript.tail = new_nucleotide
                else:
                    mRNA_transcript.tail.next = new_nucleotide
                    new_nucleotide.previous = mRNA_transcript.tail
                    mRNA_transcript.tail = new_nucleotide

                # Increment the length of the mRNA strand
                mRNA_transcript.length += 1

            # Move to the next nucleotide in the gene
            gene_transcriber = gene_transcriber.next

        return mRNA_transcript

class RNAStrand:
    def __init__(self, value=None):

        if value:
            new_nucleotide = Nucleotide(value)
            self.head = new_nucleotide
            self.tail = new_nucleotide
            self.length = 1
        else:
            self.head = None
            self.tail = None
            self.length = 0

    def print_sequence(self):
        if self.head == None:
            print("This strand contains no nucleotides")
            return False
        else:
            if self.head.end_direction == "5'":
                print("5'", end = ' ')
            if self.head.end_direction == "3'":
                print("3'", end=' ')
            temp = self.head
            while temp is not None:

                if temp.next is not None:
                    print(temp.value, end = "--")
                else:
                    print(temp.value, end = ' ')

                temp = temp.next
            if self.tail.end_direction == "3'":
                print("3'")
            if self.tail.end_direction == "5'":
                print("5'")



            return True

    def append(self,value):
        new_nucleotide = Nucleotide(value)
        if self.head == None:
            self.head,self.tail = new_nucleotide, new_nucleotide
            new_nucleotide.end_direction = "5'"
        else:
            self.tail.next = new_nucleotide
            new_nucleotide.previous = self.tail
            self.tail = new_nucleotide
            if new_nucleotide.next is None:
                new_nucleotide.end_direction = "3'"

        self.length +=1

    def get_nucleotide_byIndex(self,index):
        if self.head is None:
            print("This strand contains no nucleotides")
            return None

        elif index < 0 or index >= self.length:
                print("index out of range")
                return None
        else:
            if index < self.length/2:
                temp = self.head
                for _ in range(index):
                    temp = temp.next
                #print(f"The nucleotide at index {index} is {temp.value}.")
                return temp
            else:
                temp = self.tail
                for _ in range(self.length -1, index, -1):
                    temp = temp.previous
                #print(f"The nucleotide at index {index} is {temp.value}.")
                return temp









class DNAStrand:
    def __init__(self, value = None):



        if value:
            new_nucleotide = Nucleotide(value)
            self.head = new_nucleotide
            self.tail = new_nucleotide
            self.length = 1
        else:
            self.head = None
            self.tail = None
            self.length = 0
        #self.gene_promoter_indices = {}
        self.wildtype_gene_indices = {}


    def generate_complement_sequence(self):
        DNA_dict = {'A':'T',
                    'T':'A',
                    'G':'C',
                    'C':'G'}

        compliment_sequence = []


        if self.head == None:
            print("this strand contains no nucleotides")
            return False

        else:
            temp = self.head
            while temp is not None:
                if temp.value in DNA_dict:
                    new_nucleotide = Nucleotide(DNA_dict[temp.value])
                    temp.complement = new_nucleotide
                    compliment_sequence.append(new_nucleotide)

                temp = temp.next
            compliment_sequence[0].end_direction = "3'"
            compliment_sequence[-1].end_direction = "5'"

        return compliment_sequence





    def print_sequence(self):
        if self.head == None:
            print("This strand contains no nucleotides")
            return False
        else:
            if self.head.end_direction == "5'":
                print("5'", end = ' ')
            if self.head.end_direction == "3'":
                print("3'", end=' ')
            temp = self.head
            while temp is not None:

                if temp.next is not None:
                    print(temp.value, end = "--")
                else:
                    print(temp.value, end = ' ')

                temp = temp.next
            if self.tail.end_direction == "3'":
                print("3'")
            if self.tail.end_direction == "5'":
                print("5'")



            return True

    def append(self,value):
        new_nucleotide = Nucleotide(value)
        if self.head == None:
            self.head,self.tail = new_nucleotide, new_nucleotide
            new_nucleotide.end_direction = "5'"
        else:
            self.tail.next = new_nucleotide
            new_nucleotide.previous = self.tail
            self.tail = new_nucleotide
            if new_nucleotide.next is None:
                new_nucleotide.end_direction = "3'"

        self.length +=1

    def get_nucleotide_byIndex(self,index):
        if self.head is None:
            print("This strand contains no nucleotides")
            return None

        elif index < 0 or index >= self.length:
                print("index out of range")
                return None
        else:
            if index < self.length/2:
                temp = self.head
                for _ in range(index):
                    temp = temp.next
                #print(f"The nucleotide at index {index} is {temp.value}.")
                return temp
            else:
                temp = self.tail
                for _ in range(self.length -1, index, -1):
                    temp = temp.previous
                #print(f"The nucleotide at index {index} is {temp.value}.")
                return temp

    def point_mutation(self,index,value):
        temp = self.get_nucleotide_byIndex(index)
        if temp:
            temp.value = value
            return True
        return False

    def find_sequence(self, sequence):
        index = 0
        length = len(sequence)

        if length == 0:  # Handle empty sequence
            return -1, -1  # Return invalid indices

        pointer_1 = self.head
        start_index = -1  # To store where the sequence starts
        current_index = 0  # Tracks the index of pointer_1 in the linked list

        while pointer_1:  # Loop until the end of the linked list
            if pointer_1.value == sequence[index]:
                if index == 0:
                    start_index = current_index  # Record the starting index when match begins
                index += 1
            else:
                if index > 0:  # Reset if there's a mismatch after a partial match
                    index = 0
                    start_index = -1  # Reset start index

            # Check if the sequence is fully matched
            if index == length:
                end_index = current_index  # End index is the current position in the list
                return start_index, end_index

            # Move to the next node in the list
            pointer_1 = pointer_1.next
            current_index += 1

        # If we exit the loop, it means the sequence wasn't found
        return False  # Sequence not found

    def assign_gene(self, sequence, gene_name):
        if self.find_sequence(sequence):
            gene_start_index, gene_end_index = self.find_sequence(sequence)
            self.wildtype_gene_indices[gene_name] = [gene_start_index,gene_end_index]

            start_node = self.get_nucleotide_byIndex(gene_start_index)
            end_node = self.get_nucleotide_byIndex(gene_end_index)

            start_node.gene_marker = f"{gene_name} start"
            end_node.gene_marker = f"{gene_name} end"






dna_strand = DNAStrand()

dna_polymerase = DNA_Polymerase()

rna_polymerase = RNA_Polymerase()



sq = ['A','G','G','T','A','A','T','C','G','C']
sequence = "AGGCCGGTTAATGCGTATGCGTATGACTA"
for i in sequence:
    dna_strand.append(i)

complement_strand = dna_polymerase.DNA_Replication(dna_strand)

dna_strand.print_sequence()
complement_strand.print_sequence()

dna_strand.assign_gene("CCGGTTAAT", "bronson-149")
dna_strand.assign_gene("CGT", "alf-123")

#print(dna_strand.wildtype_gene_indices)

mRNA = rna_polymerase.RNA_Transcription(dna_strand,"bronson-149")
mRNA_alf = rna_polymerase.RNA_Transcription(dna_strand, "alf-123")

mRNA.print_sequence()
mRNA_alf.print_sequence()










#dna_strand.assign_gene("TTAATGCGTATG","gene1","CCG")


def main():
    input_sequence = input("enter a DNA Sequence: ").strip().upper()


    dna_strand = DNAStrand()
    dna_polymerase = DNA_Polymerase()

    for i in input_sequence:
        dna_strand.append(i)
    #dna_strand.print_sequence()
    complement_generation = input("\nWould you like to see this sequence bonded to its complement strand? ").strip()
    complement_generation.lower()
    if complement_generation == 'yes' or complement_generation =='y':
        complement_strand = dna_polymerase.DNA_Replication(dna_strand.generate_complement_sequence())

        dna_strand.print_sequence()
        complement_strand.print_sequence()
    elif complement_generation == 'no' or complement_generation =='n':
        see_single = input("\nWould you like to see this strand as a single strand of DNA? ")
        if see_single == 'yes' or see_single == 'y':
            dna_strand.print_sequence()


def primary():
    program = True
    main_menu = True
    chromosome_view_menu = False
    chromosome_edit_menu = False
    chromosome_create_menu = False

    dna_polymerase = DNA_Polymerase()
    rna_polymerase = RNA_Polymerase()


    genome = {}

    print("Choose one of the following options\n")
    while program:
        while main_menu:

            print("1. Create a new chromosome")
            print("2. Delete a chromosome")
            print("3. View an existing chromosome")
            print("4. Edit an existing chromosome")
            print("5. View existing genome")
            main_menu_option = input("\nWhat would you like to do? ").strip()

            if main_menu_option == "1":
                main_menu = False
                chromosome_create_menu = True
        while chromosome_create_menu:
            chromosome_name = input("Enter a name for this chromosome: ").strip()
            chromosome_name = chromosome_name.lower()

            chromosome_sequence = input("\nEnter a sequence for this chromosome's template strand: ").strip()
            chromosome_sequence = chromosome_sequence.upper()

            single_or_double = input("\nWould you like this DNA to be single or double stranded? ").strip()
            single_or_double.lower()

            if single_or_double == 'single':
                genome[chromosome_name] = DNAStrand()

                for i in range(len(chromosome_sequence)):
                    genome[chromosome_name].append(chromosome_sequence[i])
                genome[chromosome_name].print_sequence()

            elif single_or_double == 'double':
                genome[chromosome_name] = DNAStrand()

                for i in range(len(chromosome_sequence)):
                    genome[chromosome_name].append(chromosome_sequence[i])

                genome[f"{chromosome_name}_complement"] = dna_polymerase.DNA_Replication(genome[chromosome_name].generate_complement_sequence())
                genome[chromosome_name].print_sequence()
                genome[f"{chromosome_name}_complement"].print_sequence()
                print(genome)
















