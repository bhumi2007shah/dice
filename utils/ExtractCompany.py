from model.CandidateCompanyDetails import CandidateCompanyDetails

def extract_company(resume_text):
    print(resume_text)
    start=resume_text.find("Work History")
    end=resume_text.find("Education")
    text=resume_text[start+13:end]
    company_details=[]
    comapnies=text.split('\uf0b7')
    for company in comapnies:
        Company= CandidateCompanyDetails()
        Company.companyName=company.split('|')[0].split('-')[0]
        Company.designation=company.split('|')[1].split()[0]
        if(len(company.split('|'))>2):
            Company.location=company.split('|')[len(company.split('|'))-1]
        if(len(company.split('|'))>3):    
            if(len(company.split('|')[3].split('-'))>0):
                Company.startDate=company.split('|')[3].split('-')[0]
                Company.endDate=company.split('|')[3].split('-')[1]
        company_details.append(Company)
    return company_details