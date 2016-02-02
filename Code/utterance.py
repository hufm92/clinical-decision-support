'''
TREC Clinical Decision Support 2015
SIGIR 2016
University of Michigan
School of Information, Department of Learning Health Science
Author: Fengmin Hu
This is a module to define a parsed utterance class
'''

import parse

class utterance():
    '''Define a parsed utterance class'''
    UtteranceID = ''
    UtteranceText = ''
    PosInfo = {'StartPos':0, 'Length':0}
    Component = []    

    def __init__(self, utterance_tmp):
	info = parse.utterance_info(utterance_tmp['Info'])
