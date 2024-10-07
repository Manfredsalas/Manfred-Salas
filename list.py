#Homogeneus List

integers = [1, 2, 3, 8, 33]

animals = ['dog', 'cat', 'goat']

names = ['roger', 'Quebec', 'Manfred']

floats = [2.2, 4.5, 9.8, 10.8]

#Heterogeneus List 

numbers_animals_names = [2, 'cat', 34.33,'roger']


list_list = [[1,2,3], ['cat', 'dos', 'spider']]

#Hoe to access an elemnt in a list 

list = [3, 22, 30, 5.3, 20]

print(list[2])

print(list[0])

print(list[1])

print(list[4])

word = ["Code", "Loop", "Bug", "Debug", "Execute",
    "Variable", "Function", "Module", "Import", "Package",
    "Library", "Syntax", "Class", "Object", "Inheritance",
    "Data", "JSON", "String", "Integer", "Float",
    "Boolean", "List", "Tuple", "Dictionary", "Set",
    "Exception", "API", "Argument", "Parameter", "Return",
    "Scope", "Closure", "Comprehension", "Lambda", "Decorator",
    "Iteration", "Recursion", "Runtime", "Environment", "Dependency",
    "Framework", "Script", "Compiler", "Interpreter", "IDE",
    "Virtualenv", "Pip", "Anaconda", "Jupyter", "Variable",
    "Static", "Dynamic", "Execution", "Test", "Mock",
    "Assertion", "Library", "DataFrame", "Series", "Plot",
    "Chart", "Visualization", "Histogram", "Scatter", "Line",
    "Axis", "Label", "Legend", "Annotation", "Parameter",
    "Training", "Testing", "Validation", "Model", "Algorithm",
    "Feature", "Label", "Classifier", "Clustering", "Regression",
    "Hyperparameter", "Optimization", "Cross-validation", "Pipeline", "Epoch",
    "Batch", "Loss", "Gradient", "Descent", "Activation",
    "Neural", "Network", "Tokenization", "Embedding", "NLP",
    "Web scraping", "Automation", "Scripting", "Deployment", "Environment",
    "Repository", "Version", "Control", "Git", "GitHub",
    "Branch", "Merge", "Commit", "Push", "Pull",
    "Clone", "Diff", "Status", "Conflict", "Release",
    "Build", "Continuous", "Integration", "Delivery", "Deployment",
    "Cloud", "AWS", "Azure", "Google Cloud", "Virtualization",
    "Containerization", "Docker", "Kubernetes", "Microservices", "REST",
    "GraphQL", "Middleware", "Caching", "Load", "Balancer",
    "Security", "Encryption", "Authentication", "Authorization", "Token",
    "Session", "Cookie", "API key", "Rate limiting", "Throttling",
    "Performance", "Scalability", "Reliability", "Monitoring", "Logging",
    "Debugger", "Profiler", "Test case", "Mocking", "Assertion",
    "Coverage", "Documentation", "Markdown", "Tutorial", "Guide",
    "Community", "Forum", "Contribution", "Open-source", "License",
    "Convention", "Best practices", "Pattern", "Architecture", "Design",
    "Strategy", "Workflow", "Process", "Solution", "Debugging",
    "Exception handling", "Concurrency", "Thread", "Async", "Await",
    "Decorator", "Context", "Manager", "Yield", "Generator",
    "Multiprocessing", "ArgumentParser", "Command-line", "CLI", "Pathlib",
    "OS", "Sys", "Time", "Random", "Math",
    "Built-in", "Custom", "Staticmethod", "Classmethod", "Dataclass",
    "F-string", "Format", "Join", "Split", "Strip",
    "Find", "Replace", "Count", "Slice", "Reverse",
    "Zip", "Map", "Filter", "Reduce", "Any",
    "All", "Enumerate", "Sorted", "Reversed", "Set comprehension",
    "Dictionary comprehension", "List comprehension", "Type hinting", "Docstring", "PEP"]

print(word[-1])

#list slicing

list = [3, 22, 30, 5.3, 20]

print(list[:])

print(list[1 : 3])

print(list[2:-1])

#update a list

science = ['art', 'chemistry', 'math']

science[0] = 'Biology'

print(science)

science[2] = 'Geology'
print(science)

integers = [2,5,9,20,27]

integers.remove(5)
print(integers)

integers.pop()
print()

list_frut = ['sandia', 'manzana', 'melon']

#pop, remove, del

del list_frut[0]
print(list_frut)

list_name = ['roger', 'dania', 'anahi']
list_name.append('manfred')
print(list_name)

#python list

list_of_squares = []
for int in range (1,10):
    suquare= int**2
    list_of_squares.append(suquare)
print(list_of_squares)

#[expression for int in list if condition]

square2 = [int**2 for int in range(1,10) ]

print(square2)


Numbers = [1,2,3,4,5,6,7,8,9]
for number in Numbers:
    print(number**3)

cubic = [num**3 for num in Numbers]
print(cubic)

iven_numbers = [num*2 for num in Numbers]
print(iven_numbers)