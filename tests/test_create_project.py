import random
import string

from models.project import Project


def random_string(prefix, maxlen):
    symbols = string.ascii_letters.lower()
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def test_create_new_project(app):
    app.session.login("administrator", "root")
    project = Project(name=random_string("proj_", 10), status="development",
                      view_status="public", description=random_string("descr_", 10))
    app.project.create_new(project)
    app.project.open_project_list_page()
    app.project.verify_project_created(project)
    app.project.verify_project_created_by_soap(project)
    app.session.logout()
