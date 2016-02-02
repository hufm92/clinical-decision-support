'''
TREC Clinical Decision Support 2015
SIGIR 2016
School of Information, Department of Learning Health Science
Author: Fengmin Hu
This is a module to define the concept class
'''
import re

class concept():
	''' Define a concept class '''
	neg = False
	score = 0
	CUI = ''
	string = ''
	preferred_name = ''
	semantic_type = ''

class concept_neg():
	''' Define a negation concept class'''
	NegType = ''
	NegTrigger = ''
	TriggerPosInfo = []
	NegConcept = []
	ConceptPosInfo = []
	source = 'description'

	def __init__(self, negation, summary_pos = 0):
		'''
		negation is a list of following variables
		negation(TypeOfNegation,
			 NegationTrigger, TriggerPosInfo,
			 NegationConcept, ConceptPosInfo)
		'''
		elem = negation.split(',',2)
		self.NegType = elem[0]
		self.NegTrigger = elem[1]
		self.TriggerPosInfo = []
		self.NegConcept = []
		self.ConceptPosInfo = []
		pattern = re.compile(r'\[([^\]]*)\]')
		match = re.findall(pattern, elem[2])

		PosInfo = match[0].split(',')
		for item in PosInfo:
			tmp = {}
			tmp['StartPos'] = int(item.split('/')[0])
			tmp['Length'] = int(item.split('/')[1])
			self.TriggerPosInfo.append(tmp)

		Concept = match[1].split(',')
		for item in Concept:
			tmp = {}
			tmp['CUI'] = item.split(':')[0].strip("'")
			tmp['String'] = item.split(':')[1].strip("'")
			self.NegConcept.append(tmp)

		PosInfo = match[2].split(',')
		for item in PosInfo:
			tmp = {}
			tmp['StartPos'] = int(item.split('/')[0])
			tmp['Length'] = int(item.split('/')[1])
			self.ConceptPosInfo.append(tmp)
			if tmp['StartPos'] >= summary_pos:
				self.source = 'summary'

	def show(self):
		print "NegType: "+self.NegType
		print "NegTrigger: "+self.NegTrigger
		print "TriggerPosInfo: "
		print self.TriggerPosInfo
		print "NegConcept: "
		print self.NegConcept
		print "ConceptPosInfo"
		print self.ConceptPosInfo
		print "source"
		print self.source
