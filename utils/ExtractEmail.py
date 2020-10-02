def extract_email(text):
	start=text.find("Contact Information")
	end=text.find("Summary")
	email=text[start+19:end]
	try:
		email=email.split()[0]
		email=email[1:len(email)]
		return email
	except Exception as e:
		return None