from graphviz import Digraph

# Создаем новый граф
dot = Digraph()

# Добавляем сущности
dot.node('Book', 'Book\n- BookID (PK)\n- Title\n- Authors\n- Publisher\n- Year\n- Genre\n- TotalCopies\n- AvailableCopies')
dot.node('Reader', 'Reader\n- ReaderID (PK)\n- Name\n- DateOfBirth\n- Address\n- PhoneNumber\n- RegistrationDate')
dot.node('BookIssue', 'BookIssue\n- IssueID (PK)\n- BookID (FK)\n- ReaderID (FK)\n- IssueDate\n- DueDate')
dot.node('BookReturn', 'BookReturn\n- ReturnID (PK)\n- IssueID (FK)\n- ReturnDate\n- Fine')
dot.node('Employee', 'Employee\n- EmployeeID (PK)\n- Name\n- Position\n- PhoneNumber\n- Email')

# Добавляем связи
dot.edge('Book', 'BookIssue', label='1 to M')
dot.edge('Reader', 'BookIssue', label='1 to M')
dot.edge('BookIssue', 'BookReturn', label='1 to 1')

# Визуализируем граф
dot.render('library_er_diagram', format='png', view=True)
