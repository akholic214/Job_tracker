import tkinter as tk
from tkinter import ttk, messagebox, Menu
import pickle
import datetime
from ttkthemes import ThemedStyle
from tkcalendar import Calendar


# Load data if it exists
try:
    with open('job_data.pkl', 'rb') as f:
        job_data = pickle.load(f)
except FileNotFoundError:
    job_data = []

def validate_date(date_text):
    try:
        if date_text != '':  # Allow for date fields to be empty
            datetime.datetime.strptime(date_text, '%d-%m-%Y')
        return True
    except ValueError:
        return False

def use_todays_date():
    if not date_entry.get():
        today = datetime.date.today().strftime('%d-%m-%Y')
        date_entry.delete(0, 'end')
        date_entry.insert(0, today)

def add_job():
    job_title = title_entry.get()
    company = company_entry.get()
    applied_date = date_entry.get()
    interview_date = interview_date_entry.get()
    assessment_stage = stage_var.get()
    outcome = outcome_var.get() if stage_var.get() == "Interview Stage" else ""

    if job_title and company:
        # Append the data to job_data
        job_data.append((job_title, company, applied_date, interview_date, assessment_stage, outcome))

        # Refresh the tree view
        refresh_tree()
        clear_input_fields()  # Clear input fields
        messagebox.showinfo("Success", "Job application added!")
    else:
        messagebox.showerror("Incomplete Information", "Please enter job title and company.")

def delete_job():
    try:
        selected_item = tree.selection()[0]  # get selected item
        tree.delete(selected_item)
        del job_data[tree.index(selected_item)]  # delete the data from the list
        refresh_tree()
        clear_input_fields()  # Clear input fields
    except IndexError:
        messagebox.showerror("Selection Error", "Please select an item to delete.")

def update_job():
    try:
        selected_id = tree.focus()  # get selected item
        selected_item = tree.item(selected_id)['values']

        updated_item = list(selected_item)
        updated_item[0] = title_entry.get()
        updated_item[1] = company_entry.get()
        updated_item[2] = date_entry.get()
        updated_item[3] = interview_date_entry.get()
        updated_item[4] = stage_var.get()
        updated_item[5] = outcome_var.get() if stage_var.get() == "Interview Stage" else ""

        if all(updated_item[:2]):
            job_data[tree.index(selected_id)] = tuple(updated_item)
            refresh_tree()
            clear_input_fields()  # Clear input fields
            messagebox.showinfo("Success", "Job application updated!")
        else:
            messagebox.showerror("Incomplete Information", "Please enter job title and company.")
    except IndexError:
        messagebox.showerror("Selection Error", "Please select an item to update.")

def refresh_tree():
    # Clear the tree view
    tree.delete(*tree.get_children())

    # Reload job_data
    for job_data_tuple in job_data:
        tree.insert("", 'end', values=job_data_tuple)

def save_data():
    with open('job_data.pkl', 'wb') as f:
        pickle.dump(job_data, f)
    messagebox.showinfo("Data saved", "Your job data has been saved.")

def choose_date(entry):
    def set_date():
        selected_date = cal.selection_get().strftime('%d-%m-%Y')
        entry.delete(0, 'end')
        entry.insert(0, selected_date)
        top.destroy()

    top = tk.Toplevel(root)
    cal = Calendar(top, selectmode='day')
    cal.pack(pady=10, padx=10)
    ok_button = ttk.Button(top, text="OK", command=set_date)
    ok_button.pack(pady=5)

def highlight_job():
    selected_item = tree.focus()  # get selected item

    # Remove previous highlighting
    for item in tree.get_children():
        tree.item(item, tags='normal')

    # Apply highlighting to the selected item
    tree.item(selected_item, tags='highlight')

    # Scroll to the selected item
    tree.see(selected_item)

    # Configure tag for highlighting
    tree.tag_configure('highlight', font=('Arial', 12, 'bold'))

