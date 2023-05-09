
class Address(object):
    """
    Class used to represent an Address
    """

    def __init__(self, house_number: int = 1, apartment: int = 0, street: str = 'street', postal_code: str = '00000',
                 locality: str = 'locality', department: str = 'department', country: str = 'country'):
        """ Address constructor object.

        :param house_number: number of house.
        :type house_number: int
        :param street: name of street.
        :type street: str
        :param apartment: department of street.
        :type apartment: int
        :param postal_code: last name of city.
        :type postal_code: str
        :param locality: name of state.
        :type locality: str
        :param locality: name of state.
        :type : str
        :param department: department of the country.
        :type department: str
        :param country: name of the country.
        :type country: str
        :returns: Address object
        :rtype: Address
        """
        self.__house_number = house_number
        self.__apartment = apartment
        self.__street = street
        self.__postal_code = postal_code
        self.__locality = locality
        self.__department = department
        self.__country = country

    @property
    def house_number(self) -> int:
        """ Returns house number of the address.
          :returns: house number of address.
          :rtype: int
        """
        return self.__house_number

    @house_number.setter
    def house_number(self, house_number: int):
        """
        The house number of the address.
        :param house_number: house number of the address.
        :type: int
        """
        self.__house_number = house_number

    @property
    def apartment(self) -> int:
        """ Returns apartment number of the address.
          :returns: apartment number of address.
          :rtype: int
        """
        return self.__apartment

    @apartment.setter
    def apartment(self, apartment: int):
        """
        The apartment number of the address.
        :param apartment: apartment number of the address.
        :type: int
        """
        self.__apartment = apartment

    @property
    def street(self) -> str:
        """
        Returns the name of street of the address.
          :returns: name of street of address.
          :rtype: str
        """
        return self.__street

    @street.setter
    def street(self, street: str):
        """
        The name of street of the address.
        :param street: name of address.
        :type: str
        """
        self.__street = street

    @property
    def postal_code(self) -> str:
        """
        Returns the postal_code of the address.
          :returns: last postal_code of address.
          :rtype: str
        """
        return self.__postal_code

    @postal_code.setter
    def postal_code(self, postal_code: str):
        """
        The postal_code of the address.
        :param postal_code: postal_code of address.
        :type: str
        """
        self.__postal_code = postal_code

    @property
    def locality(self) -> str:
        """
      Returns the locality of the address.
        :returns: locality of address.
        :rtype: str
      """
        return self.__locality

    @locality.setter
    def locality(self, locality: str):
        """
        The locality of the address.
      :param locality: locality of the address
      :type: str
      """
        self.__locality = locality

    @property
    def department(self) -> str:
        """ Returns department of the address.
          :returns: department of address.
          :rtype: str
        """
        return self.__department

    @department.setter
    def department(self, department: str):
        """
        The department of the address.
        :param department: department of the address.
        :type: int
        """
        self.__department = department

    @property
    def country(self) -> str:
        """
        Returns the country of the address.
            :returns: country of address.
            :rtype: str
      """
        return self.__country

    @country.setter
    def country(self, country: str):
        """
        The country of the address.
      :param country: country of the address
      :type: str
      """
        self.__country = country

    def __str__(self):
        """
        Returns str of address.
          :returns: sting person
          :rtype: str
        """
        return '({0}, {1}, {2}, {3}, {4}, {5}, {6})'.format(self.__house_number, self.__street, self.__apartment,
                                                            self.__postal_code, self.__locality, self.__department,
                                                            self.__country)


if __name__ == '__main__':
    address1 = Address(house_number=7, street="San martin", apartment=1001, postal_code="00045", locality="locality",
                       department="Bolivar", country="Colombia")
    print("\nAddress:")
    address1.name = "address1"
    print(address1)

    address2 = Address()
    print(address2)
