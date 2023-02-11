"""
@author: Ramon
@date: 11/02/2023
    This class is going to calculate how many years will it take
    to generate passive for a given income from renting apts.
"""


class Calculator:
    """_summary_"""

    def __init__(
        self,
        desired_passive_income: float,
        yearly_savings: float,
        starting_year: int,
        apartment_value: float, 
        yearly_apartment_rent_income: float,
    ):
        self.desired_passive_income = desired_passive_income
        self.yearly_savings = yearly_savings
        self.starting_year = starting_year
        self.apartment_value = apartment_value
        self.yearly_apartment_rent_income = yearly_apartment_rent_income
        self.calculator_data = dict()
        self.initial_passive_income = 0

        if (
            not isinstance(self.desired_passive_income, (float, int))
            or not isinstance(self.yearly_savings, (float, int))
            or not isinstance(self.starting_year, int)
            or not isinstance(self.apartment_value, (float, int))
            or not isinstance(self.yearly_apartment_rent_income, (float, int))
        ) or (
            isinstance(self.desired_passive_income, bool)
            or isinstance(self.yearly_savings, bool)
            or isinstance(self.starting_year, bool)
            or isinstance(self.apartment_value, bool)
            or isinstance(self.yearly_apartment_rent_income, bool)
        ):
            raise TypeError(
                "All parameter values must be a number, try declaring the class again"
            )

    def create_dictionary(
        self,
        year_balance=0,
        passive_income=0,
        number_of_apartments: int = 0,
        number_of_apartments_purchased = 0
    ) -> dict:
        """_summary_

        Args:
            year_balance (int, optional): the year_balance of the account.
                Defaults to 0 as we start with nothing
            passive_income (int, optional): the passive_income of the year.
                Defaults to 0 as we start with nothing
            number_of_apartments (int, optional): the number of apartments at the end of the year.
                Defaults to 0 as we start with nothing

        Returns:
            self.calculator_data: A dictionary containg the current year as Keys
            and a list containing [number_of_apartments, yearly_balance]
        """

        current_year = self.starting_year

        while passive_income <= self.desired_passive_income:

            year_balance += self.yearly_savings

            if year_balance >= self.apartment_value:
                number_of_apartments_purchased = year_balance // self.apartment_value
                number_of_apartments += number_of_apartments_purchased
                passive_income = (
                    number_of_apartments * self.yearly_apartment_rent_income
                )

            year_balance += passive_income - (
                number_of_apartments_purchased * self.apartment_value
            )

            self.calculator_data.update({current_year: [number_of_apartments, year_balance]})

            current_year += 1

        return self.calculator_data

    def get_years_needed(self):
        """_summary_

        Returns:
            years_needed: Return the number of years needed to reach desired passive income
        """

        key = max(self.create_dictionary(), key=int)

        return key - self.starting_year + 1

    def get_apartments_needed(self):
        """_summary_

        Returns:
            years_needed: Return the number of years needed to reach desired passive income
        """
        key = max(self.create_dictionary(), key=int)

        return self.calculator_data[key][0]

    def get_networth(self):
        """_summary_

        Returns:
            years_needed: Return the number of years needed to reach desired passive income
        """
        net_worth = self.get_apartments_needed() * self.apartment_value

        return net_worth
