#! /usr/bin/env python
import os
import sys
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO


ITS = []
ETS = []
LF = []
MAT = []
RPL = []
TL = []

handle = open('chloroplast_ETS_2014-07-08.fasta', 'rb')
for record in SeqIO.parse(handle, "fasta"):
    if (record.id.find('ETS') != -1):
        ETS.append(record)
    if (record.id.find('ITS') != -1):
        ITS.append(record)
    if (record.id.find('trnT-L') != -1):
        TL.append(record)
    if (record.id.find('trnL-F') != -1):
        LF.append(record)
handle.close()

handle = open('chloroplast_2014-07-08.fasta', 'rb')
for record in SeqIO.parse(handle, "fasta"):
    if (record.id.find('trnTL') != -1):
        TL.append(record)
    if (record.id.find('rpl16') != -1):
        RPL.append(record)
handle.close()

handle = open('Hesp_Oro_2014-07-14.fasta', 'rb')
for record in SeqIO.parse(handle, "fasta"):
    if (record.id.find('O_') == -1):
        if (record.id.find('ETS') != -1):
            ETS.append(record)
        if (record.id.find('ITS') != -1):
            ITS.append(record)
        if (record.id.find('trnLF') != -1):
            LF.append(record)
        if (record.id.find('rpl16') != -1):
            RPL.append(record)
handle.close()

handle = open('ETS_2014-04-15.fasta', 'rb')
for record in SeqIO.parse(handle, "fasta"):
    ETS.append(record)
handle.close()

handle = open('ETS_2014-06-30.fasta', 'rb')
for record in SeqIO.parse(handle, "fasta"):
    ETS.append(record)
handle.close()

handle = open('ITS_2013-12-27.nex', 'rb')
for record in SeqIO.parse(handle, "nexus"):
    ITS.append(record)
handle.close()

handle = open('chloroplast_yuri/LF.nex', 'rb')
for record in SeqIO.parse(handle, "nexus"):
    LF.append(record)
handle.close()

handle = open('chloroplast_yuri/MAT.nex', 'rb')
for record in SeqIO.parse(handle, "nexus"):
    MAT.append(record)
handle.close()

handle = open('chloroplast_yuri/RPL.nex', 'rb')
for record in SeqIO.parse(handle, "nexus"):
    RPL.append(record)
handle.close()

handle = open('chloroplast_yuri/TL.nex', 'rb')
for record in SeqIO.parse(handle, "nexus"):
    TL.append(record)
handle.close()

SeqIO.write(ITS, "final/ITS.fasta", "fasta")
SeqIO.write(ETS, "final/ETS.fasta", "fasta")
SeqIO.write(LF, "final/trnLF.fasta", "fasta")
SeqIO.write(MAT, "final/matK.fasta", "fasta")
SeqIO.write(RPL, "final/rpl16.fasta", "fasta")
SeqIO.write(TL, "final/trnTL.fasta", "fasta")
