# PathPilot- A Career Guide
A data-driven web application that uses python and tktinter to predict personalized career based on the questionare related to personality, intersts, and goals
##  Overview of the Project

**PATHPILOT** addresses the critical challenge faced by students and recent graduates who struggle to choose careers due to inability to navigate the vast sea of career options. They often lack a single, detailed, credible source for personalized,tailored guidance that aligns with their skills, intesets, goals, educational preferences and financial background with real world career paths.

In order to address this, this application: 
1. administers a **15-question quiz** that is intended to profile the user's aptitude, personality, interests, and limitations.
2. By comparing the user's responses to an extensive, in-memory database of 50 career profiles (representing more than 250 career options), a **Fit Score** is determined.
3. Presenting a list of the top five tailored career suggestions.


***

##  Key Features

The Start Page, Quiz Page, and Results Page are the three main functional modules that make up the application's structure.

50 thorough career entries from the major streams (Science-A/PCM, Science-B/PCB, Commerce, and Arts/Humanities) are included in this extensive career database.
* Personalised Profiling Quiz: This 15-question multiple-choice test covers important aspects such as aptitude, interests, personality, objectives, and financial limitations.
* Fit Score Algorithm: Custom logic that produces a measurable percentage score that shows how well a user fits into each career path.
* View of Detailed Recommendations ("Flash Card"): The application shows a thorough information sheet for every suggested career, which includes:
Education and Stream Requirements, Cost, and Difficulty Level
India's Top 10+ Colleges
10+ Entry-Level Positions
Appropriate Trainee/Internship Positions
* Interactive GUI: A graphical user interface created with the standard Python tkinter library.
***

##  Technologies & Tools Used

| Tool/Library | Purpose |
| :--- | :--- |
| **Python 3.x** | Core programming language |
| **Tkinter** | Standard Python library for creating the Graphical User Interface (GUI)  |
| **`tkinter.ttk`** | Used for modern, themed widgets |
| **`collections.defaultdict`** | Used for efficient data structures in the scoring logic |

***

## How to Install and Start the Project

 A standard Python 3 installation is needed for this project.

 ### 1.  Requirements

 Make sure your system has **Python 3** installed.

 ### 2.  Setting up

 1.   Make a clone of the repository:
 ```bash
 [Your-GitHub-Repo-URL] git clone
 CD pathpilot-a-career-guide
 ```

 2.   Since the project makes use of built-in modules (`tkinter`, `sys`, `os`, `random`), no external libraries beyond the standard Python distribution are strictly necessary.

 ### 3.  Executing the Program

 Run the primary Python file straight from the terminal:
```bash
 "srihitha's final project better version.py" in Python
```
## Instructions for  for Testing
1. Open the application:  Use the Python command to launch the application.
2. Click "START CAREER QUIZ" to begin the test.
3. Finish 15 Questions: Respond to all 15 multiple-choice questions pertaining to goals, aptitude, and interest.
4. Click "FINISH QUIZ & GET RESULTS" to view the results.
5. Verify Suggestions: Verify that a list of the top five professions, each with a determined Fit Score, is shown.
6. Verify Details: To access the comprehensive Career Flash Card view and confirm the college, employment, and educational information, double-click any career recommendation.
7. Test Navigation: Verify that the quiz's return and restart buttons work properly.
