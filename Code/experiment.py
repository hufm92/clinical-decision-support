# coding=utf-8
'''
TREC Clinical Decision Support 2015
SIGIR 2016
University of Michigan
School of Information, Department of Learning Health Science
Author: Fengmin Hu
This is the module to run experiments
'''

import os

def CreateParam(params, queries):
	'''
	Generate the IndriRunQuery Parameter files
	params = {
	Dir: directory of Parameter file
	index: directory of Index Files
	runID: ID of this run
	memory: default = 16G
	count: default = 1000
	trecFormat：default = True
	fbDocs: default = 20
	fbTerms: default = 10
	fbOrigWeight: default = 0.5
	stopwords:
		remove: default = True, remove
		words: list of stopword
	}
	'''

	outputfile = open(params['Dir'], 'wb')
	outputfile.write('<parameter>\n')
	for item in params:
		if item != 'Dir' and item != 'stopwords':
			outputfile.write('\t'+'<'+item+'>'+str(params[item])+'</'+item+'>\n')
	for idx in xrange(len(queries)):
		query_tmp = queries[idx]
		outputfile.write('\t<query>\n')
		outputfile.write('\t\t<number>'+str(idx+1)+'</number>\n')
		outputfile.write('\t\t<text>')
		IndriQuery = ''
		for item in query_tmp:
			if item['Type'] == 'text':
				for term in item['String']:
					IndriQuery = IndriQuery + ' ' + term
				continue
			if item['Type'] in ['syn', 'combine']:
				IndriQuery = IndriQuery + ' #' + item['Type'] + '('
				for term in item['String']:
					IndriQuery = IndriQuery + ' ' + term
				IndriQuery = IndriQuery + ')'
		outputfile.write(IndriQuery + '</text>\n')
		outputfile.write('\t</query>\n')
	if params['stopwords']['remove']:
		outputfile.write('\t<stopper>\n')
		for item in params['stopwords']['words']:
			outputfile.write('\t\t<word>'+item+'</word>\n')
		outputfile.write('\t</stopper>')
	outputfile.write('</parameter>')
	outputfile.close()