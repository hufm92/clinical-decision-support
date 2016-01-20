'''
TREC Clinical Decision Support 2015
SIGIR 2016
University of Michigan
School of Information, Department of Learning Health Science
Author: Fengmin Hu
This is a module to define the query class
'''

import parse

class query():
    '''Define a query class'''
    querytype = ''
    description = ''
    summary = ''
    summary_pos = 0
    neg_list = []

    def __init__(self, dir_text, dir_MetaMap):
	self.text_init(dir_text)
	self.MetaMap_init(dir_MetaMap)

    def text_init(self, dir_text):
	'''
	Get the information from Text files.
	Type: Diagnosis/Test/Treatment
	Summary: A simplified version of the narratives that contain less irrelevent information.
	Description: A complete account of the patients' visits, including details such as their vital statistics, drug dosages, etc.
	'''
	textinput = open(dir_text,'rU')
	text_info = textinput.readlines()
	self.querytype = text_info[0].strip().strip('.')
	self.description = text_info[1].strip()
	self.summary = text_info[2].strip()
	self.summary_pos = len(text_info[0])+len(text_info[1])
	# print self.summary_pos

    def MetaMap_init(self, dir_MetaMap):
	'''
	Get the information from MetaMapped files.
	Format:
	1. args
	2. aas
	3. neg_list
	4. utterance
	    A list of (phrase, candidate, mappings)
	5. 'EOU': End of Utterance Marker.
	'''
	MetaMapinput = open(dir_MetaMap,'rU')
	MetaMap_info = MetaMapinput.readlines()
	for line in MetaMap_info:
	    if line.startswith('neg_list'):
		self.neg_list = parse.neg_list(line, self.summary_pos)
	

