from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def return_to_add_new(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "add new").click()

    def create_new(self, contact):
        wd = self.app.wd
        self.fill_contact_form(contact)
        # Submit contact creation
        wd.find_element(By.XPATH, "//div[@id='content']/form/input[21]").click()
        self.return_to_add_new()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_contact_field("firstname", contact.firstname)
        self.change_contact_field("middlename", contact.middlename)
        self.change_contact_field("lastname", contact.lastname)
        self.change_contact_field("nickname", contact.nickname)
        self.change_contact_field("title", contact.title)
        self.change_contact_field("company", contact.company)
        self.change_contact_field("address", contact.address)
        self.change_contact_field("home", contact.phone1)
        self.change_contact_field("mobile", contact.mobilephone)
        self.change_contact_field("work", contact.workphone)
        self.change_contact_field("fax", contact.fax)
        self.change_contact_field("email", contact.email1)
        self.change_contact_field("email2", contact.email2)
        self.change_contact_field("email3", contact.email3)
        self.change_contact_field("homepage", contact.site)
        self.change_contact_date("bday", contact.bday)
        self.change_contact_date("bmonth", contact.bmonth)
        self.change_contact_field("byear", contact.byear)
        self.change_contact_date("aday", contact.bday)
        self.change_contact_date("amonth", contact.bmonth)
        self.change_contact_field("ayear", contact.ayear)
        self.change_contact_field("address2", contact.address2)
        self.change_contact_field("phone2", contact.phone2)
        self.change_contact_field("notes", contact.notes)

    def change_contact_field(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element(By.NAME, field_name).click()
            wd.find_element(By.NAME, field_name).clear()
            wd.find_element(By.NAME, field_name).send_keys(text)

    def change_contact_date(self, field_date, date):
        wd = self.app.wd
        if date is not None:
            wd.find_element(By.NAME, field_date).click()
            Select(wd.find_element(By.NAME, field_date)).select_by_visible_text(date)

    def open_add_contact_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "add new").click()

    def open_contact_list(self):
        wd = self.app.wd
        # Open contact list (home)
        wd.find_element(By.LINK_TEXT, "home").click()

    def delete_first_contact(self):
        wd = self.app.wd
        self.open_contact_list()
        self.open_edit_page()
        # submit deletion
        wd.find_element(By.XPATH, "//div[@id='content']/form[2]/input[2]").click()

    def open_edit_page(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, "//img[@alt='Edit']").click()

    def edit_first_contact(self, edit_contact):
        wd = self.app.wd
        self.open_contact_list()
        self.open_edit_page()
        # fill new contact data
        self.fill_contact_form(edit_contact)
        # submit edition
        wd.find_element(By.XPATH, "//div[@id='content']/form/input[22]").click()
