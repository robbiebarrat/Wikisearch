rimport wikipedia
# Great API that lets me focus on using the wikipedia data; not getting it #
import urllib
# Used for looking through the links it opens in the ‘references’ section. #
import re
# Used for splitting text into sentences, I didn't want to reinvent the wheel. #
# Written by Robbie Barrat, 2014-2015 #
def findarticle(subject, keyword):
    page =  wikipedia.page(subject)
    pagecontent = page.content
    breakinto(pagecontent, keyword)


# All this does is break the code into a list based on different ‘sentence terminators’ #
def breakinto(pagecontent, keyword):
    sentences = re.split(r' *[\.\?!][\'"\)\]]* *', pagecontent)
    findsentence(sentences, keyword)


# Searches through the list for sentences containing keywords #
def findsentence(sentences, keyword):
    # somehow incorporate a fact-finding algorithm here #
    for i in sentences:
        if keyword in i:
            print i
    # in the future you should send target sentences to be refined #

# This scans through the ‘references’ section on the wikipedia page #
def references(subject, keyword, sourcequestion):
	page = wikipedia.page(subject)
	sources = page.references
	for i in sources:
		if sourcequestion > 0:
			# scan the webpage for the keyword submitted by the user earlier #
			webpage = urllib.urlopen(str(i)).read()
			if keyword in webpage:
				print i
				# subtract 1 from the ‘number of URLS’ the user submitted earlier #
				sourcequestion = sourcequestion - 1



# Just get basic user input #
subject = raw_input("What is the subject of your question? ")
keyword = raw_input("Enter a keyword to look for. ")


findarticle(subject, keyword)

# This gets URLS whose content contains the user submitted keyword #
sourcequestion = raw_input("A list of relevant URLs can be displayed; this may take about 5-10 seconds per URL. How many urls do you want?: ")
references(subject, keyword, int(sourcequestion))
#				^ Type had to be integer because it kept messing up and treating it like a string #
