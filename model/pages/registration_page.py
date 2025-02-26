from selene import browser, have, command
from model.resource import path


class RegistrationPage:

    def open(self):
        browser.open("/automation-practice-form")
        browser.all("[id^=google_ads][id$=container__]").with_(timeout=10).wait_until(
            have.size_greater_than_or_equal(3)
        )
        browser.all("[id^=google_ads][id$=container__]").perform(command.js.remove)

    def fill_first_name(self, value):
        browser.element("#firstName").send_keys(value)

    def fill_last_name(self, value):
        browser.element("#lastName").send_keys(value)

    def fill_email(self, value):
        browser.element("#userEmail").send_keys(value)

    def select_gender(self, value=None):
        selectors = {
            "Male": '[for="gender-radio-1"]',
            "Female": '[for="gender-radio-2"]',
        }
        selector = selectors.get(value, '[for="gender-radio-3"]')
        browser.element(selector).click()

    def fill_phone_number(self, value):
        browser.element("#userNumber").send_keys(value)

    def fill_date_of_birth(self, year, month, day):
        browser.element("#dateOfBirthInput").click()
        browser.element(".react-datepicker__year-select").click().element(
            f'option[value="{year}"]'
        ).click()
        browser.element(".react-datepicker__month-select").click().element(
            f'option[value="{month}"]'
        ).click()
        browser.element(f".react-datepicker__day--0{day}").click()

    def fill_subject(self, value):
        browser.element("#subjectsInput").send_keys(value).press_enter()

    def upload_photo(self, value):
        browser.element("#uploadPicture").set_value(path(value))

    def select_hobbies(self, *hobbies):
        available_hobbies = ["Sports", "Reading", "Music"]
        if not hobbies or "all" in hobbies:
            for hobby in available_hobbies:
                browser.all(".custom-control-label").element_by(
                    have.text(hobby)
                ).click()
        else:
            for hobby in hobbies:
                browser.all(".custom-control-label").element_by(
                    have.text(hobby)
                ).click()

    def fill_current_address(self, value_input):
        browser.element("#currentAddress").type(value_input)

    def select_from_dropdown(self, element_id, value):
        browser.element(element_id).perform(command.js.scroll_into_view).click()
        browser.all("[id^=react-select][id*=option]").element_by(
            have.exact_text(value)
        ).click()

    def select_state(self, value):
        self.select_from_dropdown("#state", value)

    def select_city(self, value):
        self.select_from_dropdown("#city", value)

    def submit_form(self):
        browser.element("#submit").press_enter()

    @staticmethod
    def should_have_data_registered(data: dict):
        expected_values = [
            data["Student Name"],
            data["Student Email"],
            data["Gender"],
            data["Mobile"],
            data["Date of Birth"],
            data["Subjects"],
            ", ".join(data["Hobbies"]),
            data["Picture"],
            data["Address"],
            data["State and City"],
        ]

        browser.element(".table").all("td").even.should(
            have.exact_texts(*expected_values)
        )
