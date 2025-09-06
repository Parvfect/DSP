
from ont_fast5_api.fast5_interface import get_fast5_file
import pod5 as p5
from Bio import SeqIO


def parse_biopython(input_fastq):
    for record in SeqIO.parse(input_fastq, 'fastq'):
        yield record

def get_fastq_records(fastq_filepath):
    records = []
    for i, record in enumerate(parse_biopython(fastq_filepath)):
        records.append(record)
    return records

def read_pod5_file(filepath):
    read_ids = []
    squiggles = []
    with p5.Reader(filepath) as reader:
        for read_record in reader.reads():
            read_ids.append(read_record.read_id)
            squiggles.append(read_record.signal)
            

    return squiggles, read_ids

def get_data_from_fast5(fast5_filepath):
    """Returns read_ids, data"""
    data_arr = []
    read_ids = []
    with get_fast5_file(fast5_filepath, mode="r") as f5:
        for read in f5.get_reads():
            raw_data = read.get_raw_data()
            read_ids.append(read.read_id)
            data_arr.append(raw_data)
    return read_ids, data_arr

def reverse_complement(dna):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(complement[base] for base in reversed(dna))

def write_fasta_for_squigulator(strands, filepath=r"C:\Users\Parv\Doc\HelixWorks\Basecalling\squigulator\sample.fa.txt"):
    counter = 3793
    with open(filepath, 'w') as f:
        for strand in strands:
            f.write(f'>>seq_{counter} {len(strand)}bp\n')
            f.write(strand)
            f.write('\n\n')
            counter += 1