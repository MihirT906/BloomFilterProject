import bloomFilter2 as bloomFilter2
import pdfplumber
import re
import os
import time
import sys

class BloomSkillsExtractor:
    def __init__(self, file_path, pdf_path):
        self.file_path = file_path #file path containing the list of all possible skills to be loaded to the bloom filter
        self.skills = [] #list of extracted skills from the resume
        self.bloom_filter = self.init_bloom_filter() #Contains list of all skills used to extract from pdf
        self.skill_filter = bloomFilter2.BloomFilter(num_items=80, false_positive_rate=0.01) #Bloom filter containing list of extracted skills for duplicate checking
        self.pdf_path = pdf_path #File path for resume pdf
        
    
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

    
    def init_bloom_filter(self):
        '''
        Creates bloom filter with estimated size and inserts skills
        '''
        self.skills =self.get_list_of_skills()
        bloom_filter = bloomFilter2.BloomFilter(num_items=2*len(self.skills), false_positive_rate=0.001)
        for skill in self.skills:
            bloom_filter.insert(skill)
        return bloom_filter
        
        
    def extract_skills_from_resume(self):
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
    
        extracted_skills = []
        
        i = 0
        while i < len(words):
            matched_skill = False
            for j in range(len(self.skills), 0, -1):
                candidate = ' '.join(words[i:i + j])
                if self.bloom_filter.query(candidate):
                    if(not self.skill_filter.query(candidate)):
                        extracted_skills.append(candidate)
                        self.skill_filter.insert(candidate)
                    i += j
                    matched_skill = True
                    break

            if not matched_skill:
                i += 1
                
        not_found_skills = []
        with open(self.file_path, 'r') as file:
            skills = file.read().lower().split(', ')
        
        for skill in skills:
            if not self.skill_filter.query(skill):
                not_found_skills.append(skill)

        return extracted_skills, not_found_skills
    
    def pretty_print(self):
        print("Candidate has the following skills:")
        for i, string in enumerate(self.extract_skills_from_resume(), start=1):
            print(f"{i}. {string}")
        
    def get_analytics(self):
        start_time = time.time()
        es = self.extract_skills_from_resume()
        end_time = time.time()
        elapsed_time = end_time - start_time
        size_in_bits = self.bloom_filter.size + self.skill_filter.size + sys.getsizeof(es)*8
        print(f"Time taken for search operation: {elapsed_time:.6f} seconds")
        print(f"Space taken: {size_in_bits} bits")


        
        
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script_name.py skills.txt resume.pdf")
        sys.exit(1)

    skills_file_path = sys.argv[1]
    resume_pdf_path = sys.argv[2]

    se = BloomSkillsExtractor(skills_file_path, resume_pdf_path)
    se.pretty_print()
    se.get_analytics()