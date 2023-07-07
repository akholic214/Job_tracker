# Job Application Tracker

This is a simple job application tracker application built using Python and the Tkinter library. It provides a user-friendly interface for managing job applications, including adding, updating, deleting, and highlighting job entries. The application allows you to track various details of each job application, such as the job title, company, applied date, interview date, assessment stage, and outcome.

## Features

- Add a new job application by entering the job title, company, applied date, interview date, assessment stage, and outcome.
- Use the "Use Today's Date" checkbox to automatically fill in the applied date field with the current date.
- Choose the applied date and interview date using a calendar pop-up.
- Select the assessment stage from a predefined list of options.
- If the assessment stage is set to "Interview Stage," you can choose the outcome as either "Good" or "Bad."
- View and manage all job applications in a treeview widget, including sorting by columns.
- Highlight a selected job application for better visibility.
- Update and delete existing job applications.
- Save the job application data to a file for persistent storage.

## Installation

1. Clone the repository: `git clone https://github.com/your-username/job-application-tracker.git`
2. Navigate to the project directory: `cd job-application-tracker`
3. Install the required dependencies: `pip install -r requirements.txt`
4. Run the application: `python main.py`

## Usage

1. Launch the application by running the `main.py` script.
2. Fill in the job details in the input fields, including the job title, company, applied date, interview date, assessment stage, and outcome.
3. Use the "Use Today's Date" checkbox to automatically fill in the applied date field with the current date.
4. Choose the applied date and interview date by clicking the "Choose Date" button and selecting a date from the calendar pop-up.
5. Select the assessment stage by clicking the corresponding button.
6. If the assessment stage is set to "Interview Stage," choose the outcome as either "Good" or "Bad."
7. Click the "Add Job" button to add the job application to the tracker.
8. View the list of job applications in the treeview widget.
9. Select a job application to populate the input fields for editing or deletion.
10. Click the "Update Job" button to save any changes made to a job application.
11. Click the "Delete Job" button to remove a job application from the tracker.
12. Use the "Highlight Job" button to highlight a selected job application in the treeview for better visibility.
13. Click the "Save" button to persistently store the job application data to a file.
14. Close the application when finished.

## Contributing

Contributions are welcome! If you have any suggestions, bug fixes, or feature implementations, please submit a pull request. Before contributing, please make sure to read the [contributing guidelines](CONTRIBUTING.md).

## License

This project is licensed under the [MIT License](LICENSE). Feel free to modify and distribute this code for personal or commercial use.

## Acknowledgements

- The application was developed using the Tkinter library for Python.
- The treeview widget styling is enhanced using the ThemedStyle module from the ttkthemes library.
- The tkcalendar library is used to provide a calendar pop-up for date selection.
- This project was inspired by the need for a simple and intuitive job application tracker.

## Contact

For any questions or inquiries, please contact [paulmunteanu2010@gmail.com]

Thank you for using the Job Application Tracker! We hope it helps you in managing your job search effectively.
