

class Doctor:

    def __init__(self, name, image_link, specialization, experience):
        self._name = name
        self._image_link = image_link
        self._specialization = specialization
        self._experience = experience

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

    def __str__(self):
        return "Doctor: [{0}], Especializations: [{1}], Experience: [{2}]"\
            .format(self.name, self.specialization, self.experience)
