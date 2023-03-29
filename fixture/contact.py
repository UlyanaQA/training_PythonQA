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
        self.change_contact_field("home", contact.homephone)
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
        self.change_contact_field("phone2", contact.secondaryphone)
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

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element(By.CSS_SELECTOR, "input[value='%s']" % id).click()

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.open_contact_list()
        wd.find_element(By.ID, id).click()
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

    def open_contact_to_edit_by_id(self, id):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element(By.CSS_SELECTOR, 'a[href="edit.php?id=%s"]' % id).click()

    def edit_contact_by_id(self, id, new_contact_data):
        wd = self.app.wd
        self.open_contact_to_edit_by_id(id)
        # fill new contact data
        self.fill_contact_form(new_contact_data)
        # submit edition
        wd.find_element(By.NAME, "update").click()
        self.app.open_home_page()
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
        id = wd.find_element(By.NAME, "id").get_attribute("value")
        firstname = wd.find_element(By.NAME, "firstname").get_attribute("value")
        lasttname = wd.find_element(By.NAME, "lastname").get_attribute("value")
        middlename = wd.find_element(By.NAME, "middlename").get_attribute("value")
        address = wd.find_element(By.NAME, "address").get_attribute("value")
        homephone = wd.find_element(By.NAME, "home").get_attribute("value")
        workphone = wd.find_element(By.NAME, "work").get_attribute("value")
        mobilephone = wd.find_element(By.NAME, "mobile").get_attribute("value")
        secondaryphone = wd.find_element(By.NAME, "phone2").get_attribute("value")
        email1 = wd.find_element(By.NAME, "email").get_attribute("value")
        email2 = wd.find_element(By.NAME, "email2").get_attribute("value")
        email3 = wd.find_element(By.NAME, "email3").get_attribute("value")

        return Contact(id=id, firstname=firstname, middlename=middlename, lastname=lasttname,
                       address=address, homephone=homephone, mobilephone=mobilephone, workphone=workphone,
                       secondaryphone=secondaryphone, email1=email1, email2=email2, email3=email3)

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
                id = element.find_element(By.NAME, "selected[]").get_attribute("value")
                cells = element.find_elements(By.TAG_NAME, "td")
                lastname = element.find_element(By.XPATH, "./td[2]").text
                firstname = element.find_element(By.XPATH, "./td[3]").text
                address = element.find_element(By.XPATH, "./td[4]").text
                all_emails = cells[4].text
                all_phones = cells[5].text
                self.contact_cache.append(Contact(id=id, lastname=lastname, firstname=firstname,
                                                  address=address, all_emails_from_home_page=all_emails,
                                                  all_phones_from_home_page=all_phones))
        return list(self.contact_cache)

    def add_contact_to_group(self, contact, group):
        wd = self.app.wd
        self.open_contact_list()
        self.select_contact_by_id(contact.id)
        wd.find_element(By.NAME, "to_group").\
            find_element(By.CSS_SELECTOR, "option[value='%s']" % group.id).click()
        wd.find_element(By.NAME, "add").click()
        self.open_contact_list()

    def delete_contact_from_group(self, contact, group):
        wd = self.app.wd
        self.open_contact_list()
        wd.find_element(By.NAME, "group").find_element(By.CSS_SELECTOR, "option[value='%s']" % group.id).click()
        self.select_contact_by_id(contact.id)
        wd.find_element(By.NAME, "remove").click()
        self.open_contact_list()
