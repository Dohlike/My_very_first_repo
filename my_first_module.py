from todoist_api_python.api import TodoistAPI


projects = api.get_projects()
# print(projects)

putzplan = projects[1]
print(projects)



collaborators = api.get_collaborators(project_id="****")
print(collaborators)

person1 = collaborators[0]
print(person1)

person2 = collaborators[1]
print(person2)

****_id = ****.id
print(****_id)

sections = api.get_sections(project_id="****")
print(sections)



