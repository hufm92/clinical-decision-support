'''
TREC Clinical Decision Support 2015
SIGIR 2016
University of Michigan
School of Information, Department of Learning Health Science
Author: Fengmin Hu
This is a module to define the query class
'''

class query():
    '''Define a query class'''
    querytype = ''
    summary = ''
    description = ''

    def __init__(self, dir_text, dir_MetaMap):
	self.text_init(dir_text)
	self.MetaMap_init(dir_MetaMap)

    def text_init(dir_text):
	'''
	Get information from Text input
	Type: Diagnosis/Test/Treatment
	Summary: A simplified version of the narratives that contain less irrelevent information.
	Description: A complete account of the patients' visits, including details such as their vital statistics, drug dosages, etc.
	'''
	textinput = open(dir_text,'rU')
	text_info = textinput.readlines()
	self.querytype = text_info[0].strip().strip('.')
	self.summary = text_info[1].strip()
	self.description = text_info[2].strip()

    def MetaMap_init(dir_MetaMap):
	

