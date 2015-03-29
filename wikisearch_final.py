# Written by Robbie Barrat, 2014-2015 #
__author__ = 'Robbie Barrat'

# Great wikipedia API. now i can focus on using wikipedia data rather than getting it #
import wikipedia

# Urllib is used to open up non-wikipedia webpages and look for keywords #
import urllib

# Used for splitting text into sentences, I didn't want to reinvent the wheel. #
import re



# Here is just where the lists are established; most of them empty to be filled in by functions later. The 'bannedsites'
# list contains keywords of URLs that my search engine can't parse very well since they have a lot of information #
bannedsites = ["wiki", "youtube", "books.google", "wikibooks", "wikipedia", "yahoo"]
sourceslist = []
refinedlist = []
garbagelist = []

# This function just defines the wikipedia page for the appropriate subject and runs it through the breakinto function #
def findarticle(subject, keyword):
    page = wikipedia.page(subject)
    pagecontent = page.content
    breakinto(pagecontent, keyword)


# This function breaks the page content into a list based on different sentence terminators #
def breakinto(pagecontent, keyword):
    # The different sentence terminators are below #
    sentences = re.split(r' *[\.\?!][\'"\)\]]* *', pagecontent)
    findsentence(sentences, keyword)


# Just scans the list of sentences created above for keywords #
def findsentence(sentences, keyword):
    for i in sentences:
        if keyword in i:
            sentencecheck(i)



# This function creates two lists, refinedlist and garbagelist. If the sentence it is processing does not meet certain
# requirements it is put on the garbagelist.
def sentencecheck(sentence):
    if len(sentence) < 5 or sentence[0].isupper() == False:
        garbagelist.append(sentence)
    else:
        refinedlist.append(sentence)

# Simply prints everything in a list; hence the name 'printeverything' #
def printeverything(list):
    for i in list:
        print str(i)


# Scrolls through the references section of wikipedia pages to find a document that includes a keyword #
def references(subject, keyword, sourcequestion):
    page = wikipedia.page(subject)
    sources = page.references
    for i in sources:
        if sourcequestion > 0:
            # google books completely destroyed the keyword searcher #
            if bannedcheck(i) == ("clean"):
                webpage = urllib.urlopen(i).read()
                if keyword in webpage or keyword in i:
                    sourcequestion = sourcequestion - 1
                    sourceslist.append(i)
        else:
            printeverything(sourceslist)
            break



# Just checks to see if the website is on the bannedsites list, and tells the above function whether or not the site is#
# good to parse or not. #
def bannedcheck(website):
    for i in bannedsites:
        if i in website:
            return ("banned")
        else:
            return ("clean")


# All these next two lines do is take user input #
subject = raw_input("What is the subject of your question? ")
keyword = raw_input("Enter a keyword to look for. ")

# Runs the user input through the findarticle function #
findarticle(subject, keyword)
printeverything(refinedlist)
# These next few lines are also input #
sourcequestion = raw_input(
    "A list of relevant URLs can be displayed; this may take about 5-10 seconds per URL. How many urls do you want?: ")

# I had to turn sourcequestion into an integer so that it would return the correct amount of URLS #
sourcequestion = int(sourcequestion)
references(subject, keyword, sourcequestion)