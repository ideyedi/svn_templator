"""
 Author : Eunseok Ji (eyedi)
"""
import sys
import os

def __combine_content__(templ, commit):
	# Get templete file contents
	templ_form = open(templ, 'r')
	templ_content = templ_form.read()
	templ_form.close() # closed 

	commit_form = open(commit, 'r')
	commit_content = commit_form.read()
	# not closed !!

	tot_content = templ_content + commit_content
	commit_form = open(commit, 'w')
	commit_form.write(tot_content)


def __init__() :
	commit_file = sys.argv[2]
	templete_file = sys.argv[1]
	__combine_content__(templete_file, commit_file)


__init__()
