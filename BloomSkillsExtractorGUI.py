import tkinter as tk
from tkinter import filedialog, messagebox
from BloomSkillsExtractor import BloomSkillsExtractor

class BloomSkillsExtractorGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Resume Skill Extractor")

        self.label_skills = tk.Label(self.master, text="Select Skills File:")
        self.label_skills.pack()

        self.entry_skills = tk.Entry(self.master, width=50)
        self.entry_skills.pack()

        self.browse_skills_button = tk.Button(self.master, text="Browse", command=self.browse_skills_file)
        self.browse_skills_button.pack()

        self.label_resume = tk.Label(self.master, text="Select Resume PDF:")
        self.label_resume.pack()

        self.entry_resume = tk.Entry(self.master, width=50)
        self.entry_resume.pack()

        self.browse_resume_button = tk.Button(self.master, text="Browse", command=self.browse_resume_file)
        self.browse_resume_button.pack()

        self.extract_skills_button = tk.Button(self.master, text="Extract Skills", command=self.extract_skills)
        self.extract_skills_button.pack()

        # Create a Text widget for displaying results
        self.result_text = tk.Text(self.master, height=10, width=80)
        self.result_text.pack()

    def browse_skills_file(self):
        skills_file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if skills_file_path:
            self.entry_skills.delete(0, tk.END)
            self.entry_skills.insert(0, skills_file_path)

    def browse_resume_file(self):
        resume_pdf_path = filedialog.askopenfilename()
        if resume_pdf_path:
            self.entry_resume.delete(0, tk.END)
            self.entry_resume.insert(0, resume_pdf_path)

    def extract_skills(self):
        skills_file_path = self.entry_skills.get()
        resume_pdf_path = self.entry_resume.get()

        # Check if both documents are uploaded
        if not skills_file_path or not resume_pdf_path:
            messagebox.showerror("Error", "Please upload both skills file and resume PDF.")
            return
        # Instantiate the BloomSkillsExtractor object
        # Instantiate the BloomSkillsExtractor object
        se = BloomSkillsExtractor(skills_file_path, resume_pdf_path)

        # Call extract_skills_from_resume to get found and not found skills
        found_skills, not_found_skills = se.extract_skills_from_resume()
        
        # Display results in the Text widget
        result_str = "Skills from the Skills File:\n"

        # Display found skills with a check mark
        for i, skill in enumerate(found_skills, start=1):
            result_str += f"\u2713 {skill}\n"

        # Display not found skills with a cross mark
        for i, skill in enumerate(not_found_skills, start=1):
            result_str += f"\u2717 {skill}\n"

        # Update the Text widget
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, result_str)

if __name__ == "__main__":
    root = tk.Tk()
    app = BloomSkillsExtractorGUI(root)
    root.mainloop()
