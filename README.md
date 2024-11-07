# Swarthmore Athletic Training Tool
This project is meant as a prototype for a streamlined athletic training form. 
It aims to provide an easier way for student-athletes to report injuries, book appointments, 
and allow trainers to manage reports effectively. 

## Project Overview
Our tool serves two purposes:
1. **User Functionality:** Allow student-athletes to report and for trainers to manage with ease.
2. **Learning Resource:** Designed and well-documented for new open source developers, basic website 
design, and simple database management.

## Original Authors
- Eddie Paquette ( [eddiep12](https://github.com/eddiep12) )
- Zachary Potthoff ( [zpotthoff](https://github.com/zpotthoff) )
- Alex Rimerman ( [alex-rimerman](https://github.com/alex-rimerman) )

## Setup
Before starting, do the following:

1. Ensure `python` and `pip` are both installed and up to date.

2. Clone this repository.

3. Run `pip install -r requirements.txt` from the root of the repository.

## Troubleshooting
  - **pip command not found**
    - Cannot install required packages without `pip`
    - Resources:
      - [Solving pip Issues](https://flexiple.com/python/pip-command-not-found)

  - **ImportError: No module named flask**
    - Common error when installing requirements
    - Ensure `python` and `pip` are correctly placed on your path. It may be worthwhile 
    to set up a virtual environment to do this.
    - Some resources:
      - [Setting Up a Virtual Environment in VS Code](https://www.youtube.com/watch?app=desktop&v=GZbeL5AcTgw)
      - [General Guid to Python Virtual Environments](https://www.youtube.com/watch?v=KxvKCSwlUv8)

## Contributing
We are always welcome to new contributions from all experience levels. Feel free to submit issues, pull 
requests, or feel free to fork the project and add your own features, go for it.

## Warning
Do **NOT** use this code in production. Website and database management are not secure. 
This is a prototype for what training room software *could* look like, not a final 
product.

## Acknowledgements
This project was started as a final project for Professor Chris Murphy's 
[Open Source Software Development](https://www.cs.swarthmore.edu/~cmurphy/cs91r-f24.html) 
course at Swarthmore College. Many thanks to [Tim Ruscica](https://github.com/techwithtim)
for allowing us to use his code as a base structure to our project, specifically the login 
and database management features 
( [YouTube tutoial here](https://www.youtube.com/watch?app=desktop&v=dam0GPOAvVI) ).
