#lib for importing Regular Expresions
import re

#There are certain patterns which are difficult to get by only using traditional if and else 
# conditions. So, in order to make it more simple we use regualr expressions. It can be used 
# for various things such as in this i case just spliting all the alpanumeric charcters in a list.
# It matches all the alpha numeric strings breaks when there is a special charcter such as .,*..etc
# and appends the string into the list. It makes work very easy 

#Function for extracting the name from resume
def extract_name(resume_text):

	#Split all the alphanumeric strings and append in list_names
	list_names=re.findall(r"[\w]+",resume_text)

	#Just in case if get a null string or a single string we are using try block
	try:
		return list_names[0]+" "+list_names[1]
	
	#Returns null if there are no strings in the list
	except Exception as e:
		return None