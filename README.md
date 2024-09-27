# Openspace Organizer

## 🏢 Description

Your company moved to a new office at the Gent Zuiderport. Its an openspace with some number of tables some number of seats on each table. As many of you are new colleagues, you come up with the idea of changing seats everyday and get to know each other better by working side by side with your new colleagues. 

This script runs everyday to re-assign everybody to a new seat. 

## 📦 Repo structure

```
.
├── src/
│   ├── openspace.py
│   ├── table.py
│   └── utils.py
├── .gitignore
├── main.py
├── new_colleagues.csv
├── output.csv
└── README.md

## 🛎️ Usage

1. Clone the repository to your local machine.

2 .To run the script, you can execute the `main.py` file from your command line:

    ```
    python main.py
    ```

3. The script then prompts you to enter the number of tables and seats in your open space. Then, it reads the input file "new_colleagues.csv", and organizes your colleagues to random seat assignments. The resulting seating plan is displayed in your console and also saved to an "output.csv" file in your root directory. 

```python

input_filepath = "new_colleagues.csv"
output_filename = "output.csv"

# Creates a list that contains all the colleagues names
names = file_utils.read_names_from_csv(input_filepath)

#Take the number of seats and tables as an input from the user
number_of_tables=int(input("Please enter number of tables: "))
number_ofseats=int(input("Please enter number of seats in each table: "))

# create an OpenSpace() 
open_space = OpenSpace(number_of_tables,number_ofseats)

# assign a colleague randomly to a table
open_space.organize(names)

# save the seat assigments to a new file
open_space.store(output_filename)

# display assignments in the terminal
open_space.display()

```

## ⏱️ Timeline

This project took two days for completion.

## 📌 Personal Situation
This project was done as part of the AI Boocamp at BeCode.org. 

Connect with me on [LinkedIn](https://www.linkedin.com/in/rasmita-damaraju-33b577126/).