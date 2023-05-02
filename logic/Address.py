
class Address(object):
    """
    Class used to represent an Address
    """

    def __init__(self, house_number: int = 1, street: str = 'street', apartment: int = 0, postal_code: str = '00000',
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
        self._house_number = house_number
        self._apartment = apartment
        self._street = street
        self._Postal_code = postal_code
        self._locality = locality
        self._department = department
        self._country = country

    @property
    def house_number(self) -> int:
        """ Returns house number of the address.
          :returns: house number of address.
          :rtype: int
        """
        return self._house_number

    @house_number.setter
    def house_number(self, house_number: int):
        """
        The house number of the address.
        :param house_number: house number of the address.
        :type: int
        """
        self._house_number = house_number

    @property
    def apartment(self) -> int:
        """ Returns apartment number of the address.
          :returns: apartment number of address.
          :rtype: int
        """
        return self._apartment

    @apartment.setter
    def apartment(self, apartment: int):
        """
        The apartment number of the address.
        :param apartment: apartment number of the address.
        :type: int
        """
        self._apartment = apartment

    @property
    def street(self) -> str:
        """
        Returns the name of street of the address.
          :returns: name of street of address.
          :rtype: str
        """
        return self._street

    @street.setter
    def name(self, street: str):
        """
        The name of street of the address.
        :param street: name of address.
        :type: str
        """
        self._street = street

    @property
    def city(self) -> str:
        """
        Returns the postal_code of the address.
          :returns: last postal_code of address.
          :rtype: str
        """
        return self._Postal_code

    @city.setter
    def city(self, city: str):
        """
        The postal_code of the address.
        :param city: postal_code of address.
        :type: str
        """
        self._Postal_code = city

    @property
    def state(self) -> str:
        """
      Returns the locality of the address.
        :returns: locality of address.
        :rtype: str
      """
        return self._locality

    @state.setter
    def state(self, state: str):
        """
        The locality of the address.
      :param state: locality of the address
      :type: str
      """
        self.state = state

    @property
    def department(self) -> str:
        """ Returns department of the address.
          :returns: department of address.
          :rtype: str
        """
        return self._department

    @department.setter
    def department(self, department: str):
        """
        The department of the address.
        :param department: department of the address.
        :type: int
        """
        self._department = department

    @property
    def country(self) -> str:
        """
        Returns the country of the address.
            :returns: country of address.
            :rtype: str
      """
        return self._country

    @country.setter
    def country(self, country: str):
        """
        The country of the address.
      :param country: country of the address
      :type: str
      """
        self.country = country

    def __str__(self):
        """
        Returns str of address.
          :returns: sting person
          :rtype: str
        """
        return '({0}, {1}, {2}, {3}, {4}, {5}, {6})'.format(self.house_number, self.street, self.apartment,
                                                            self.city, self.state, self.department, self.country)


if __name__ == '__main__':
    address1 = Address(house_number=7, street="San martin", apartment=1001, postal_code="00045", locality="localidad",
                       department="Bolivar",country="Colombia")
    print("\nAddress:")
    address1.name = "address1"
    print(address1)

    address2 = Address()
    print(address2)
