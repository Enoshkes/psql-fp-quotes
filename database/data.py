# data.py

# Quotes dictionary
quotes = [
    {"id": 1, "quote": "The purpose of abstraction is not to be vague, but to create a new semantic level in which one can be absolutely precise.", "developer_id": 1},
    {"id": 2, "quote": "The key to understanding recursion is to begin by understanding recursion.", "developer_id": 2},
    {"id": 3, "quote": "Lisp isn't a language, it's a building material.", "developer_id": 3},
    {"id": 4, "quote": "The most disastrous thing that you can ever learn is your first programming language.", "developer_id": 4},
    {"id": 5, "quote": "The programmer's primary weapon in the never-ending battle against slow system is to change the intramodular structure.", "developer_id": 5},
    {"id": 6, "quote": "Programming is an art form that fights back.", "developer_id": 6},
    {"id": 7, "quote": "Sometimes it pays to stay in bed on Monday, rather than spending the rest of the week debugging Monday's code.", "developer_id": 7},
    {"id": 8, "quote": "The best way to predict the future is to implement it.", "developer_id": 8},
    {"id": 9, "quote": "The Internet? We are not interested in it.", "developer_id": 9},
    {"id": 10, "quote": "Talk is cheap. Show me the code.", "developer_id": 10},
    {"id": 11, "quote": "The computer was born to solve problems that did not exist before.", "developer_id": 11},
    {"id": 12, "quote": "The question of whether computers can think is like the question of whether submarines can swim.", "developer_id": 12},
    {"id": 13, "quote": "The only way to learn a new programming language is by writing programs in it.", "developer_id": 13},
    {"id": 14, "quote": "Any fool can write code that a computer can understand. Good programmers write code that humans can understand.", "developer_id": 14},
    {"id": 15, "quote": "First, solve the problem. Then, write the code.", "developer_id": 15},
    {"id": 16, "quote": "It's not a bug – it's an undocumented feature.", "developer_id": 16},
    {"id": 17, "quote": "Software is like entropy: It is difficult to grasp, weighs nothing, and obeys the Second Law of Thermodynamics; i.e., it always increases.", "developer_id": 17},
    {"id": 18, "quote": "Measuring programming progress by lines of code is like measuring aircraft building progress by weight.", "developer_id": 9},
    {"id": 19, "quote": "Walking on water and developing software from a specification are easy if both are frozen.", "developer_id": 18},
    {"id": 20, "quote": "Always code as if the guy who ends up maintaining your code will be a violent psychopath who knows where you live.", "developer_id": 14}
]

# Developers dictionary
developers = [
    {"id": 1, "fullname": "Edsger W. Dijkstra", "language": "Algol", "active_years": "1960-2002"},
    {"id": 2, "fullname": "John McCarthy", "language": "Lisp", "active_years": "1958-2011"},
    {"id": 3, "fullname": "Alan Kay", "language": "Smalltalk", "active_years": "1970-present"},
    {"id": 4, "fullname": "Alan Perlis", "language": "ALGOL", "active_years": "1958-1989"},
    {"id": 5, "fullname": "Frederick P. Brooks Jr.", "language": "OS/360", "active_years": "1956-present"},
    {"id": 6, "fullname": "Larry Wall", "language": "Perl", "active_years": "1987-present"},
    {"id": 7, "fullname": "Dan Ingalls", "language": "Smalltalk", "active_years": "1972-present"},
    {"id": 8, "fullname": "David Heinemeier Hansson", "language": "Ruby", "active_years": "2003-present"},
    {"id": 9, "fullname": "Bill Gates", "language": "BASIC", "active_years": "1975-present"},
    {"id": 10, "fullname": "Linus Torvalds", "language": "C", "active_years": "1991-present"},
    {"id": 11, "fullname": "Bill Joy", "language": "BSD Unix", "active_years": "1975-2003"},
    {"id": 12, "fullname": "Edsger W. Dijkstra", "language": "Algol", "active_years": "1960-2002"},
    {"id": 13, "fullname": "Dennis Ritchie", "language": "C", "active_years": "1967-2011"},
    {"id": 14, "fullname": "Martin Fowler", "language": "UML", "active_years": "1990-present"},
    {"id": 15, "fullname": "John Carmack", "language": "C++", "active_years": "1991-present"},
    {"id": 16, "fullname": "Ada Lovelace", "language": "Analytical Engine", "active_years": "1842-1852"},
    {"id": 17, "fullname": "Norman Ramsey", "language": "Haskell", "active_years": "1990-present"},
    {"id": 18, "fullname": "Edward V. Berard", "language": "Object-Oriented Design", "active_years": "1985-present"},
    {"id": 19, "fullname": "Grace Hopper", "language": "COBOL", "active_years": "1944-1986"},
    {"id": 20, "fullname": "Yukihiro Matsumoto", "language": "Ruby", "active_years": "1993-present"}
]

