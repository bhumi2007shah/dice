def extract_mobile_number(text):
    start=text.find("Contact Information")
    end=text.find("Summary")
    mobile_number=text[start:end]
    mobile_number=mobile_number.split()[2]
    start=mobile_number.find('\uf0b7')
    return mobile_number[start+1:len(mobile_number)]