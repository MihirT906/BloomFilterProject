import pdfplumber
import re
import os
import time
import sys

class SkillsExtractor:
    def __init__(self, file_path, pdf_path):
        self.file_path = file_path
        self.pdf_path = pdf_path
        self.skills =self.get_list_of_skills()
    
    def get_list_of_skills(self):
        '''
        Returns the list of all possible skills from the file skills.txt. This is converted to lower case for consistency and returned as a list
        '''
        try:
            with open(self.file_path, 'r') as file:
                skills = file.read().lower().split(', ')
            return skills
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {self.file_path}")

    def extract_words_from_resume(self):
        '''
        Extracts all words from resume
        Converts to lower case
        Matches skills (of length more than 1)
        '''
        if not os.path.exists(self.pdf_path):
            raise FileNotFoundError(f"PDF file not found: {self.pdf_path}")

        with pdfplumber.open(self.pdf_path) as pdf:
            text = ""
            for page in pdf.pages:
                text += page.extract_text()
            
        text_lower = text.lower()
        words = text_lower.split()
        words = [re.sub(r'\W+', '', word) for word in words]
        return words
    
    def extract_skills(self):
        words = self.extract_words_from_resume()
        extracted_skills = set()
        
        i = 0
        while i < len(words):
            matched_skill = False
            for j in range(len(self.skills), 0, -1):
                candidate = ' '.join(words[i:i + j])
                if candidate in self.skills:
                    extracted_skills.add(candidate)
                    i += j
                    matched_skill = True
                    break

            if not matched_skill:
                i += 1

        return extracted_skills

    def pretty_print(self):
        print("Candidate has the following skills:")
        for i, string in enumerate(self.extract_skills(), start=1):
            print(f"{i}. {string}")
    
    def get_analytics(self):
        start_time = time.time()
        es = self.extract_skills()
        end_time = time.time()
        elapsed_time = end_time - start_time
        size_in_bits = sys.getsizeof(self.skills)*8 + sys.getsizeof(es)*8
        print(f"Time taken for search operation: {elapsed_time:.6f} seconds")
        print(f"Space taken: {size_in_bits} bits")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script_name.py skills.txt resume.pdf")
        sys.exit(1)

    skills_file_path = sys.argv[1]
    resume_pdf_path = sys.argv[2]

    se = SkillsExtractor(skills_file_path, resume_pdf_path)
    se.pretty_print()
    se.get_analytics()