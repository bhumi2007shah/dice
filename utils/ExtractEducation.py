from model.CandidateEducationDetails import CandidateEducationDetails

def extract_education(resume_text):
    start=resume_text.find("Education")
    end=resume_text.find("Skills")
    text=resume_text[start+10:end]
    education_details=[]
    educations=text.split('\uf0b7')
    for edu in educations:
        Education = CandidateEducationDetails()
        Education.degree=edu.split(',')[0]
        Education.instituteName=edu.split('|')[len(edu.split('|'))-1]
        try:
            Education.yearOfPassing=edu.split('-')[1].split('|')[0]
            education_details.append(Education)
        except Exception as e:
            education_details.append(Education)
    return education_details