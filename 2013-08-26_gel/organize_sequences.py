#! /usr/bin/env python
import os
import sys
import time
from threading import Thread
from threading import Event
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Alphabet import IUPAC
from Bio.Align.Applications import ClustalwCommandline
from Bio import SeqIO
from Bio import AlignIO
from Bio.Align import AlignInfo

"""
organize_sequences.py

Filters out bad reads, then makes consensus sequences out of the good forward 
and reverse sequences, finally outputing an alignment for all the sequences. 
Uses ClustalW for alignments.

To use:
python organize_sequences.py path cutoff
where path is the folder containing the sequences
and cutoff is the percent (0-100) of ambiguous characters allowed

"""

def make_consensus( rev_string, for_string, seqfile):
    "function that accepts 2 sequence and returns the consensus sequence"
    # make fasta file for each paired sequence
    rev_sequence = Seq(rev_string.replace("\n", "").replace('\r', '').replace(' ', ''), IUPAC.ambiguous_dna)
    rev_sequence= rev_sequence.reverse_complement()
    for_sequence = Seq(for_string.replace("\n", "").replace('\r', '').replace(' ', ''), IUPAC.ambiguous_dna)
    paired_sequences = [SeqRecord(rev_sequence, id="rev"), SeqRecord(for_sequence, id="for")]
    if not os.path.exists("results/"):
        os.makedirs("results/")
    fasta_file = "results/" + seqfile + ".fasta"
    SeqIO.write(paired_sequences, fasta_file, "fasta")
    # align the paired sequences
    aln_file = "results/" + seqfile + ".aln"
    # clustalw_cline = ClustalwCommandline("clustalw", infile=fasta_file, outfile=aln_file, pwgapopen="100", gapopen="100")
    clustalw_cline = ClustalwCommandline("clustalw", infile=fasta_file, outfile=aln_file, pwgapopen=100, gapopen=100)
    clustalw_cline()
    # hack so that dumb_consensus will accept 1 base call against N
    f = open(aln_file, 'r+')
    contents = f.read()
    f.close()
    f = open(aln_file, 'w')
    f.write( contents.replace('N','.') )
    f.close()
    # read in alignment file and generate consensus
    alignment = AlignIO.read(aln_file, "clustal")
    summary_align = AlignInfo.SummaryInfo(alignment)
    return summary_align.dumb_consensus(ambiguous = "N", threshold=0.0, require_multiple=0)

def percent_ambiguous( string ):
    "function that return the percent of ambiguous N characters in the string"
    n = 0
    i = 0
    for letter in string:
        # skip the first and last 40 positions
	if ((letter == 'N') and (i > 40) and (i < (len(string) - 40))):
	    n += 1
	i += 1
    return 100 * n / len(string)

class SimpleTimer(Thread):
    
    def __init__(self, event):
        Thread.__init__(self)
	self.stopped = event

    def run(self):
        while not self.stopped.wait(1):
	    print ".",
            sys.stdout.flush()


path = sys.argv[1]
cutoff = int(sys.argv[2])

# alphabetize the list of filenames
filelist = os.listdir(path)
filelist.sort()

ITS_records = []
i = 0

for seqfile in filelist:

    # find forward sequences
    if (seqfile.find(".F_") != -1):
        print "current forward seq file: " + seqfile

	# get sample_id
	sample_id = seqfile[7:seqfile.find(".F_")]

	handle = open(path + seqfile, "rb")
	for record in SeqIO.parse(handle, "abi"):
	    forward_seq = record.seq
	    reverse_found = False
	    # get reverse sequence
	    for seqfile2 in filelist:
	        if (seqfile2.find(sample_id + ".R_") != -1):
		    print "found reverse seq file: " + seqfile2
		    reverse_found = True
		    handle2 = open(path + seqfile2, "rb")
		    for record2 in SeqIO.parse(handle2, "abi"):
		        reverse_seq = record2.seq
		
	    if (reverse_found == False):
	        print "reverse seq file not found"
		reverse_seq = Seq("A", IUPAC.ambiguous_dna)
		
	    print "checking percent ambiguous"
	    for_str = str(forward_seq)
	    rev_str = str(reverse_seq)
	    if (percent_ambiguous(for_str) > cutoff):
	        for_str = "A"
		print "forward sequence is no good"
	    if (percent_ambiguous(rev_str) > cutoff):
		rev_str = "A"
		print "reverse sequence is no good"
		
	    print "making consensus"
	    # send the for and rev strings to function that return seq object of consensus sequence
	    consensusseq = make_consensus(for_str, rev_str, sample_id)
	    print "consensus sequence: " + consensusseq
	    # make fasta file containing all the consensus sequences
	    ITS_records.append( SeqRecord(consensusseq, id=sample_id, description='') )

print "writing ITS.fasta"
SeqIO.write(ITS_records, "ITS.fasta", "fasta")
print "aligning ITS.fasta with clustalw"

stop_timer = Event()
timer = SimpleTimer(stop_timer)
timer.start()

clustalw_cline = ClustalwCommandline("clustalw", infile="ITS.fasta")
clustalw_cline()

stop_timer.set()
