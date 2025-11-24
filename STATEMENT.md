#  Problem Statement 
Students and recent graduates often struggle to find career paths that truly fit their educational background, personal interests, skills, and financial constraints. They frequently rely on generic or incomplete online information that fails to provide tailored guidance.

This leads to two major challenges: Lack of Personalised Fit: There is no single, reliable platform that correlates a user's aptitude, personality, and constraints (like cost and difficulty) with a structured list of compatible, real-world career options and their required academic paths, which can lead to missed opportunities and the risk of selecting an inappropriate career path, which can hinder long-term growth.
# The project's scope
 PATHPILOT is a client-side, data-driven desktop application developed with Tkinter and Python.

 * Functionality: It only concentrates on creating user profiles and offering tailored career advice.  A customised scoring algorithm, a comprehensive career information view, and a multi-factor quiz are all included.

 * Data Set: 50 comprehensive career profiles from the main academic streams (Science-A/PCM, Science-B/PCB, Commerce, Arts/Humanities) are contained in a pre-defined, in-memory database (CAREER_DB).

 * System Environment: Python 3.x and the integrated Tkinter GUI library are supported by the standard desktop operating system on which the application is intended to run locally.

 * Exclusions: Because it uses in-memory data structures, it excludes cloud storage, user accounts and authentication, real-time data retrieval, and a sophisticated database management system.
 # Target Users
 The following are PATHPILOT's main target users:

 * High school students (ages 15 to 18): Those who are choosing their first undergraduate degree, academic stream, and college entrance exams.

 * Recent College Graduates (Ages 20–24): People looking for their first job or thinking about changing careers who require clarification on next steps, job roles, and necessary upskilling.

 * Parents and career counsellors: People who need a methodical, evidence-based tool to help students make decisions.
# High Level Features
The system follows a three-stage workflow:

* Personalized Profiling Quiz: It administers a 15-question quiz to capture the user's profile, including their aptitude, interests, personality, and financial/goal constraints.

* Fit Score Algorithm: A custom-developed algorithm processes the quiz responses against the 50 career profiles to generate a quantifiable, percentage-based Fit Score for compatibility.

* Detailed Recommendations: The application displays the Top 5 most compatible careers and provides in-depth Career Flash Cards. These cards offer crucial information such as required education, estimated cost, difficulty level, lists of top colleges, and specific entry-level job roles.
