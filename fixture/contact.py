from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import re


from model.contact import Contact


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def return_to_add_new(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "add new").click()

    def create_new(self, contact):
        wd = self.app.wd
        self.open_add_contact_page()
        self.fill_contact_form(contact)
        # Submit contact creation
        wd.find_element(By.XPATH, "//div[@id='content']/form/input[21]").click()
        self.return_to_add_new()
        self.contact_cache = None

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
        self.change_contact_date("aday", contact.aday)
        self.change_contact_date("amonth", contact.amonth)
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
        if not (wd.current_url.endswith("/edit.php") and len(wd.find_elements(By.NAME, "submit")) > 0):
            wd.find_element(By.LINK_TEXT, "add new").click()

    def open_contact_list(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook") and len(wd.find_elements(By.NAME, "add")) > 0):
            wd.find_element(By.LINK_TEXT, "home").click()

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_contact_list()
        wd.find_elements(By.NAME, "selected[]")[index].click()
        wd.find_element(By.XPATH, "//input[@value='Delete']").click()
        # submit deletion
        wd.switch_to.alert.accept()
        WebDriverWait(wd, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.msgbox")))
        self.contact_cache = None

    def edit_first_contact(self):
        self.edit_contact_by_index(0)

    def edit_contact_by_index(self, index, edit_contact):
        wd = self.app.wd
        self.open_contact_list()
        wd.find_elements(By.XPATH, "//img[@alt='Edit']")[index].click()
        # fill new contact data
        self.fill_contact_form(edit_contact)
        # submit edition
        wd.find_element(By.NAME, "update").click()
        self.contact_cache = None

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.open_contact_list()
        wd.find_elements(By.XPATH, "//img[@alt='Edit']")[index].click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.open_contact_list()
        wd.find_elements(By.XPATH, "//img[@alt='Details']")[index].click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element(By.NAME, "firstname").get_attribute("value")
        lasttname = wd.find_element(By.NAME, "lastname").get_attribute("value")
        id = wd.find_element(By.NAME, "id").get_attribute("value")
        homephone = wd.find_element(By.NAME, "home").get_attribute("value")
        workphone = wd.find_element(By.NAME, "work").get_attribute("value")
        mobilephone = wd.find_element(By.NAME, "mobile").get_attribute("value")
        secondaryphone = wd.find_element(By.NAME, "phone2").get_attribute("value")
        return Contact(firstname=firstname, lastname=lasttname, id=id,
                       homephone=homephone, mobilephone=mobilephone, workphone=workphone,
                       secondaryphone=secondaryphone)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element(By.ID, "content").text
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)
        return Contact(homephone=homephone, mobilephone=mobilephone, workphone=workphone,
                       secondaryphone=secondaryphone)




    def is_list_empty(self):
        wd = self.app.wd
        self.open_contact_list()
        return wd.find_element(By.ID, "search_count").text == "0"

    def count(self):
        wd = self.app.wd
        self.open_contact_list()
        return len(wd.find_elements(By.NAME, "selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_contact_list()
            self.contact_cache = []
            for element in wd.find_elements(By.CSS_SELECTOR, "[name=entry]"):
                cells = element.find_elements(By.TAG_NAME, "td")
                lastname = element.find_element(By.XPATH, "./td[2]").text
                firstname = element.find_element(By.XPATH, "./td[3]").text
                id = element.find_element(By.NAME, "selected[]").get_attribute("value")
                all_phones = cells[5].text.splitlines()
                self.contact_cache.append(Contact(lastname=lastname, firstname=firstname, id=id,
                                                  homephone=all_phones[0], mobilephone=all_phones[1],
                                          workphone=all_phones[2], secondaryphone=all_phones[3]))
        return list(self.contact_cache)
