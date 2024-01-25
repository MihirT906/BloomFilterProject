import tkinter as tk
from tkinter import filedialog
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

        # Instantiate the BloomSkillsExtractor object
        se = BloomSkillsExtractor(skills_file_path, resume_pdf_path)

        # Capture the results in a formatted string
        result_str = "Extracted Skills:\n"
        extracted_skills = se.extract_skills_from_resume()

        if extracted_skills:
            for i, skill in enumerate(extracted_skills, start=1):
                result_str += f"{i}. {skill}\n"
        else:
            result_str += "No skills found in the resume.\n"

        # Display results in the Text widget
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, result_str)

if __name__ == "__main__":
    root = tk.Tk()
    app = BloomSkillsExtractorGUI(root)
    root.mainloop()
