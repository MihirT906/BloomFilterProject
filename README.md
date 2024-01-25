

### Resume Skill Extractor using Bloom Filters
A Bloom filter is a space-efficient probabilistic data structure designed to test whether a given element is a member of a set. 
I implemented an automated skill detection program using bloom filters. This system utilizes a Bloom filter initialized with a curated list of common technical skills prevalent in the IT industry. I incorporated the murmur3 hash algorithm in the bloom filter. By feeding PDF resumes through this filter, the program accurately extracts skills, streamlining the skill identification process.
I successfully demonstrated the efficiency gains achieved by employing the Bloom filter in terms of both space and time. 

### Results
Without using bloom filter: </br>
```
 python SkillsExtractor.py skills.txt Resumes/Resume-Sample-2.pdf
```
 
<img width="510" alt="Screenshot 2024-01-17 at 6 42 12 PM" src="https://github.com/MihirT906/BloomFilterProject/assets/56927051/a124b757-eccd-4199-b614-2d3a73ad08b8">

With Bloom Filter: </br>
```
python BloomSkillsExtractor.py skills.txt Resumes/Resume-Sample-2.pdf      
```
<img width="500" alt="Screenshot 2024-01-17 at 6 40 29 PM" src="https://github.com/MihirT906/BloomFilterProject/assets/56927051/4c009e44-0bc3-4004-84d2-98967697f9d4">

The implementation with bloom filter saves considerable amount of space.


### Phase 2:
Created an intuitive graphical user interface (GUI) tailored for job recruiters, providing a platform for efficient resume analysis based on specific skillsets. The user-friendly interface enables recruiters to swiftly assess resumes, facilitating a seamless and targeted skill matching process.
A job recruiter can customize the desired skillset for the position they are looking for in /Skills folder. The application allows recruiters to effortlessly upload resumes, facilitating a comprehensive analysis of candidate skillsets. 
Try it out with Jake's resume. 
![2A186825-AABD-44DD-BD9B-CE38FCC12BC4](https://github.com/MihirT906/BloomFilterProject/assets/56927051/2dd53534-ad86-4ea2-966b-93184e7763bf)
![7BFE4BD3-49C2-4185-8478-574CEDADF443](https://github.com/MihirT906/BloomFilterProject/assets/56927051/7a562fd4-bc73-4e73-bbdf-405d203c05c1)
![BC9C4CF2-4822-4E11-A34A-A234B698098C](https://github.com/MihirT906/BloomFilterProject/assets/56927051/8592bd18-f91e-49aa-83ee-5282e1245dae)