def on_tree_select(event):
    selected_item = tree.focus()  # get selected item
    selected_values = tree.item(selected_item, "values")
    if selected_values:
        title_entry.delete(0, 'end')
        title_entry.insert(0, selected_values[0])

        company_entry.delete(0, 'end')
        company_entry.insert(0, selected_values[1])

        date_entry.delete(0, 'end')
        date_entry.insert(0, selected_values[2])

        interview_date_entry.delete(0, 'end')
        interview_date_entry.insert(0, selected_values[3])

        stage_var.set(selected_values[4])

        outcome_var.set(selected_values[5])

def clear_input_fields():
    title_entry.delete(0, 'end')
    company_entry.delete(0, 'end')
    date_entry.delete(0, 'end')
    interview_date_entry.delete(0, 'end')
    stage_var.set("")
    outcome_var.set("")

# Create a window
root = tk.Tk()
root.title("Job Application Tracker")
style = ThemedStyle(root)
style.theme_use("clam")

# Configure style for buttons
style.configure("Toolbutton.TButton", font=("Arial", 14), borderwidth=2, focuscolor=style.lookup("TEntry", "fieldbackground"))
style.map("Toolbutton.TButton", foreground=[('pressed', 'black'), ('active', 'black')])

# Create frame for input fields
input_frame = ttk.Frame(root)
input_frame.pack(padx=10, pady=10)

# Create text boxes and labels
title_label = ttk.Label(input_frame, text="Job Title:", font=("Arial", 14))
title_label.grid(row=0, column=0, padx=5, pady=5, sticky='e')
title_entry = ttk.Entry(input_frame, width=30, font=("Arial", 14))
title_entry.grid(row=0, column=1, padx=5, pady=5)

company_label = ttk.Label(input_frame, text="Company:", font=("Arial", 14))
company_label.grid(row=1, column=0, padx=5, pady=5, sticky='e')
company_entry = ttk.Entry(input_frame, width=30, font=("Arial", 14))
company_entry.grid(row=1, column=1, padx=5, pady=5)

# Create "Use Today's Date" checkbox for applied date
use_today_var = tk.IntVar()
use_today_checkbox = ttk.Checkbutton(input_frame, text="Use Today's Date", variable=use_today_var, command=use_todays_date, style="Toolbutton.TCheckbutton")
use_today_checkbox.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky='w')

# Create date entry and button for applied date
date_label = ttk.Label(input_frame, text="Applied Date (DD-MM-YYYY):", font=("Arial", 14))
date_label.grid(row=3, column=0, padx=5, pady=5, sticky='e')
date_entry = ttk.Entry(input_frame, width=12, font=("Arial", 14))
date_entry.grid(row=3, column=1, padx=5, pady=5)
date_button = ttk.Button(input_frame, text="Choose Date", command=lambda: choose_date(date_entry), style="Toolbutton.TButton")
date_button.grid(row=3, column=2, padx=5, pady=5)

# Create date entry and button for interview date
interview_date_label = ttk.Label(input_frame, text="Interview Date (DD-MM-YYYY):", font=("Arial", 14))
interview_date_label.grid(row=4, column=0, padx=5, pady=5, sticky='e')
interview_date_entry = ttk.Entry(input_frame, width=12, font=("Arial", 14))
interview_date_entry.grid(row=4, column=1, padx=5, pady=5)
interview_date_button = ttk.Button(input_frame, text="Choose Date", command=lambda: choose_date(interview_date_entry), style="Toolbutton.TButton")
interview_date_button.grid(row=4, column=2, padx=5, pady=5)

# Create frame for stage and outcome selection
selection_frame = ttk.Frame(root)
selection_frame.pack(padx=10, pady=10)

stage_label = ttk.Label(selection_frame, text="Assessment Stage:", font=("Arial", 14))
stage_label.grid(row=0, column=0, padx=5, pady=5, sticky='e')

stage_var = tk.StringVar()
stage_var.set("")  # Set initial value

