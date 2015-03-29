# Great wikipedia API. now i can focus on using wikipedia data rather than getting it #
import wikipedia
# Urllib is used to open up non-wikipedia webpages and look for keywords #
import urllib
# Used for splitting text into sentences, I didn't want to reinvent the wheel. #
import re
# Written by Robbie Barrat, 2014-2015 #


# This function just defines the wikipedia page for the appropriate subject and runs it through the breakinto function #
def findarticle(subject, keyword):
    page =  wikipedia.page(subject)
    pagecontent = page.content
    breakinto(pagecontent, keyword)


# This function breaks the page content into a list based on different sentence terminators #
def breakinto(pagecontent, keyword):
	# The different sentence terminators are below #
    sentences = re.split(r' *[\.\?!][\'"\)\]]* *', pagecontent)
    findsentence(sentences, keyword)


# Just scans the list of sentences created above for keywords #
def findsentence(sentences, keyword):
    # somehow incorporate a fact-finding algorithm here #
    for i in sentences:
        if keyword in i:
            #i = targetsentence
            print i
    # in the future you should send target sentences to be refined #


# Scrolls through the references section of wikipedia pages to find a document that includes a keyword #
def references(subject, keyword, sourcequestion):
	page = wikipedia.page(subject)
	sources = page.references
	for i in sources:
		if sourcequestion > 0:
			# google books completley destroyed the keyword searcher #
			if "books.google" not in i and "wiki" not in i:
				webpage = urllib.urlopen(i).read()
				if keyword in webpage or keyword in i:
					sourcequestion = sourcequestion - 1
					print i


# All these next two lines do is take user input #	
subject = raw_input("What is the subject of your question? ")
keyword = raw_input("Enter a keyword to look for. ")

# Runs the user input through the findarticle function #
findarticle(subject, keyword)

# These next few lines are also input #
sourcequestion = raw_input("A list of relevant URLs can be displayed; this may take about 5-10 seconds per URL. How many urls do you want?: ")

# I had to turn sourcequestion into an integer so that it would return the correct amount of URLS #
sourcequestion = int(sourcequestion)
references(subject, keyword, sourcequestion)
