from model.CandidateProfileDetails import CandidateProfileDetails

def extract_profile(resume_text):
    start=resume_text.find("Profile Sources")
    profile_details=[]
    text=resume_text[start+16:len(resume_text)]
    profiles=text.split('\uf0b7')
    for profile in profiles:
        Profile=CandidateProfileDetails()
        Profile.profileType=profile.split(':')[0]
        start=profile.find(':')
        Profile.url=profile[start+1:len(profile)].strip()
        profile_details.append(Profile)
    return profile_details