# Companies dictionary
companies = [
    {"id": 1, "name": "Eindhoven University of Technology", "product": "Computer Science Research"},
    {"id": 2, "name": "MIT", "product": "Artificial Intelligence"},
    {"id": 3, "name": "Xerox PARC", "product": "Object-Oriented Programming"},
    {"id": 4, "name": "Carnegie Mellon University", "product": "Computer Science Education"},
    {"id": 5, "name": "IBM", "product": "Operating Systems"},
    {"id": 6, "name": "Bell Labs", "product": "Unix"},
    {"id": 7, "name": "Microsoft", "product": "Windows"},
    {"id": 8, "name": "Apple", "product": "macOS"},
    {"id": 9, "name": "Google", "product": "Search Engine"},
    {"id": 10, "name": "Facebook", "product": "Social Network"},
    {"id": 11, "name": "Amazon", "product": "E-commerce Platform"},
    {"id": 12, "name": "Oracle", "product": "Database Management Systems"},
    {"id": 13, "name": "Sun Microsystems", "product": "Java"},
    {"id": 14, "name": "Red Hat", "product": "Linux Distribution"},
    {"id": 15, "name": "VMware", "product": "Virtualization Software"},
    {"id": 16, "name": "Nvidia", "product": "Graphics Processing Units"},
    {"id": 17, "name": "Tesla", "product": "Electric Vehicles"},
    {"id": 18, "name": "SpaceX", "product": "Spacecraft"},
    {"id": 19, "name": "Palantir", "product": "Big Data Analytics"},
    {"id": 20, "name": "OpenAI", "product": "Artificial General Intelligence"}
]

# Many-to-many relationship between developers and companies
developers_companies = [
    {"developer_id": 1, "company_id": 1},
    {"developer_id": 2, "company_id": 2},
    {"developer_id": 3, "company_id": 3},
    {"developer_id": 4, "company_id": 4},
    {"developer_id": 5, "company_id": 5},
    {"developer_id": 2, "company_id": 4},
    {"developer_id": 3, "company_id": 2},
    {"developer_id": 6, "company_id": 6},
    {"developer_id": 7, "company_id": 3},
    {"developer_id": 8, "company_id": 11},
    {"developer_id": 9, "company_id": 7},
    {"developer_id": 10, "company_id": 14},
    {"developer_id": 11, "company_id": 13},
    {"developer_id": 12, "company_id": 1},
    {"developer_id": 13, "company_id": 6},
    {"developer_id": 14, "company_id": 12},
    {"developer_id": 15, "company_id": 16},
    {"developer_id": 16, "company_id": 1},
    {"developer_id": 17, "company_id": 4},
    {"developer_id": 18, "company_id": 9},
    {"developer_id": 19, "company_id": 5},
    {"developer_id": 20, "company_id": 8},
    {"developer_id": 10, "company_id": 9},
    {"developer_id": 11, "company_id": 8},
    {"developer_id": 13, "company_id": 5},
    {"developer_id": 15, "company_id": 18},
    {"developer_id": 8, "company_id": 10},
    {"developer_id": 14, "company_id": 15},
    {"developer_id": 19, "company_id": 2},
    {"developer_id": 20, "company_id": 13}
]