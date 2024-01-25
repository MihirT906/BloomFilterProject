import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from BloomSkillsExtractor import BloomSkillsExtractor

class BloomSkillsExtractorGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Resume Skill Extractor")
        self.master.geometry("900x600")

        # Modify these files for the job you are trying to fill:
        self.concepts_file_path = "Skills/concepts.txt"
        self.frameworks_file_path = "Skills/frameworks.txt"
        self.languages_file_path = "Skills/languages.txt"

        self.label_resume = tk.Label(self.master, text="Upload Resume:")
        self.label_resume.pack()

        self.entry_resume = tk.Entry(self.master, width=50)
        self.entry_resume.pack()

        self.browse_resume_button = tk.Button(self.master, text="Browse", command=self.browse_resume_file)
        self.browse_resume_button.pack()

        self.extract_skills_button = tk.Button(self.master, text="Analyze", command=self.extract_skills)
        self.extract_skills_button.pack()

        self.notebook = ttk.Notebook(self.master)
        self.notebook.pack(fill='both', expand=True)

        self.concepts_frame = ttk.Frame(self.notebook)
        self.frameworks_frame = ttk.Frame(self.notebook)
        self.languages_frame = ttk.Frame(self.notebook)

        self.notebook.add(self.languages_frame, text='Languages')
        self.notebook.add(self.frameworks_frame, text='Frameworks')
        self.notebook.add(self.concepts_frame, text='Concepts')

        self.result_text_concepts = tk.Text(self.concepts_frame, height=5, width=80)
        self.result_text_concepts.pack(side='left', fill='both', expand=True)

        self.scrollbar_concepts = tk.Scrollbar(self.concepts_frame, command=self.result_text_concepts.yview)
        self.scrollbar_concepts.pack(side='right', fill='y')
        self.result_text_concepts.config(yscrollcommand=self.scrollbar_concepts.set)

        self.result_text_frameworks = tk.Text(self.frameworks_frame, height=5, width=80)
        self.result_text_frameworks.pack(side='left', fill='both', expand=True)

        self.scrollbar_frameworks = tk.Scrollbar(self.frameworks_frame, command=self.result_text_frameworks.yview)
        self.scrollbar_frameworks.pack(side='right', fill='y')
        self.result_text_frameworks.config(yscrollcommand=self.scrollbar_frameworks.set)

        self.result_text_languages = tk.Text(self.languages_frame, height=5, width=80)
        self.result_text_languages.pack(side='left', fill='both', expand=True)

        self.scrollbar_languages = tk.Scrollbar(self.languages_frame, command=self.result_text_languages.yview)
        self.scrollbar_languages.pack(side='right', fill='y')
        self.result_text_languages.config(yscrollcommand=self.scrollbar_languages.set)

    def browse_resume_file(self):
        initial_dir = "/Resumes"
        resume_pdf_path = filedialog.askopenfilename()
        if resume_pdf_path:
            self.entry_resume.delete(0, tk.END)
            self.entry_resume.insert(0, resume_pdf_path)

    def extract_skills(self):
        resume_pdf_path = self.entry_resume.get()

        if not resume_pdf_path:
            messagebox.showerror("Error", "Please upload a resume PDF.")
            return

        se_concepts = BloomSkillsExtractor(self.concepts_file_path, resume_pdf_path)
        se_frameworks = BloomSkillsExtractor(self.frameworks_file_path, resume_pdf_path)
        se_languages = BloomSkillsExtractor(self.languages_file_path, resume_pdf_path)

        found_concepts, not_found_concepts = se_concepts.extract_skills_from_resume()
        found_frameworks, not_found_frameworks = se_frameworks.extract_skills_from_resume()
        found_languages, not_found_languages = se_languages.extract_skills_from_resume()

        result_str_concepts = "Candidate knows the following concepts:\n"
        for i, skill in enumerate(found_concepts, start=1):
            result_str_concepts += f"\u2713 {skill}\n"
        for i, skill in enumerate(not_found_concepts, start=1):
            result_str_concepts += f"\u2717 {skill}\n"
        self.result_text_concepts.delete(1.0, tk.END)
        self.result_text_concepts.insert(tk.END, result_str_concepts)

        result_str_frameworks = "Candidate knows the following softwares/frameworks:\n"
        for i, skill in enumerate(found_frameworks, start=1):
            result_str_frameworks += f"\u2713 {skill}\n"
        for i, skill in enumerate(not_found_frameworks, start=1):
            result_str_frameworks += f"\u2717 {skill}\n"
        self.result_text_frameworks.delete(1.0, tk.END)
        self.result_text_frameworks.insert(tk.END, result_str_frameworks)

        result_str_languages = "Candidate knows the following languages:\n"
        for i, skill in enumerate(found_languages, start=1):
            result_str_languages += f"\u2713 {skill}\n"
        for i, skill in enumerate(not_found_languages, start=1):
            result_str_languages += f"\u2717 {skill}\n"
        self.result_text_languages.delete(1.0, tk.END)
        self.result_text_languages.insert(tk.END, result_str_languages)

if __name__ == "__main__":
    root = tk.Tk()
    app = BloomSkillsExtractorGUI(root)
    root.mainloop()
