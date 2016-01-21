'''
TREC Clinical Decision Support 2015
SIGIR 2016
University of Michigan
School of Information, Department of Learning Health Science
Author: Fengmin Hu
This is the main function
'''

import os
import sys
import query
import experiment

class data():
    num = 0
    file_name_text = []
    file_name_MetaMap = []
    querylist = list()

    def __init__(self, dirlist):
	self.file_name_text = os.listdir(dirlist['text'])
	self.file_name_MetaMap = os.listdir(dirlist['MetaMap'])
	self.file_name_text.sort()
	self.file_name_MetaMap.sort()
	'''Get the filelists in text and MetaMapped text formats and keep them ordered'''
	if len(self.file_name_text) != len(self.file_name_MetaMap):
	    print "Number of Text files: "+str(len(self.file_name_text))
	    print "Number of MetaMap files: "+str(len(self.file_name_MetaMap))
	    sys.exit("Error: The numbers of files in text and MetaMapped text formats don't match!")
	self.num = len(self.file_name_text)
	for idx in xrange(self.num):
	    dir_text = dirlist['text']+'/'+self.file_name_text[idx]
	    dir_MetaMap = dirlist['MetaMap']+'/'+self.file_name_MetaMap[idx]
	    query_tmp = query.query(dir_text, dir_MetaMap)
	    self.querylist.append(query_tmp)

def Dir_init():
    ''' Initialize the directory'''
    global directory
    directory = {}
    directory['train'] = {}
    directory['test'] = {}
    directory['train']['text'] = '/storage6/users/hufm/SIGIR/Query/2014/2014-original'
    directory['train']['MetaMap'] = '/storage6/users/hufm/SIGIR/Query/2014/2014-original-MMed'
    directory['test']['text'] = '/storage6/users/hufm/SIGIR/Query/2015/2015-original'
    directory['test']['MetaMap'] = '/storage6/users/hufm/SIGIR/Query/2015/2015-original-MMed'
    directory['stopwords'] = '/storage6/users/hufm/SIGIR/Data/stopwords.txt'
    directory['semantictype'] = '/storage6/users/hufm/SIGIR/Data/SemanticTypes.txt'

def main():
    Dir_init()
    train_data = data(directory['train'])
    test_data = data(directory['test'])
    print train_data.querylist[0].querytype
    print train_data.querylist[0].summary
    print train_data.querylist[0].description
    
    

 
if __name__ == "__main__":
    main()

