API-PHYTHON

BACKGROUND CONTEXT

Old-school system administrators usually only know Bash and that is what they use to build their scripts. While Bash is perfectly fine for a lot of things, it can quickly get messy and not efficient compared to other programming languages. The new generation of system administrators, usually called SREs, are pretty much regular software engineers but instead of building products, they are managing systems. And one of the big differences with their predecessors is that they know more than just Bash scripting.

One popular way to expose an application and dataset is to use an API. Often, they are the public facing part of websites and micro-services so that allow outsiders to interact with them – access and modify their data. In this project, you will access employee data via an API to organize and export them to different data structures.

This is a perfect example of a task that is not suited for Bash scripting, so let’s build Python scripts.
Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

GENERAL

What is an API
What is a REST API
What are microservices
What is the CSV format
What is the JSON format
Pythonic Package and module name style
Pythonic Class name style
Pythonic Variable name style
Pythonic Function name style
Pythonic Constant name style
Significance of CapWords or CamelCase in Python

REQUIREMENTS

Recommended editors: Visual studio code
All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3)
All your files should end with a new line
Libraries imported in your Python files must be organized in alphabetical order
A README.md file, at the root of the folder of the project, is mandatory
Your code should use the PEP 8 style
The length of your files will be tested using wc
All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
You must use get to access to dictionary value by key (it won’t throw an exception if the key doesn’t exist in the dictionary)
Your code should not be executed when imported (by using if __name__ == "__main__":)

TASKS
0-gather_data_from_an_API.py

Python script that, using this REST API, for a given employee ID, returns information about his/her TODO list progress

1-export_to_CSV.py

Python script to export data in the CSV format, extending from 0-gather_data_from_an_API.py

2-export_to_JSON.py

Python script to export data in the JSON format, extending from 0-gather_data_from_an_API.py

3-dictionary_of_list_of_dictionaries.py

Python script to export data in the JSON format, extending from 0-gather_data_from_an_API.py and 2-export_to_JSON.pyPython script to export data in the JSON format, extending from 0-gather_data_from_an_API.py and 2-export_to_JSON.py
