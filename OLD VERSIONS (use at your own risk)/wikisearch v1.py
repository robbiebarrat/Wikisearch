import wikipedia
# Used for splitting text into sentences, I didn't want to reinvent the wheel. #
import re
# Written by Robbie Barrat, 2014-2015 #
def findarticle(subject, keyword):
    page =  wikipedia.page(subject)
    pagecontent = page.content
    breakinto(pagecontent, page, subject, keyword)
def breakinto(pagecontent, keyword):
    sentences = re.split(r' *[\.\?!][\'"\)\]]* *', pagecontent)
    findsentence(pagecontent, keyword)



def findsentence(pagecontent, keyword):


def stringconvert():

subject = raw_input("What is the subject of your question? ")
keyword = raw_input("Enter a keyword to look for. ")

findarticle(subject, keyword)