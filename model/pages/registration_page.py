from selene import browser, have, command
from model.data.resource import path
from model.data.user import User


class RegistrationPage:

    def open(self):
        browser.open("/automation-practice-form")
        browser.all("[id^=google_ads][id$=container__]").with_(timeout=10).wait_until(
            have.size_greater_than_or_equal(3)
        )
        browser.all("[id^=google_ads][id$=container__]").perform(command.js.remove)

    def _fill_first_name(self, value):
        browser.element("#firstName").send_keys(value)

    def _fill_last_name(self, value):
        browser.element("#lastName").send_keys(value)

    def _fill_email(self, value):
        browser.element("#userEmail").send_keys(value)

    def _select_gender(self, value=None):
        selectors = {
            "Male": '[for="gender-radio-1"]',
            "Female": '[for="gender-radio-2"]',
        }
        selector = selectors.get(value, '[for="gender-radio-3"]')
        browser.element(selector).click()

    def _fill_phone_number(self, value):
        browser.element("#userNumber").send_keys(value)

    def _fill_date_of_birth(self, year, month, day):
        browser.element("#dateOfBirthInput").click()
        browser.element(".react-datepicker__year-select").click().element(
            f'option[value="{year}"]'
        ).click()
        browser.element(".react-datepicker__month-select").click().element(
            f'option[value="{month}"]'
        ).click()
        browser.element(f".react-datepicker__day--0{day}").click()

    def _fill_subject(self, value):
        browser.element("#subjectsInput").send_keys(value).press_enter()

    def _upload_photo(self, value):
        browser.element("#uploadPicture").set_value(path(value))

    def _select_hobbies(self, *hobbies):
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

    def _fill_current_address(self, value):
        browser.element("#currentAddress").type(value)

    def _select_from_dropdown(self, element_id, value):
        browser.element(element_id).perform(command.js.scroll_into_view).click()
        browser.all("[id^=react-select][id*=option]").element_by(
            have.exact_text(value)
        ).click()

    def _select_state(self, value):
        self._select_from_dropdown("#state", value)

    def _select_city(self, value):
        self._select_from_dropdown("#city", value)

    def _submit_form(self):
        browser.element("#submit").press_enter()

    @staticmethod
    def _should_have_data_registered(data: dict):
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

    def register(self, user: User):
        self._fill_first_name(user.first_name)
        self._fill_last_name(user.last_name)
        self._fill_email(user.email)
        self._select_gender(user.gender)
        self._fill_phone_number(user.phone)
        self._fill_date_of_birth(
            user.date_of_birth.year,
            user.date_of_birth.month - 1,
            user.date_of_birth.day,
        )
        self._fill_subject(user.subject)
        self._upload_photo(user.picture)
        hobbies = [hobby.value for hobby in user.hobbies]
        self._select_hobbies(*hobbies)
        self._fill_current_address(user.address)
        self._select_state(user.state)
        self._select_city(user.city)
        self._submit_form()

    def should_have_registered(self, user: User):
        expected_data = {
            "Student Name": f"{user.first_name} {user.last_name}",
            "Student Email": user.email,
            "Gender": user.gender,
            "Mobile": user.phone,
            "Date of Birth": user.date_of_birth.strftime("%d %B,%Y"),
            "Subjects": user.subject,
            "Hobbies": [hobby.value for hobby in user.hobbies],
            "Picture": user.picture,
            "Address": user.address,
            "State and City": f"{user.state} {user.city}",
        }
        RegistrationPage._should_have_data_registered(expected_data)
