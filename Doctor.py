

class Doctor:

    CSV_HEADER = ['Doctor Name', 'Specialization', 'Experiences', 'Telephone', 'City', 'State', 'Address', 'Image link']

    def __init__(self, name, image_link, specialization, experiences, city, state, address, telephone):
        self._name = name
        self._image_link = image_link
        self._specialization = specialization
        self._experience = experiences
        self._city = city
        self._state = state
        self._address = address
        self._telephone = telephone

    def get_name(self):
        return self._name

    def set_name(self, name):
        if name is not None:
            name = ""
        self._name = name.strip()

    name = property(get_name, set_name)

    def get_image_link(self):
        return self._image_link

    def set_image_link(self, image_link):
        if image_link is not None:
            image_link = ""
        self._image_link = image_link.strip()

    image_link = property(get_image_link, set_image_link)

    def get_specialization(self):
        return self._specialization

    def set_specialization(self, specialization):
        if specialization is not None:
            specialization = ""
        self._specialization = specialization.strip()

    specialization = property(get_specialization, set_specialization)

    def get_experience(self):
        return self._experience

    def set_experience(self, experience):
        if experience is not None:
            experience = ""
        self._experience = experience.strip()

    experience = property(get_experience, set_experience)

    def get_city(self):
        return self._city

    def set_city(self, city):
        if city is not None:
            city = ""
        self._city = city.strip()

    city = property(get_city, set_city)

    def get_state(self):
        return self._state

    def set_state(self, state):
        if state is not None:
            state = ""
        self._state = state.strip()

    state = property(get_state, set_state)

    def get_address(self):
        return self._address

    def set_address(self, address):
        if address is not None:
            address = ""
        self._address = address.strip()

    address = property(get_address, set_address)

    def get_telephone(self):
        return self._telephone

    def set_telephone(self, telephone):
        if telephone is not None:
            telephone = ""
        self._telephone = telephone.strip()

    telephone = property(get_telephone, set_telephone)

    def to_csv(self):
        return [self.name, self.specialization, self.experience, self.telephone, self.city, self.state, self.address,
                self.image_link]

    def __str__(self):
        return "Doctor: [{0}], Especializations: [{1}], Experience: [{2}], Telephone: [{3}], Address: [{4}][{5}][{6}]"\
            .format(self.name, self.specialization, self.experience, self.telephone, self.address, self.city,
                    self.state)
