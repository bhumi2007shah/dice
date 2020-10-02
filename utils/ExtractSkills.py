from model.CandidateSkillDetails import CandidateSkillDetails

def extract_skills(text_data, isJdText):
	start=text_data.find("Skills")
	end=text_data.find("Work Preferences")
	skills=text_data[start+6:end].split('\uf0b7')
	skill_data=[]
	for skill in skills:
		Skill=CandidateSkillDetails()
		if(skill.split('|')[0]):
			Skill.skill=skill.split('|')[0]
		if(len(skill.split('|'))>2):
			Skill.lastUsed=skill.split('|')[2]
			skill_data.append(Skill)
	return skill_data