assessment_stages = ["Application Sent", "Application Approved", "Application Rejected", "Interview Stage", "Onboarding"]
stage_buttons = []
for i, stage in enumerate(assessment_stages):
    button = ttk.Button(selection_frame, text=stage, command=lambda stage=stage: stage_var.set(stage), style="Toolbutton.TButton")
    button.grid(row=0, column=i+1, padx=5, pady=5)
    stage_buttons.append(button)

outcome_label = ttk.Label(selection_frame, text="Outcome:", font=("Arial", 14))
outcome_label.grid(row=1, column=0, padx=5, pady=5, sticky='e')

outcome_var = tk.StringVar()
outcome_good_radio = ttk.Radiobutton(selection_frame, text="Good", variable=outcome_var, value="Good", style="Toolbutton.TRadiobutton")
outcome_good_radio.grid(row=1, column=1, padx=5, pady=5)

outcome_bad_radio = ttk.Radiobutton(selection_frame, text="Bad", variable=outcome_var, value="Bad", style="Toolbutton.TRadiobutton")
outcome_bad_radio.grid(row=1, column=2, padx=5, pady=5)

# Function to enable/disable outcome selection based on assessment stage
def toggle_outcome_selection(*args):
    if stage_var.get() == "Interview Stage":
        outcome_good_radio.configure(state="enabled")
        outcome_bad_radio.configure(state="enabled")
    else:
        outcome_good_radio.configure(state="disabled")
        outcome_bad_radio.configure(state="disabled")

# Add a trace to stage_var to call the toggle_outcome_selection function
stage_var.trace_add("write", toggle_outcome_selection)

# Create buttons frame
button_frame = ttk.Frame(root)
button_frame.pack(side="top", padx=10, pady=10)

# Create a style for the highlight button
style.configure("HighlightButton.TButton", font=("Arial", 14, "bold"), borderwidth=2, focuscolor=style.lookup("TEntry", "fieldbackground"))
style.map("HighlightButton.TButton", foreground=[('pressed', 'black'), ('active', 'black')])

add_button = ttk.Button(button_frame, text="Add Job", command=add_job, style="Toolbutton.TButton")
add_button.pack(side="left", padx=5, pady=5)

delete_button = ttk.Button(button_frame, text="Delete Job", command=delete_job, style="Toolbutton.TButton")
delete_button.pack(side="left", padx=5, pady=5)

update_button = ttk.Button(button_frame, text="Update Job", command=update_job, style="Toolbutton.TButton")
update_button.pack(side="left", padx=5, pady=5)

save_button = ttk.Button(button_frame, text="Save", command=save_data, style="Toolbutton.TButton")
save_button.pack(side="left", padx=5, pady=5)

highlight_button = ttk.Button(button_frame, text="Highlight Job", command=highlight_job, style="HighlightButton.TButton")
highlight_button.pack(side="left", padx=5, pady=5)

# Create treeview
tree = ttk.Treeview(root, columns=("Job Title", "Company", "Applied Date", "Interview Date", "Assessment Stage", "Outcome"), show="headings")
tree.pack(padx=10, pady=10)

tree.heading("Job Title", text="Job Title", anchor=tk.CENTER)
tree.heading("Company", text="Company", anchor=tk.CENTER)
tree.heading("Applied Date", text="Applied Date", anchor=tk.CENTER)
tree.heading("Interview Date", text="Interview Date", anchor=tk.CENTER)
tree.heading("Assessment Stage", text="Assessment Stage", anchor=tk.CENTER)
tree.heading("Outcome", text="Outcome", anchor=tk.CENTER)

# Apply styling to the treeview
style.configure("Treeview.Heading", font=('Arial', 14, 'bold'))
style.configure("Treeview", font=('Arial', 12))

# Bind the treeview selection event to on_tree_select function ...
tree.bind("<<TreeviewSelect>>", on_tree_select)

root.mainloop()




