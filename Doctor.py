

class Doctor:

    def __init__(self, name, image_link, specialization, experience):
        self._name = name
        self._image_link = image_link
        self._specialization = specialization
        self._experience = experience

    def get_name(self):
        return self._name

    def set_name(self, name):
        if name == None:
            name = ""
        self._name = name

    name = property(get_name, set_name)
