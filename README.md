# AI-Powered Automated Job Search Platform

### How to Run:
1. Add resume.pdf file in resources/input folder. 
2. Update application.properties with API Keys and required parameters
3. After application runs and if there are errors, it populates error's screenshot in resources/error. View the screenshot, 
  determine if the error is due to outside indeed search and delete png file if so and update output/job_list.txt with job status "AUTOMATION_NOT_SUPPORTED_OUTSIDE_INDEED". Otherwise fix the error in the code.

###Phase-1:
#### Job Search
1. Web scrape Indeed to get the specific job criteria
2. Read resume from input folder
3. Check output folder to see if that job has been applied before
4. Call Chatgpt api to see resume match
5. update output folder

#### Job Apply
1. Read output folder 
2. Write automation to automatically apply
3. Update job status 

###Phase-2:
- Integrate machine learning to answer question and interact with the page -> use custom model to for free version
- Integrate with docker 
- Introduce profile based search

Note:
- Indeed sample job url: https://www.indeed.com/viewjob/?jk=2468182232661cd8