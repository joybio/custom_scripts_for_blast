#!/root/miniconda3/bin/python
#coding:utf-8
''' filter scafflods by min len 500 '''

__date__ = "2020-6-19"
__author__ = "Junbo Yang"
__email__ = "yang_junbo_hi@126.com"
__license__ = "Joybio"

import optparse
import os
import re
import csv
from optparse import OptionParser

parser = OptionParser('Usage: python %prog -i scaffolds.fasta -o scaffolds.500.fasta')

parser.add_option('-i','--input',
                dest='input',
                help='scaffolds.fasta')

(options,args) = parser.parse_args()

# 函数功能：调用blastn软件对fast文件进行对比分析并生成结果文件。
os.system('blastn -query ' + options.input + ' -db /media/ruizhi/database/NR.database/nt_format -out nt_result -outfmt 6 -num_threads 30 -max_target_seqs 2 -max_hsps 1')
useblastn(query)
# 函数功能：将分析结果文件转换为csv文件。
def result_csv(file):
	csvfile=file + '.csv'
	resultfile = open(file_dir + file, 'r')
	resultfile_read = resultfile.readlines()
	elementlist = []
    # elementlist.append("query,subject\tidentity\tlength\tmismatch\tgap\tstart_q\tend_q\tstart_s\tend_s\te value\tscore")
	elementlist.append(["query","subject","identity","length","mismatch","gap","start_q","end_q","start_s","end_s","e value","score"])
    # print(elementlist[0])
	for row in resultfile_read:
		eachrow = re.split('[\t]',row)
		elementlist.append(eachrow)
	with open(csvfile, 'w', newline = '') as t_file:
		csv_writer = csv.writer(t_file)
		csv_writer.writerows(elementlist)
	resultfile.close()
result_csv("nt_result")
os.remove('nt_result')
