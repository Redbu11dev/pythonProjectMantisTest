from __future__ import annotations

import time
from typing import TYPE_CHECKING

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select

if TYPE_CHECKING:
    from fixture.application import Application
    from models.project import Project


class ProjectHelper:
    def __init__(self, app: Application):
        self.app = app

    def open_creation_page(self):
        wd = self.app.wd
        wd.get(self.app.base_url + "/manage_proj_create_page.php")

    def open_project_list_page(self):
        wd = self.app.wd
        wd.get(self.app.base_url + "/manage_proj_page.php")

    def verify_project_created(self, project: Project):
        driver = self.app.wd
        assert driver.find_element_by_link_text(project.name) is not None

    def open_project_edit(self, project: Project):
        driver = self.app.wd
        driver.find_element_by_link_text(project.name).click()

    def delete_project(self, project: Project):
        driver = self.app.wd
        self.open_project_edit(project)
        driver.find_element_by_xpath("//input[@value='Delete Project']").click()
        time.sleep(3)
        driver.find_element_by_xpath("//input[@value='Delete Project']").click()

    def verify_project_deleted(self, project: Project):
        driver = self.app.wd
        element_found = False
        try:
            driver.find_element_by_link_text(project.name)
            element_found = True
        except NoSuchElementException as e:
            element_found = False
        if element_found:
            raise AssertionError("project was not deleted")

    def create_new(self, project: Project):
        driver = self.app.wd
        self.open_creation_page()
        driver.find_element_by_name("name").click()
        driver.find_element_by_name("name").clear()
        driver.find_element_by_name("name").send_keys(project.name)
        driver.find_element_by_name("status").click()
        Select(driver.find_element_by_name("status")).select_by_visible_text(project.status)
        driver.find_element_by_name("status").click()
        driver.find_element_by_name("view_state").click()
        Select(driver.find_element_by_name("view_state")).select_by_visible_text(project.view_status)
        driver.find_element_by_name("view_state").click()
        driver.find_element_by_name("description").click()
        driver.find_element_by_name("description").clear()
        driver.find_element_by_name("description").send_keys(project.description)
        driver.find_element_by_xpath("//input[@value='Add Project']").click()

