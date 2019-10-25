class Client:

    def __init__(self, preferred_language="", name="", legal_name="", primary_email="", secondary_email="",
                 primary_phone="", secondary_phone="", fax="", postal_code="", country="", state="", city="",
                 address_line_1="", address_line_2="", note=""):
        self.preferred_language = preferred_language
        self.name = name
        self.legal_name = legal_name
        self.primary_email = primary_email
        self.secondary_email = secondary_email
        self.primary_phone = primary_phone
        self.secondary_phone = secondary_phone
        self.fax = fax
        self.postal_code = postal_code
        self.state = state
        self.country = country
        self.city = city
        self.address_line_1 = address_line_1
        self.address_line_2 = address_line_2
        self.note = note
