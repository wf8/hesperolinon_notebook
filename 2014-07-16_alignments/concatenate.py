#! /usr/bin/env python

import os
import sys
from Bio import Entrez
from Bio import SeqIO
from Bio import AlignIO
from Bio.Alphabet import IUPAC, Gapped


def concatenate(alignments, file_name):
    """
    Concatenates alignments and saves a fasta file
    """
    otus = []
    sequences = []
    for alignment in alignments:
        records = SeqIO.parse(alignment, "fasta")
        for record in records:
            # sample record.description:
            # 10-JEPS-98429
            otu = record.description
            if otu not in otus:
                otus.append(otu)
                sequences.append("")

    # now concatenate the sequences
    total_length = 0
    for alignment in alignments:
        records = SeqIO.parse(alignment, "fasta")
        # make sure to only add 1 sequence per gene region for each otu
        already_added = []
        for record in records:
            otu = record.description
            if otu not in already_added:
                sequences[otus.index(otu)] = sequences[otus.index(otu)] + record.seq
                already_added.append(otu)
            loci_length = len(record.seq)
        total_length += loci_length
        # add gaps for any OTU that didn't have a sequence
        for otu in otus:
            if otu not in already_added:
                sequences[otus.index(otu)] = sequences[otus.index(otu)] + make_gaps(loci_length)

    # write to FASTA file
    f = open(file_name, "w")
    for otu in otus:
        # >otu
        # otus[otu]
        f.write("> " + otu + "\n")
        sequence = str(sequences[otus.index(otu)])
        i = 0
        while i < len(sequence):
            f.write(sequence[i:i+80] + "\n")
            i += 80
    f.close()

    # write to nexus file
    alignment = AlignIO.read(open(file_name), "fasta", alphabet=Gapped(IUPAC.ambiguous_dna))
    g = open(file_name + ".nex", "w")
    g.write(alignment.format("nexus"))


def make_gaps(length):
    """
    Inputs an integer.
    Returns a string of '-' of length
    """
    gap = ""
    for i in range(length):
        gap = "-" + gap
    return gap


nuclear = ["aligned/ITS.fas", "aligned/ETS.fas"]
chloroplast = ["aligned/matK.fas", "aligned/rpl16.fas", "aligned/trnLF.fas", "aligned/trnTL.fas"]
combined = nuclear + chloroplast

concatenate(nuclear, "nuclear.fasta")
concatenate(chloroplast, "chloroplast.fasta")
concatenate(combined, "combined.fasta")

