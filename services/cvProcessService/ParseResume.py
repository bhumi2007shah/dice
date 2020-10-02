from Config import config
from model.Candidate import Candidate
from utils.ExtractSkills import extract_skills
from utils.ExtractEducation import extract_education
from utils.ExtractEmail import extract_email
from utils.ExtractMobile import extract_mobile_number
from utils.ExtractName import extract_name
from utils.ExtractCompany import extract_company
from utils.ExtractProfile import extract_profile
from services.FileService import convert_to_text

def extractData(parsed_text):
	candidate = Candidate()
	# extracting candidate name
	try:
		candidate.firstName = candidate.candidateName.split()[0]
		candidate.lastName = candidate.candidateName.split()[len(candidate.candidateName.split()) - 1]
		candidate.candidateName = extract_name(parsed_text)
	except Exception as e:	
		candidate.candidateName = extract_name(parsed_text)
	
	# extracting candidate mobile numbers
	candidate.mobile = extract_mobile_number(parsed_text);
	
	# extracting candidate email
	candidate.email = extract_email(parsed_text)
	
	# extracting candidate's skills
	candidate.candidateSkillDetails = extract_skills(parsed_text, bool(0)) 	#skillset also can be used

	# extracting candidate's education
	candidate.candidateEducationDetails = extract_education(parsed_text)
	
	# extracting candidate's previous companies
	candidate.candidateCompanyDetails = extract_company(parsed_text)
	
	# extracting candidate's profile sources
	candidate.profileSources = extract_profile(parsed_text)
	
	# return Candidate object
	return candidate.toJSON()


def parseResume(fileName):
	try:
		text = convert_to_text(fileName)
	except Exception as e:
		raise Exception(e)

	if text != "":
		Candidate = extractData(text)
		return Candidate;
	else:
		candidate=Candidate()
		return candidate
