"""
@author: ramon
@date: 11/02/2023
This class is going to calculate how many years will it take to generate passive for a given income from renting apts.
"""


class Calculator:
    """_summary_"""

    def __init__(
        self,
        desired_passive_income: float,
        yearly_savings: float,
        starting_year: float,
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

    def create_dictionary(
        self,
        year_balance=0,
        passive_income=0,
        number_of_apartments: int = 0,
    ):
        """_summary_

        Args:
            year_balance (int, optional): the year_balance of the account. Defaults to 0 as we start with nothing
            passive_income (int, optional): the passive_income of the year. Defaults to 0 as we start with nothing
            number_of_apartments (int, optional): the number of apartments at the end of the year. Defaults to 0 as we start with nothing

        Returns:
            self.calculator_data: A dictionary containg the current year as Keys
            and a list containing [number_of_apartments, yearly_balance]
        """

        current_year = self.starting_year
        number_of_apartments_purchased = 0

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

            to_append = {
                current_year: [
                    number_of_apartments,
                    year_balance,
                ]
            }
            self.calculator_data.update(to_append)

            current_year += 1

        return self.calculator_data, current_year - self.starting_year


data, years_needed = Calculator(150000, 70000, 2019, 80000, 6666).create_dictionary()
print(data, years_needed)
