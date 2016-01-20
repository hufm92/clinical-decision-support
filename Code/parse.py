'''
TREC Clinical Decision Support 2015
SIGIR 2016
University of Michigan
School of Information, Department of Learning Health Science
Author: Fengmin Hu
This is a module to parse the MetaMapped files.
'''
import re
import sys
import concept

def neg_list(line, summary_pos = 0):
    '''
    neg_list(ListOfNegations).
    negation(TypeOfNegation, 
	     NegationTrigger, TriggerPosInfo,
	     NegationConcept, ConceptPosInfo)
    '''
    negation = []
    neglist_pattern = re.compile(r'neg_list\(\[(.*)\]\).')
    neglist_match = re.match(neglist_pattern, line)
    if neglist_match is None:
	sys.exit("Parsing Error: The line to be parsed doesn't follow the neg_list format. ")
    neglist_string = neglist_match.groups()[0]
    if len(neglist_string) == 0:
	return negation
    negation_pattern = re.compile(r'negation\(([^\)]*)\)')
    negation_match = re.findall(negation_pattern, neglist_string)
    for item in negation_match:
	tmp_Neg = concept.concept_neg(item, summary_pos)
	negation.append(tmp_Neg)
    return negation

def utterance_info(line):
    

def utterance_term(lines):
    line_num = len(line)


