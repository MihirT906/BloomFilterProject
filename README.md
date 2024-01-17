

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
