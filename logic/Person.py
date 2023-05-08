
from Address import Address


class Person(object):
    """
    Class used to represent a Person
    """

    def __init__(self, dni: int = 0, name: str = 'Name', last_name: str = "LastName", contact: int = 0,
                 address: Address = Address, permission: int = 0):
        """ Person constructor object.

        :param dni: id of person.
        :type dni: int
        :param name: name of person.
        :type name: str
        :param last_name: last name of person.
        :type last_name: str
        :param contact: person contact.
        :type contact: int
        :param address: address of person
        :type address: object
        :param permission: permission of person
        :type permission: int
        :returns: Person: object
        :rtype: Person
        """
        self._dni = dni
        self._name = name
        self._last_name = last_name
        self._contact = contact
        self._address = address
        self._permission = permission

    @property
    def id_person(self) -> int:
        """
        Returns id person of the person.
          :returns: id of person.
          :rtype: int
        """
        return self._dni

    @id_person.setter
    def id_person(self, id_person: int):
        """
        The id of the person.
        :param id_person: id of person.
        :type: int
        """
        self._dni = id_person

    @property
    def name(self) -> str:
        """ Returns the name of the person.
          :returns: name of person.
          :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """ The name of the person.
        :param name: name of person.
        :type: str
        """
        self._name = name

    @property
    def last_name(self) -> str:
        """ Returns the last name of the person.
          :returns: last name of person.
          :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name: str):
        """ The last name of the person.
        :param last_name: last name of person.
        :type: str
        """
        self._last_name = last_name

    @property
    def contact(self) -> int:
        """
        Returns the contact of the person.
        :returns: contact of person.
        :rtype: int
      """
        return self._contact

    @contact.setter
    def contact(self, contact: int):
        """
      The contact of the person.
      :param contact: contact of the person
      :type: int
      """
        self.contact = contact

    @property
    def address(self) -> object:
        """
        Returns address of the person.
          :returns: address of person.
          :rtype: object
        """
        return self._address

    @address.setter
    def address(self, address: object):
        """
        The address of the person.
        :param address: address of person.
        :type: object
        """
        self._address = address

    @property
    def permission(self) -> int:
        """
        Returns permission of the person.
          :returns: permission of person.
          :rtype: int
        """
        return self._permission

    @permission.setter
    def permission(self, permission: int):
        """
        The permission of the person.
        :param permission: permission of person.
        :type: int
        """
        self._permission = permission

    def __str__(self):
        """
        Returns str of person.
          :returns: sting person
          :rtype: str
        """
        return '({0}, {1}, {2}, {3}, {4}, {5})'.format(self.id_person, self.name, self.last_name, self.contact,
                                                  self.address, self.permission)


class User(Person):
    def __init__(self, dni: int = 0, name: str = 'Name', last_name: str = "LastName", contact: int = 0,
                 address: Address = Address(), permission = 0):

        super().__init__(dni, name, last_name, contact, address, permission)
        self.permission = permission


class Operator(Person):
    def __init__(self, dni: int = 0, name: str = 'Name', last_name: str = "LastName", contact: int = 0,
                 address: Address = Address(), permission = 1):

        super().__init__(dni, name, last_name, contact, address, permission)
        self.permission = permission


if __name__ == '__main__':
    person1 = Person(dni=1234567890, name="Luis", last_name="Pinto", contact=3155264684, address=Address, permission=1)
    print("\nPerson:")
    print(person1)

    person2 = Person()
    print(person2)
