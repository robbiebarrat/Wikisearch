import wikipedia
# Used for splitting text into sentences, I didn't want to reinvent the wheel. #
import re
# Written by Robbie Barrat, 2014-2015 #
def findarticle(subject, keyword):
    page =  wikipedia.page(subject)
    pagecontent = page.content
    breakinto(pagecontent, keyword)
def breakinto(pagecontent, keyword):
    sentences = re.split(r' *[\.\?!][\'"\)\]]* *', pagecontent)
    findsentence(sentences, keyword)

def findsentence(sentences, keyword):
    # somehow incorporate a fact-finding algorithm here #
    for i in sentences:
        if keyword in i:
            #i = targetsentence
            print i
    # in the future you should send target sentences to be refined #

subject = raw_input("What is the subject of your question? ")
keyword = raw_input("Enter a keyword to look for. ")

findarticle(subject, keyword)
