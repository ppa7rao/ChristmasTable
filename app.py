import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.button import Button
import sqlite3
import re


def valid_name(name):

    '''Ensures that the Name:
- is between 5 and 50 characters long,
- is uniquely alphabetic,
- contains no spaces,
- has the first letter in uppercase,
- has no more than 2 consecutive duplicates.'''

    name = name.strip()
    return (
        5 <= len(name) <= 50 and
        name.isalpha() and
        not name.isspace() and
        name[0].isupper() and
        not consecutive_duplicates(name)
        )


def consecutive_duplicates(duplicate):

    '''This function makes sure there is no more
    than 2 duplicate cosecutive letters in Name'''

    return bool(re.search(r'(.)\1{3,}', duplicate))


class MyApp(GridLayout):
    def __init__(self, **kwargs):
        super(MyApp, self).__init__()
        self.cols = 2
        self.spacing = [15, 15]

        self.add_widget(Label(text='Name'))
        self.st_name = TextInput(multiline=False,
                                 on_text_validate=self.validate_name)
        self.add_widget(self.st_name)

        self.add_widget(Label(text='Surname'))
        self.st_surname = TextInput(multiline=False,
                                    on_text_validate=self.validate_name)
        self.add_widget(self.st_surname)

        self.add_widget(Label(text='Gender'))
        self.st_gender = Spinner(text='Select',
                                 values=('Female', 'Male'))
        self.add_widget(self.st_gender)

        self.add_widget(Label(text='Age'))
        self.st_age = TextInput(multiline=False,
                                input_type='number',
                                on_text_validate=self.validate_numeric)
        self.add_widget(self.st_age)

        self.add_widget(Label(text='Country'))
        self.st_country = TextInput(multiline=False)
        self.add_widget(self.st_country)

        self.add_widget(Label(text='Intensions'))
        self.st_intensions = TextInput(multiline=False)
        self.add_widget(self.st_intensions)

        self.add_widget(Label(text='How many Gifts do you bring'))
        self.st_gifts = TextInput(multiline=False,
                                  input_type='number',
                                  on_text_validate=self.validate_numeric)
        self.add_widget(self.st_gifts)

        self.add_widget(Label(text='Did you behave this year?'))
        self.st_behave = Spinner(text='Select',
                                 values=('Off Course!', 'Maybe Not...'))
        self.add_widget(self.st_behave)

        self.press = Button(text='Save')
        self.press.bind(on_press=self.save)
        self.add_widget(self.press)

    def validate_name(self, input_name):
        if not valid_name(input_name.text):
            self.st_name.text = ''
            self.st_surname.text = ''
            print('Invalid Entry!\nPlease enter a valid one!')

    def validate_numeric(self, input_number):
        try:
            number = int(input_number)
            if number < 0:
                print('You can not input a negative number!')
                return False
            return True
        except ValueError:
            self.st_age.text = ''
            self.st_gifts.text = ''
            print('Invalid entry!\nPlease enter an integer value!')
            return False

    def save(self, instance):
        # Person Name is Valid
        self.validate_name(self.st_name)
        person_name = self.st_name.text.strip()

        # Person Surname is Valid
        self.validate_name(self.st_surname)
        person_surname = self.st_surname.text.strip()

        # Name and Surname are not equal
        if person_name.lower() == person_surname.lower():
            print('Name and Surname must be different!')
            return

        # Age and Gits are integers
        age_is_numeric = self.validate_numeric(self.st_age.text)
        gifts_is_numeric = self.validate_numeric(self.st_gifts.text)

        # Gender and Behaviour Buttons were used
        if self.st_gender.text == 'Select':
            print('Please enter your Gender!')
            return
        if self.st_behave.text == 'Select':
            print('Please enter if you behave this year!')
            return

        # Checking if the nº of gifts is enough
        if gifts_is_numeric and int(self.st_gifts.text) < 5:
            print("Is that all the magic you've got in your sleigh?\nLooks like someone might be on the 'Naughty List' for a gift shortage!")  # noqa E401
            return

        if valid_name(person_name) and valid_name(person_surname) and age_is_numeric and gifts_is_numeric:  # noqa E401
            print('Name ', self.st_name.text)
            print('Surname ', self.st_surname.text)
            print('Gender ', self.st_gender.text)
            print('Age ', self.st_age.text)
            print('Country ', self.st_country.text)
            print('Intensions ', self.st_intensions.text)
            print('Number of Gifts ', self.st_gifts.text)
            print('Good Behaviour ', self.st_behave.text)

            if self.st_behave.text == 'No':
                print("Looks like Santa has detected some questionable behavior on his radar!\nYour case is under review.\nHang tight and reconsider those life choices!")  # noqa E401
            else:
                print('Congratulations!\nYour seat at the Christmas Table is secured!\nGet ready to jingle all the way!!')  # noqa E401


class ParentApp(App):
    def build(self):
        return MyApp()


if __name__ == '__main__':
    ParentApp().run()
