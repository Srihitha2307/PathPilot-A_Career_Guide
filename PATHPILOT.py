import tkinter as tk
from tkinter import ttk, messagebox
from collections import defaultdict
import random
import sys
import os 
from functools import partial

# ==========================================================
# CRITICAL FIX: Add local_packages folder to system path
# ==========================================================
try:
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'local_packages'))
except Exception:
    pass 
# ==========================================================

# ==========================================================
# In-Memory Database for 250+ Careers (Representative Sample)
# 50 Total Entries Now (10 Original + 40 New)
# ==========================================================
CAREER_DB = [
    # ------------------- SCIENCE-A GROUP (PCM) - Engineering -------------------
    {
        "topic": "Software Engineer",
        "stream": "Science-A/PCM",
        "aptitude": "Maths, Logic, Tech",
        "personality": "Problem-Solver, Introvert",
        "interest": "Coding, Gadgets",
        "education": "B.Tech/BE (CS/IT)",
        "cost": "Medium-High",
        "difficulty": "Hard",
        "description": "Develops, designs, and maintains software systems and applications. Requires strong programming and analytical skills.",
        "fees": "₹4 Lakh - ₹20 Lakh (Total Course)",
        "colleges": [
            "Indian Institute of Technology (IIT) Bombay", "IIT Delhi", "BITS Pilani", "Vellore Institute of Technology (VIT)",
            "National Institute of Technology (NIT) Trichy", "Delhi Technological University (DTU)", "Jadavpur University",
            "Indian Institute of Information Technology (IIIT) Hyderabad", "Anna University", "College of Engineering, Pune (COEP)"
        ],
        "jobs": [
            "Frontend Developer", "Backend Developer", "Full-Stack Developer", "Cloud Engineer", "DevOps Specialist",
            "Data Scientist", "Machine Learning Engineer", "Cyber Security Analyst", "Embedded Systems Engineer",
            "Game Developer", 
            "Solutions Architect", 
            "Product Manager (Technical)" 
        ],
        "internships": [
            {"role": "Software Dev Intern", "company": "Google", "duration": "6 months"},
            {"role": "Data Analyst Intern", "company": "Microsoft", "duration": "3 months"},
            {"role": "Web Dev Trainee", "company": "TCS", "duration": "6 months"}
        ]
    },
    {
        "topic": "Civil Engineer",
        "stream": "Science-A/PCM",
        "aptitude": "Physics, Maths, Design",
        "personality": "Practical, Detail-Oriented",
        "interest": "Construction, Infrastructure",
        "education": "B.Tech/BE (Civil)",
        "cost": "Medium",
        "difficulty": "Medium",
        "description": "Plans, designs, and oversees the construction and maintenance of building structures and public works, such as roads, dams, and bridges.",
        "fees": "₹3 Lakh - ₹15 Lakh (Total Course)",
        "colleges": [
            "IIT Madras", "IIT Kanpur", "NIT Warangal", "Birla Institute of Technology, Mesra", "Jamia Millia Islamia",
            "Indian Institute of Engineering Science and Technology, Shibpur", "Osmania University", "Anna University",
            "Sardar Vallabhbhai National Institute of Technology", "College of Engineering, Pune (COEP)"
        ],
        "jobs": [
            "Structural Engineer", "Transportation Engineer", "Geotechnical Engineer", "Construction Manager", 
            "Water Resource Engineer", "Urban Planner", "Site Engineer", "Project Manager", "Consultant", "Quantity Surveyor",
            "Site Supervisor", 
            "Environmental Engineer" 
        ],
        "internships": [
            {"role": "Site Trainee", "company": "L&T Construction", "duration": "4 months"},
            {"role": "Design Intern", "company": "AECOM", "duration": "6 months"},
            {"role": "Project Intern", "company": "GMR Infrastructure", "duration": "3 months"}
        ]
    },
    
    # ------------------- SCIENCE-B GROUP (PCB) - Medical & Allied -------------------
    {
        "topic": "Doctor (MBBS)",
        "stream": "Science-B/PCB",
        "aptitude": "Biology, Memory, Empathy",
        "personality": "Caring, Resilient",
        "interest": "Healthcare, Human Body",
        "education": "MBBS",
        "cost": "High",
        "difficulty": "Very Hard",
        "description": "Diagnoses, treats, and prevents illness, injury, and other physical and mental impairments in humans. Requires qualifying the NEET exam.",
        "fees": "₹50 Lakh - ₹1.5 Crore (Total Course, Private)",
        "colleges": [
            "All India Institute of Medical Sciences (AIIMS), New Delhi", "Maulana Azad Medical College (MAMC)", "JIPMER Puducherry",
            "King George's Medical University (KGMU)", "Grant Medical College, Mumbai", "Banaras Hindu University (BHU)",
            "Armed Forces Medical College (AFMC), Pune", "Christian Medical College (CMC), Vellore", 
            "Seth GS Medical College, Mumbai", "Stanley Medical College, Chennai"
        ],
        "jobs": [
            "General Practitioner", "Cardiologist", "Neurologist", "Pediatrician", "Surgeon (General/Specialized)",
            "Oncologist", "Dermatologist", "Radiologist", "Anesthesiologist", "Emergency Physician",
            "Public Health Officer", 
            "Hospital Administrator" 
        ],
        "internships": [
            {"role": "Clinical Internship", "company": "Govt. Hospital A", "duration": "1 year (Mandatory)"},
            {"role": "Elective Rotation", "company": "International Clinic B", "duration": "1 month"},
            {"role": "Research Assistant", "company": "Medical University Lab", "duration": "3 months"}
        ]
    },
    {
        "topic": "Pharmacist",
        "stream": "Science-B/PCB",
        "aptitude": "Chemistry, Detail-Oriented",
        "personality": "Methodical, Responsible",
        "interest": "Pharmaceuticals, Research",
        "education": "B.Pharm",
        "cost": "Medium",
        "difficulty": "Medium",
        "description": "Specializes in the preparation and dispensing of medicinal drugs, and acts as a drug expert to the public and healthcare providers.",
        "fees": "₹2 Lakh - ₹10 Lakh (Total Course)",
        "colleges": [
            "National Institute of Pharmaceutical Education and Research (NIPER), Mohali", "Jamia Hamdard, Delhi", "BITS Pilani",
            "Manipal College of Pharmaceutical Sciences", "JSS College of Pharmacy, Mysore", "Panjab University",
            "Poona College of Pharmacy", "Institute of Chemical Technology, Mumbai", "Madras Medical College", "SRM College of Pharmacy"
        ],
        "jobs": [
            "Retail Pharmacist", "Hospital Pharmacist", "Drug Inspector", "Research Scientist", "Pharmaceutical Sales Rep",
            "Quality Assurance Specialist", "Formulation Scientist", "Clinical Research Associate", "Regulatory Affairs Officer",
            "Academic Researcher",
            "Toxicologist", 
            "Medical Writer" 
        ],
        "internships": [
            {"role": "Dispensing Intern", "company": "Apollo Pharmacy", "duration": "3 months"},
            {"role": "QC Intern", "company": "Dr. Reddy's Labs", "duration": "6 months"},
            {"role": "Hospital Pharmacy Trainee", "company": "Max Healthcare", "duration": "3 months"}
        ]
    },

    # ------------------- COMMERCE GROUP -------------------
    {
        "topic": "Chartered Accountant (CA)",
        "stream": "Commerce/Any",
        "aptitude": "Accounts, Logic, Detail-Oriented",
        "personality": "Ethical, Methodical",
        "interest": "Finance, Taxation",
        "education": "CA (ICAI)",
        "cost": "Low (Exam Fees)",
        "difficulty": "Very Hard",
        "description": "Handles accounting, auditing, taxation, and financial advisory for individuals and businesses. Requires passing a tough set of exams.",
        "fees": "₹80,000 - ₹1,50,000 (Total CA Course Fees)",
        "colleges": [
            "The Institute of Chartered Accountants of India (ICAI)", "Shri Ram College of Commerce (SRCC), Delhi", 
            "Hindu College, Delhi", "Loyola College, Chennai", "Christ University, Bangalore", "St. Xavier's College, Kolkata",
            "Narsee Monjee College of Commerce and Economics, Mumbai", "Presidency College, Chennai", 
            "Hans Raj College, Delhi", "Symbiosis College of Arts and Commerce, Pune"
        ],
        "jobs": [
            "Auditor", "Tax Consultant", "Financial Analyst", "Management Consultant", "Forensic Accountant",
            "Internal Auditor", "Chief Financial Officer (CFO)", "Investment Banker", "Risk Manager", "Finance Manager",
            "Statutory Auditor", 
            "Business Consultant" 
        ],
        "internships": [
            {"role": "Audit Article-ship", "company": "Big 4 Firm (e.g., KPMG)", "duration": "3 years (Mandatory)"},
            {"role": "Taxation Intern", "company": "Mid-Sized CA Firm", "duration": "6 months"},
            {"role": "Accounting Trainee", "company": "Corporate Finance Dept.", "duration": "1 year"}
        ]
    },
    {
        "topic": "Financial Analyst",
        "stream": "Commerce/Any",
        "aptitude": "Maths, Statistics, Economics",
        "personality": "Analytical, Quick-thinker",
        "interest": "Stock Market, Investing",
        "education": "BBA/B.Com + MBA (Finance)",
        "cost": "Medium-High",
        "difficulty": "Medium-Hard",
        "description": "Evaluates financial data to recommend business strategies, investments, or financing decisions for clients or companies.",
        "fees": "₹5 Lakh - ₹25 Lakh (BBA + MBA)",
        "colleges": [
            "Indian Institute of Management (IIM) Ahmedabad (for MBA)", "Indian School of Business (ISB)", 
            "FMS Delhi", "NMIMS Mumbai", "XLRI Jamshedpur", "SPJIMR Mumbai", "Department of Financial Studies, DU",
            "Symbiosis School of Economics", "Madras School of Economics", "Gokhale Institute of Politics and Economics"
        ],
        "jobs": [
            "Equity Research Analyst", "Investment Banker", "Hedge Fund Analyst", "Portfolio Manager", 
            "Risk Analyst", "Credit Analyst", "Treasury Analyst", "Financial Planner", "Quantitative Analyst (Quant)", 
            "Asset Manager",
            "Hedge Fund Manager", 
            "Corporate Development Analyst" 
        ],
        "internships": [
            {"role": "Investment Banking Intern", "company": "Goldman Sachs", "duration": "10 weeks"},
            {"role": "Credit Risk Trainee", "company": "HDFC Bank", "duration": "3 months"},
            {"role": "Research Intern", "company": "Motilal Oswal", "duration": "6 months"}
        ]
    },

    # ------------------- ARTS/HUMANITIES GROUP -------------------
    {
        "topic": "Journalist/Mass Communication Specialist",
        "stream": "Arts/Any",
        "aptitude": "Language, Communication, General Knowledge",
        "personality": "Curious, Outgoing, Observant",
        "interest": "Media, Current Affairs, Writing",
        "education": "BA/BJMC",
        "cost": "Medium",
        "difficulty": "Medium",
        "description": "Researches, writes, and reports news and features for various media platforms (print, digital, broadcast).",
        "fees": "₹1 Lakh - ₹8 Lakh (Total Course)",
        "colleges": [
            "Indian Institute of Mass Communication (IIMC), Delhi", "A.J.K. Mass Communication Research Centre, Jamia Millia Islamia",
            "Symbiosis Institute of Media and Communication (SIMC), Pune", "Delhi University (various colleges)",
            "Xavier Institute of Communications (XIC), Mumbai", "Madras Christian College (MCC)",
            "Lady Shri Ram College for Women (LSR), Delhi", "Mudra Institute of Communications, Ahmedabad (MICA)",
            "Makhanlal Chaturvedi National University of Journalism and Communication", "Amity School of Communication"
        ],
        "jobs": [
            "News Reporter", "Content Writer", "Video Editor", "Public Relations Specialist", "Social Media Manager",
            "Broadcast Journalist", "Investigative Journalist", "Copywriter", "Photojournalist", "Media Planner",
            "Podcast Producer", 
            "Brand Strategist" 
        ],
        "internships": [
            {"role": "Editorial Intern", "company": "The Hindu", "duration": "3 months"},
            {"role": "PR Assistant", "company": "Edelman India", "duration": "4 months"},
            {"role": "Broadcast Trainee", "company": "NDTV", "duration": "6 months"}
        ]
    },
    {
        "topic": "Psychologist/Counsellor",
        "stream": "Arts/Science/Any",
        "aptitude": "Empathy, Analysis, Observation",
        "personality": "Patient, Good Listener",
        "interest": "Human Behaviour, Mental Health",
        "education": "BA (Psychology) + MA/M.Sc.",
        "cost": "Medium",
        "difficulty": "Medium-Hard",
        "description": "Studies the human mind and behaviour, helping individuals cope with mental or emotional challenges.",
        "fees": "₹2 Lakh - ₹8 Lakh (Total Course)",
        "colleges": [
            "Delhi University (various colleges)", "Christ University, Bangalore", "Tata Institute of Social Sciences (TISS), Mumbai",
            "National Institute of Mental Health and Neuro-Sciences (NIMHANS), Bangalore", "Amity University",
            "Jadavpur University", "Fergusson College, Pune", "Cochin University of Science and Technology",
            "University of Calcutta", "St. Francis College for Women, Hyderabad"
        ],
        "jobs": [
            "Clinical Psychologist", "Counselling Psychologist", "School Counsellor", "Industrial/Organizational Psychologist",
            "Research Psychologist", "Rehabilitation Specialist", "Sports Psychologist", "Forensic Psychologist",
            "HR Specialist (Training & Development)", "Social Worker",
            "Child Psychologist", 
            "Organizational Development Specialist" 
        ],
        "internships": [
            {"role": "Counselling Intern", "company": "Local NGO/Clinic", "duration": "3 months"},
            {"role": "Research Assistant", "company": "University Research Lab", "duration": "6 months"},
            {"role": "School Counsellor Trainee", "company": "Private School Chain", "duration": "4 months"}
        ]
    },
    # ------------------- Duplicates for top 10 results -------------------
    {
        "topic": "Data Scientist", 
        "stream": "Science-A/PCM", 
        "aptitude": "Maths, Coding, Statistics",
        "personality": "Problem-Solver, Analytical",
        "interest": "Coding, Data Analysis",
        "education": "B.Tech/BE (CS/IT) + M.Sc./PG Diploma",
        "cost": "Medium-High", 
        "difficulty": "Hard",
        "description": "Analyzes complex data sets to extract insights and inform business decisions.",
        "fees": "₹5 Lakh - ₹25 Lakh",
        "colleges": [
            "Indian Statistical Institute (ISI), Kolkata", "IIT Kharagpur", "BITS Pilani", "IIM (Analytics Programs)",
            "IIIT Bangalore", "University of Hyderabad", "SRMIST", "Amity University", "Manipal Academy", "JNU"
        ],
        "jobs": [
            "Data Analyst", "Business Intelligence Analyst", "Machine Learning Engineer", "AI Specialist",
            "Big Data Engineer", "Data Consultant", "Risk Analyst", "Database Architect", "Quantitative Analyst",
            "Research Scientist",
            "Deep Learning Engineer", 
            "NLP Scientist" 
        ],
        "internships": [
            {"role": "Data Analyst Intern", "company": "Amazon", "duration": "6 months"},
            {"role": "ML Research Trainee", "company": "TCS", "duration": "3 months"},
            {"role": "BI Intern", "company": "Accenture", "duration": "6 months"}
        ]
    },
    {
        "topic": "Veterinarian (B.V.Sc)", 
        "stream": "Science-B/PCB", 
        "aptitude": "Biology, Empathy, Observation",
        "personality": "Caring, Resilient, Practical",
        "interest": "Animals, Healthcare",
        "education": "B.V.Sc. & A.H.",
        "cost": "High", 
        "difficulty": "Very Hard",
        "description": "Deals with the treatment, health, and welfare of animals. Requires qualifying entrance exams like NEET.",
        "fees": "₹1 Lakh - ₹15 Lakh (Total Course)",
        "colleges": [
            "Indian Veterinary Research Institute (IVRI)", "GB Pant University", "Punjab Agricultural University", 
            "Madras Veterinary College", "Anand Agricultural University", "TANUVAS", "Maharashtra Animal & Fishery Sciences University",
            "Assam Agricultural University", "Rajiv Gandhi College of Veterinary and Animal Sciences", "SKLTSHU"
        ],
        "jobs": [
            "Veterinary Surgeon", "Animal Researcher", "Wildlife Biologist", "Dairy Consultant", 
            "Zoo Vet", "Public Health Vet", "Poultry Specialist", "Livestock Consultant", 
            "Companion Animal Vet", "Academic Lecturer",
            "Equine Vet", 
            "Laboratory Animal Vet" 
        ],
        "internships": [
            {"role": "Clinical Rotations", "company": "Govt. Veterinary Hospital", "duration": "1 year (Mandatory)"},
            {"role": "Farm Assistant", "company": "Dairy Farm X", "duration": "3 months"},
            {"role": "Wildlife Intern", "company": "National Park Y", "duration": "6 months"}
        ]
    },
    # ------------------- 40 NEW CAREER ENTRIES ADDED BELOW -------------------
    {
        "topic": "Aerospace Engineer",
        "stream": "Science-A/PCM",
        "aptitude": "Physics, Design, Logic, Advanced Math",
        "personality": "Innovator, Detail-Oriented, High Focus",
        "interest": "Space, Aircraft, Robotics",
        "education": "B.Tech/BE (Aerospace/Aeronautical)",
        "cost": "High",
        "difficulty": "Hard",
        "description": "Designs, develops, and tests aircraft, spacecraft, satellites, and missiles. Works with ISRO, HAL, or global aerospace companies.",
        "fees": "₹6 Lakh - ₹30 Lakh (Total Course)",
        "colleges": [
            "Indian Institute of Technology (IIT) Bombay", "IIT Madras", "Indian Institute of Science (IISc), Bangalore",
            "PEC Chandigarh", "Madras Institute of Technology (MIT)", "Amity University (Noida)", "Hindustan University",
            "UPES Dehradun", "Manipal Academy of Higher Education", "JNTU Hyderabad"
        ],
        "jobs": [
            "Aircraft Designer", "Propulsion Engineer", "Stress Analyst", "Avionics Engineer", 
            "Flight Test Engineer", "Satellite Systems Engineer", "Thermal Engineer", "Aerodynamics Specialist",
            "Mission Control Specialist", "UAV Developer"
        ],
        "internships": [
            {"role": "Design Trainee", "company": "Hindustan Aeronautics Ltd (HAL)", "duration": "6 months"},
            {"role": "Project Intern", "company": "ISRO Centers", "duration": "3 months"},
            {"role": "R&D Intern", "company": "DRDO Labs", "duration": "4 months"}
        ]
    },
    {
        "topic": "Mechanical Engineer",
        "stream": "Science-A/PCM",
        "aptitude": "Physics, Design, Practical, Kinematics",
        "personality": "Hands-on, Problem-Solver, Systems Thinker",
        "interest": "Automobiles, Manufacturing, Energy",
        "education": "B.Tech/BE (Mechanical)",
        "cost": "Medium-High",
        "difficulty": "Medium-Hard",
        "description": "Designs, analyzes, manufactures, and maintains mechanical systems. This is the broadest engineering field.",
        "fees": "₹3 Lakh - ₹15 Lakh (Total Course)",
        "colleges": [
            "IIT Kharagpur", "IIT Kanpur", "NIT Trichy", "Delhi Technological University (DTU)", "Jadavpur University",
            "College of Engineering, Pune (COEP)", "Anna University", "BITS Pilani", "Manipal Institute of Technology",
            "Osmania University"
        ],
        "jobs": [
            "Design Engineer", "Manufacturing Engineer", "Automotive Engineer", "HVAC Engineer", 
            "Robotics Engineer", "Maintenance Engineer", "Thermal Engineer", "Quality Assurance Engineer",
            "R&D Scientist", "CAD Specialist"
        ],
        "internships": [
            {"role": "Production Intern", "company": "Tata Motors", "duration": "6 months"},
            {"role": "Maintenance Trainee", "company": "NTPC", "duration": "3 months"},
            {"role": "Design Intern", "company": "Schlumberger", "duration": "4 months"}
        ]
    },
    {
        "topic": "Architect",
        "stream": "Science-A/Any", # Needs NATA/JEE Paper 2
        "aptitude": "Drawing, Design, Visual Arts, Math",
        "personality": "Creative, Visionary, Detail-Oriented",
        "interest": "Building Design, Urban Planning, Aesthetics",
        "education": "B.Arch (5 years)",
        "cost": "Medium-High",
        "difficulty": "Medium",
        "description": "Plans and designs buildings and open spaces, focusing on functionality, safety, and aesthetics.",
        "fees": "₹5 Lakh - ₹20 Lakh (Total Course)",
        "colleges": [
            "School of Planning and Architecture (SPA), Delhi", "IIT Kharagpur", "NIT Calicut", "CEPT University, Ahmedabad",
            "Sir JJ College of Architecture, Mumbai", "Anna University", "Jadavpur University", "Amity University",
            "Chandigarh College of Architecture", "Sushant University"
        ],
        "jobs": [
            "Residential Architect", "Urban Designer", "Landscape Architect", "Project Manager", 
            "Interior Designer", "Conservation Architect", "Sustainable Architect", "BIM Specialist",
            "Site Architect", "Design Consultant"
        ],
        "internships": [
            {"role": "Architectural Intern", "company": "Foster + Partners (India)", "duration": "6 months"},
            {"role": "Site Observer", "company": "DLF", "duration": "3 months"},
            {"role": "Design Assistant", "company": "Small Design Firm", "duration": "1 year"}
        ]
    },
    {
        "topic": "Pilot (Commercial)",
        "stream": "Science-A/Any",
        "aptitude": "Focus, Quick Reflexes, Physics, Decision-Making",
        "personality": "Resilient, Responsible, Cool-Headed",
        "interest": "Aviation, Travel, Technology",
        "education": "10+2 (PCM) + Commercial Pilot License (CPL)",
        "cost": "Very High",
        "difficulty": "Hard",
        "description": "Flies and navigates aircraft for commercial airlines. Requires extensive training and flight hours.",
        "fees": "₹30 Lakh - ₹60 Lakh (Total Training Cost)",
        "colleges": [
            "Indira Gandhi Rashtriya Uran Akademi (IGRUA)", "Bombay Flying Club", "Delhi Flying Club",
            "National Flying Training Institute", "Madhya Pradesh Flying Club", "Chimes Aviation Academy",
            "Government Aviation Training Institute, Bhubaneswar", "Various Foreign Academies",
            "Redbird Flight Training", "CAE Gondia"
        ],
        "jobs": [
            "First Officer", "Captain", "Flight Instructor", "Cargo Pilot", 
            "Test Pilot", "Private Jet Pilot", "Air Traffic Controller (Requires separate training)", "Ground Instructor",
            "Aviation Consultant", "Airline Operations Manager"
        ],
        "internships": [
            {"role": "Cadet Program", "company": "Indigo/Air India", "duration": "1-2 years"},
            {"role": "Ground Duty Trainee", "company": "Airport Operations", "duration": "6 months"},
            {"role": "Simulator Training", "company": "Flight Academy", "duration": "Ongoing"}
        ]
    },
    {
        "topic": "Chemist/Research Scientist",
        "stream": "Science-A/PCM, Science-B/PCB",
        "aptitude": "Chemistry, Research, Detail, Methodical",
        "personality": "Inquisitive, Patient, Analytical",
        "interest": "Experiments, Material Science, Pharmaceuticals",
        "education": "M.Sc./Ph.D. (Chemistry/Applied Science)",
        "cost": "Medium",
        "difficulty": "Hard",
        "description": "Conducts research to discover new compounds, materials, or processes in chemical and industrial labs.",
        "fees": "₹1 Lakh - ₹10 Lakh (Total Post-Grad/Ph.D.)",
        "colleges": [
            "Indian Institute of Science (IISc), Bangalore", "IIT Kanpur", "IIT Madras", "Delhi University (North Campus)",
            "Jawaharlal Nehru University (JNU)", "Tata Institute of Fundamental Research (TIFR)", 
            "BITS Pilani", "University of Hyderabad", "Indian Institute of Science Education and Research (IISER)",
            "University of Calcutta"
        ],
        "jobs": [
            "Analytical Chemist", "Organic Chemist", "Materials Scientist", "Forensic Scientist", 
            "Polymer Scientist", "Quality Control Manager", "Process Development Chemist", "Toxicologist",
            "Research Associate", "Academic Professor"
        ],
        "internships": [
            {"role": "Lab Assistant Intern", "company": "CSIR Labs", "duration": "6 months"},
            {"role": "R&D Intern", "company": "Reliance/Tata Chemicals", "duration": "3 months"},
            {"role": "Ph.D. Researcher", "company": "University Research Project", "duration": "3-5 years"}
        ]
    },
    {
        "topic": "Biotechnologist",
        "stream": "Science-B/PCB",
        "aptitude": "Biology, Genetics, Research, Chemistry",
        "personality": "Methodical, Innovative, Detail-Oriented",
        "interest": "Genetic Modification, Pharmaceuticals, Biofuels",
        "education": "B.Tech/B.Sc. + M.Sc./M.Tech (Biotechnology)",
        "cost": "Medium-High",
        "difficulty": "Hard",
        "description": "Uses living organisms and bioprocesses to create products or solve problems, especially in medicine and agriculture.",
        "fees": "₹4 Lakh - ₹20 Lakh (Total Course)",
        "colleges": [
            "IIT Delhi", "IIT Madras", "Vellore Institute of Technology (VIT)", "Anna University", "Jawaharlal Nehru University (JNU)",
            "All India Institute of Medical Sciences (AIIMS)", "Indian Institute of Science (IISc)", 
            "Manipal Academy of Higher Education", "Amity University", "BITS Pilani"
        ],
        "jobs": [
            "Research Scientist", "Clinical Research Coordinator", "Quality Assurance Specialist", "Biomanufacturing Specialist",
            "Bioinformatics Analyst", "Genetics Counsellor", "Biomedical Engineer", "Environmental Biotechnologist",
            "Drug Development Scientist", "Lab Manager"
        ],
        "internships": [
            {"role": "Research Intern", "company": "Biocon", "duration": "6 months"},
            {"role": "Lab Trainee", "company": "Government Research Labs", "duration": "3 months"},
            {"role": "Clinical Trial Assistant", "company": "Pharmaceutical CRO", "duration": "6 months"}
        ]
    },
    {
        "topic": "Marine Biologist",
        "stream": "Science-B/PCB",
        "aptitude": "Biology, Observation, Fieldwork, Patience",
        "personality": "Curious, Adventurous, Resilient",
        "interest": "Ocean Life, Conservation, Ecology",
        "education": "B.Sc. + M.Sc. (Marine Biology)",
        "cost": "Medium",
        "difficulty": "Medium",
        "description": "Studies life in oceans, seas, and other aquatic environments, focusing on ecology and conservation.",
        "fees": "₹1 Lakh - ₹8 Lakh (Total Course)",
        "colleges": [
            "Cochin University of Science and Technology (CUSAT)", "Andhra University", "Annamalai University",
            "Goa University", "Central Marine Fisheries Research Institute (CMFRI)", "University of Madras",
            "Pondicherry University", "Karnataka University", "Kerala University of Fisheries and Ocean Studies",
            "Dr. Babasaheb Ambedkar Marathwada University"
        ],
        "jobs": [
            "Field Researcher", "Fishery Scientist", "Aquaculture Specialist", "Conservation Officer (NGO/Govt)",
            "Environmental Consultant", "Oceanographer", "Zoo/Aquarium Biologist", "Data Analyst (Marine)",
            "Science Communicator", "Academic Lecturer"
        ],
        "internships": [
            {"role": "Field Research Assistant", "company": "CMFRI", "duration": "3 months"},
            {"role": "Conservation Intern", "company": "WWF India", "duration": "6 months"},
            {"role": "Aquarium Volunteer", "company": "Local Aquarium/Zoo", "duration": "Flexible"}
        ]
    },
    {
        "topic": "Dentist (BDS)",
        "stream": "Science-B/PCB",
        "aptitude": "Biology, Fine Motor Skills, Patience, Precision",
        "personality": "Patient, Detail-Oriented, Good Communicator",
        "interest": "Oral Health, Surgery, Aesthetics",
        "education": "BDS (Bachelor of Dental Surgery)",
        "cost": "High",
        "difficulty": "Hard",
        "description": "Diagnoses and treats diseases and conditions of the oral cavity. Focuses on patient care and surgical procedures.",
        "fees": "₹15 Lakh - ₹40 Lakh (Total Course, Private)",
        "colleges": [
            "All India Institute of Medical Sciences (AIIMS), New Delhi", "Maulana Azad Medical College (MAMC)", 
            "King George's Medical University (KGMU)", "Manipal College of Dental Sciences", 
            "Christian Medical College (CMC), Vellore", "Armed Forces Medical College (AFMC), Pune",
            "Government Dental College & Hospital, Mumbai", "Dr. D. Y. Patil Dental College and Hospital, Pune",
            "SDM College of Dental Sciences, Dharwad", "SRM Dental College, Chennai"
        ],
        "jobs": [
            "General Dentist", "Oral Surgeon", "Orthodontist", "Endodontist", 
            "Periodontist", "Pediatric Dentist", "Public Health Dentist", "Forensic Odontologist",
            "Academic Professor", "Dental Consultant"
        ],
        "internships": [
            {"role": "Clinical Internship", "company": "Teaching Hospital", "duration": "1 year (Mandatory)"},
            {"role": "Assistant Dentist", "company": "Private Clinic", "duration": "6 months"},
            {"role": "Research Fellow", "company": "Dental School Lab", "duration": "3 months"}
        ]
    },
    {
        "topic": "Nurse/Paramedic",
        "stream": "Science-B/PCB",
        "aptitude": "Caring, Quick Action, Stress Mgt, Anatomy",
        "personality": "Caring, Resilient, Team Player",
        "interest": "Patient Care, Emergency Response, Health",
        "education": "B.Sc. (Nursing) / Paramedical Diploma",
        "cost": "Medium",
        "difficulty": "Medium",
        "description": "Provides direct patient care, administers medications, and assists doctors. Paramedics handle emergency pre-hospital care.",
        "fees": "₹1 Lakh - ₹10 Lakh (Total Course)",
        "colleges": [
            "All India Institute of Medical Sciences (AIIMS)", "Armed Forces Medical College (AFMC)", 
            "Post Graduate Institute of Medical Education and Research (PGIMER)", "Christian Medical College (CMC), Vellore",
            "Manipal College of Nursing Sciences", "Apollo College of Nursing", 
            "Jamia Hamdard University", "Rajiv Gandhi University of Health Sciences",
            "National Institute of Mental Health and Neuro-Sciences (NIMHANS)", "Various Government Colleges"
        ],
        "jobs": [
            "Staff Nurse", "Critical Care Nurse", "Emergency Medical Technician (EMT)", "Surgical Assistant",
            "Midwife", "Nurse Educator", "Health Visitor", "ICU Nurse",
            "Flight Paramedic", "Hospital Administrator"
        ],
        "internships": [
            {"role": "Clinical Rotations", "company": "Hospital Wards", "duration": "Mandatory"},
            {"role": "Paramedic Trainee", "company": "Ambulance Service", "duration": "3 months"},
            {"role": "Home Care Assistant", "company": "Elder Care Service", "duration": "Flexible"}
        ]
    },
    {
        "topic": "Lawyer (LLB)",
        "stream": "Commerce/Arts/Any",
        "aptitude": "Debate, Logic, Communication, Research",
        "personality": "Ethical, Articulate, Resilient",
        "interest": "Justice, Policy, Legal Systems",
        "education": "LLB (3 or 5 years after 10+2)",
        "cost": "Medium-High",
        "difficulty": "Hard",
        "description": "Practices law, representing clients in court or providing legal advice for corporate matters. Requires passing the Bar exam.",
        "fees": "₹3 Lakh - ₹25 Lakh (Total Course)",
        "colleges": [
            "National Law School of India University (NLSIU), Bangalore", "NALSAR University of Law, Hyderabad", 
            "National Law University (NLU), Delhi", "The West Bengal National University of Juridical Sciences (NUJS)",
            "Faculty of Law, Delhi University (DU)", "Symbiosis Law School, Pune", 
            "Government Law College, Mumbai", "Amity Law School",
            "Jindal Global Law School", "ILS Law College, Pune"
        ],
        "jobs": [
            "Litigation Lawyer (Criminal/Civil)", "Corporate Lawyer", "Legal Consultant", "Patent Attorney", 
            "Judge (after further exams)", "Public Prosecutor", "Legal Counsel (in-house)", "Tax Lawyer",
            "Human Rights Lawyer", "Academics"
        ],
        "internships": [
            {"role": "Judicial Clerkship", "company": "High Court Justice", "duration": "1 month"},
            {"role": "Intern", "company": "Tier 1 Law Firm", "duration": "6 weeks"},
            {"role": "NGO Intern", "company": "Human Rights Organization", "duration": "3 months"}
        ]
    },
    {
        "topic": "Economist",
        "stream": "Commerce/Arts/Any",
        "aptitude": "Maths, Statistics, Analysis, Theory",
        "personality": "Analytical, Objective, Research-Oriented",
        "interest": "Finance, Policy, Global Markets",
        "education": "B.A./B.Sc. + M.A. (Economics)",
        "cost": "Medium",
        "difficulty": "Medium-Hard",
        "description": "Studies the production, distribution, and consumption of goods and services, often advising governments or businesses on policy.",
        "fees": "₹1 Lakh - ₹15 Lakh (Total Course)",
        "colleges": [
            "Delhi School of Economics (DSE), DU", "Indian Statistical Institute (ISI), Kolkata", "JNU (Centre for Economic Studies)",
            "Madras School of Economics", "Ashoka University", "St. Stephen's College, DU", 
            "Loyola College, Chennai", "Christ University, Bangalore",
            "Gokhale Institute of Politics and Economics", "University of Hyderabad"
        ],
        "jobs": [
            "Economic Advisor (Govt.)", "Market Research Analyst", "Quantitative Analyst (Quant)", "Forecaster", 
            "Financial Consultant", "Policy Analyst", "Central Bank Economist", "Data Scientist (Economic)",
            "Professor/Academic", "Development Economist"
        ],
        "internships": [
            {"role": "Research Intern", "company": "RBI/NITI Aayog", "duration": "3 months"},
            {"role": "Data Analyst Trainee", "company": "World Bank/IMF (local office)", "duration": "6 months"},
            {"role": "Market Analyst Intern", "company": "Financial Firm", "duration": "3 months"}
        ]
    },
    {
        "topic": "Marketing Manager",
        "stream": "Commerce/Arts/Any",
        "aptitude": "Communication, Sales, Creativity, Data Analysis",
        "personality": "Outgoing, Persuasive, Strategic",
        "interest": "Consumer Trends, Branding, Advertising",
        "education": "BBA/B.Com + MBA (Marketing)",
        "cost": "Medium-High",
        "difficulty": "Medium",
        "description": "Plans and executes campaigns to promote products or services. Requires a blend of creativity, consumer psychology, and data analysis.",
        "fees": "₹5 Lakh - ₹30 Lakh (BBA + MBA)",
        "colleges": [
            "IIM Ahmedabad (MBA)", "XLRI Jamshedpur", "FMS Delhi", "SPJIMR Mumbai", 
            "Mudra Institute of Communications (MICA)", "NMIMS Mumbai", "Symbiosis Institute of Business Management (SIBM)",
            "Indian School of Business (ISB)", "Christ University", "Department of Management Studies, IIT Delhi"
        ],
        "jobs": [
            "Brand Manager", "Digital Marketing Specialist", "Product Manager", "Market Research Analyst", 
            "Advertising Manager", "Content Strategist", "Sales Manager", "Public Relations Manager",
            "SEO/SEM Specialist", "E-commerce Manager"
        ],
        "internships": [
            {"role": "Marketing Intern", "company": "Hindustan Unilever (HUL)", "duration": "8 weeks"},
            {"role": "Sales Trainee", "company": "FMCG Company", "duration": "3 months"},
            {"role": "Digital Campaign Assistant", "company": "Advertising Agency", "duration": "6 months"}
        ]
    },
    {
        "topic": "Human Resources Manager",
        "stream": "Commerce/Arts/Any",
        "aptitude": "Empathy, Management, Negotiation, Policy",
        "personality": "Patient, Fair, Good Listener, Organizer",
        "interest": "People Management, Corporate Culture, Labour Laws",
        "education": "BBA/Any Grad + MBA (HR) / PG Diploma",
        "cost": "Medium-High",
        "difficulty": "Medium",
        "description": "Manages employee relations, recruitment, training, compensation, and adherence to labour policies within an organization.",
        "fees": "₹4 Lakh - ₹25 Lakh (Total Post-Grad)",
        "colleges": [
            "XLRI Jamshedpur", "Tata Institute of Social Sciences (TISS), Mumbai", "IIM Calcutta (MBA)",
            "Symbiosis Institute of Business Management (SIBM)", "NMIMS Mumbai", 
            "Mudra Institute of Communications (MICA)", "Indian School of Business (ISB)",
            "IIM Lucknow", "Xavier Institute of Management (XIMB)", "Amity University"
        ],
        "jobs": [
            "Recruiter", "Training & Development Specialist", "Compensation Analyst", "Employee Relations Manager", 
            "HR Generalist", "HR Business Partner (HRBP)", "Organizational Development Specialist", "Change Manager",
            "Talent Acquisition Head", "Labour Law Compliance Officer"
        ],
        "internships": [
            {"role": "HR Intern", "company": "TCS/Infosys", "duration": "6 months"},
            {"role": "Recruitment Trainee", "company": "Staffing Agency", "duration": "3 months"},
            {"role": "Employee Engagement Intern", "company": "Large Corporate", "duration": "4 months"}
        ]
    },
    {
        "topic": "Investment Banker",
        "stream": "Commerce/Any",
        "aptitude": "Finance, Negotiation, High Pressure, Analysis",
        "personality": "Aggressive, Decisive, High Stamina, Ethical",
        "interest": "Mergers & Acquisitions, IPOs, Capital Markets",
        "education": "B.Com/BBA/B.Tech + MBA (Finance) / CFA",
        "cost": "Very High",
        "difficulty": "Very Hard",
        "description": "Advises governments and corporations on complex financial transactions like mergers, acquisitions, and raising capital.",
        "fees": "₹10 Lakh - ₹40 Lakh (MBA/PGP)",
        "colleges": [
            "Indian School of Business (ISB), Hyderabad", "IIM Ahmedabad", "IIM Bangalore", "FMS Delhi",
            "NMIMS Mumbai", "XLRI Jamshedpur", "SPJIMR Mumbai", "SRCC, DU (B.Com)",
            "St. Xavier's College, Mumbai", "Christ University, Bangalore"
        ],
        "jobs": [
            "Analyst (Entry-Level)", "Associate", "Vice President (VP)", "Managing Director (MD)", 
            "M&A Specialist", "Private Equity Analyst", "Venture Capitalist", "Risk Manager",
            "Research Analyst", "Trader"
        ],
        "internships": [
            {"role": "Summer Analyst", "company": "Goldman Sachs/Morgan Stanley", "duration": "10 weeks"},
            {"role": "Private Equity Intern", "company": "Carlyle Group (India)", "duration": "3 months"},
            {"role": "Financial Modeling Trainee", "company": "Boutique IB Firm", "duration": "6 months"}
        ]
    },
    {
        "topic": "Social Media Content Creator",
        "stream": "Arts/Any",
        "aptitude": "Creativity, Trend Analysis, Video Editing, Writing",
        "personality": "Outgoing, Charismatic, Self-Motivated, Quick Thinker",
        "interest": "Digital Media, Influencing, Storytelling",
        "education": "Self-Taught / Digital Marketing Diploma / BA (Mass Comm)",
        "cost": "Low (Skill-Based)",
        "difficulty": "Medium-Hard (Building Audience)",
        "description": "Creates engaging content (videos, posts, blogs) for social media platforms to build a personal brand or promote products.",
        "fees": "₹0 - ₹5 Lakh (Formal Education Optional)",
        "colleges": [
            "Online Courses/YouTube", "Whistling Woods International", "Asian Academy of Film & TV (AAFT)",
            "NIFT (for Visuals)", "Symbiosis Institute of Media and Communication (SIMC)", 
            "IIMC, Delhi", "Christ University, Bangalore", "Amity School of Communication",
            "UPES Dehradun (Digital Marketing)", "Online platforms like Coursera/Udemy"
        ],
        "jobs": [
            "YouTuber", "Instagram Influencer", "TikTok/Reel Creator", "Brand Ambassador", 
            "Affiliate Marketer", "Social Media Strategist", "Video Editor (Freelance)", "Content Writer",
            "Digital Nomad", "E-commerce Seller"
        ],
        "internships": [
            {"role": "Social Media Intern", "company": "Digital Agency", "duration": "3 months"},
            {"role": "Content Creation Assistant", "company": "Established Influencer", "duration": "6 months"},
            {"role": "Marketing Trainee", "company": "Startup", "duration": "4 months"}
        ]
    },
    {
        "topic": "Graphic Designer",
        "stream": "Arts/Any",
        "aptitude": "Visual Arts, Software Skills, Creativity, Attention to Detail",
        "personality": "Creative, Patient, Responsive to Feedback",
        "interest": "Branding, Typography, Illustration, Web Design",
        "education": "B.Des / BFA / Diploma in Graphic Design",
        "cost": "Medium",
        "difficulty": "Medium",
        "description": "Creates visual concepts using computer software or by hand, to communicate ideas that inspire, inform, and captivate consumers.",
        "fees": "₹4 Lakh - ₹15 Lakh (Total Course)",
        "colleges": [
            "National Institute of Design (NID), Ahmedabad", "National Institute of Fashion Technology (NIFT)", 
            "Industrial Design Centre (IDC), IIT Bombay", "Symbiosis Institute of Design (SID), Pune",
            "Pearl Academy, Delhi", "Srishti Institute of Art, Design and Technology", 
            "MAEER's MIT Institute of Design", "College of Art, Delhi",
            "Narayana School of Architecture", "Amity School of Design"
        ],
        "jobs": [
            "Brand Designer", "UI/UX Designer", "Motion Graphic Artist", "Packaging Designer", 
            "Web Designer", "Layout Artist (Publishing)", "Visualizer (Advertising)", "Illustrator (Freelance)",
            "Art Director", "Design Educator"
        ],
        "internships": [
            {"role": "Design Intern", "company": "Digital Marketing Agency", "duration": "6 months"},
            {"role": "UI Trainee", "company": "Tech Startup", "duration": "3 months"},
            {"role": "Branding Assistant", "company": "Corporate Marketing Dept.", "duration": "4 months"}
        ]
    },
    {
        "topic": "Historian/Archaeologist",
        "stream": "Arts/Any",
        "aptitude": "Research, Memory, Patience, Analytical Writing",
        "personality": "Curious, Methodical, Detail-Oriented",
        "interest": "Ancient Cultures, Archives, Excavation",
        "education": "B.A. + M.A. (History/Archaeology)",
        "cost": "Low-Medium",
        "difficulty": "Medium",
        "description": "Studies and interprets the past through historical records or excavation of artifacts and sites.",
        "fees": "₹1 Lakh - ₹5 Lakh (Total Course)",
        "colleges": [
            "Jawaharlal Nehru University (JNU)", "Delhi University (various colleges)", "University of Calcutta",
            "Banaras Hindu University (BHU)", "Aligarh Muslim University (AMU)", 
            "Archaeological Survey of India (ASI) Institutes", "University of Mumbai",
            "Loyola College, Chennai", "Presidency College, Kolkata", "Centre for Archaeology (TISS)"
        ],
        "jobs": [
            "Academic Professor", "Archivist", "Museum Curator", "Conservation Specialist", 
            "Excavation Director", "Heritage Consultant", "Genealogist", "Historical Researcher",
            "Government Policy Advisor", "Librarian"
        ],
        "internships": [
            {"role": "Research Assistant", "company": "University History Department", "duration": "6 months"},
            {"role": "Excavation Volunteer", "company": "ASI Site", "duration": "3 months"},
            {"role": "Archival Intern", "company": "National Archives of India", "duration": "4 months"}
        ]
    },
    {
        "topic": "Foreign Language Expert/Translator",
        "stream": "Arts/Any",
        "aptitude": "Language, Memory, Cultural Awareness, Communication",
        "personality": "Detail-Oriented, Patient, Adaptable",
        "interest": "Global Cultures, Travel, Linguistics",
        "education": "B.A. + M.A. (Foreign Language) / Diplomas",
        "cost": "Low-Medium",
        "difficulty": "Medium",
        "description": "Specializes in one or more foreign languages (e.g., French, Japanese, Mandarin) for translation, interpretation, or business liaison.",
        "fees": "₹50,000 - ₹5 Lakh (Total Course)",
        "colleges": [
            "Jawaharlal Nehru University (JNU)", "Delhi University (various colleges)", "English and Foreign Languages University (EFLU)",
            "University of Pune", "Visva-Bharati University", 
            "Amity University (Centre for Languages)", "Alliance Française (for French)",
            "Max Mueller Bhavan (for German)", "Various Embassies/Cultural Centers", "Christ University"
        ],
        "jobs": [
            "Interpreter (Consecutive/Simultaneous)", "Translator (Technical/Literary)", "Language Teacher", "Tour Guide", 
            "Foreign Service Officer (IFS)", "Linguistics Researcher", "Business Liaison/Consultant", "Content Localizer",
            "Subtitler/Dubber", "Diplomatic Staff"
        ],
        "internships": [
            {"role": "Translation Intern", "company": "MNC Language Dept.", "duration": "3 months"},
            {"role": "Cultural Exchange Volunteer", "company": "Foreign Embassy", "duration": "6 months"},
            {"role": "Research Assistant", "company": "JNU Language Center", "duration": "4 months"}
        ]
    },
    {
        "topic": "Fashion Designer",
        "stream": "Arts/Any",
        "aptitude": "Drawing, Trend Analysis, Creativity, Sewing Skills",
        "personality": "Creative, Innovative, Business Savvy",
        "interest": "Clothing, Textiles, Styling, Runway",
        "education": "B.Des (Fashion Design) / Diploma",
        "cost": "High",
        "difficulty": "Medium-Hard",
        "description": "Creates original clothing, footwear, and accessories, often specializing in Haute Couture, Ready-to-Wear, or costume design.",
        "fees": "₹6 Lakh - ₹30 Lakh (Total Course)",
        "colleges": [
            "National Institute of Fashion Technology (NIFT) - various campuses", "National Institute of Design (NID), Gandhinagar", 
            "Pearl Academy, Delhi", "Symbiosis Institute of Design (SID), Pune",
            "JD Institute of Fashion Technology", "Amity School of Fashion Technology", 
            "School of Fashion Technology (SOFT), Pune", "Srishti Institute of Art, Design and Technology",
            "Indian Institute of Art and Design (IIAD)", "Lakhotia Institute of Design"
        ],
        "jobs": [
            "Apparel Designer", "Stylist", "Textile Designer", "Merchandiser", 
            "Visual Display Artist", "Costume Designer", "Pattern Maker", "Fashion Illustrator",
            "Fashion Journalist/Blogger", "Retail Buyer"
        ],
        "internships": [
            {"role": "Design Intern", "company": "Manish Malhotra/Sabyasachi", "duration": "6 months"},
            {"role": "Production Assistant", "company": "Garment Export House", "duration": "3 months"},
            {"role": "Styling Trainee", "company": "Magazine/E-commerce", "duration": "4 months"}
        ]
    },
    {
        "topic": "Chef/Culinary Artist",
        "stream": "Arts/Any",
        "aptitude": "Taste, Precision, Stress Mgt, Creativity",
        "personality": "Disciplined, Hardworking, Innovative, Team Leader",
        "interest": "Cooking, Food Science, Global Cuisine",
        "education": "Diploma/Degree in Culinary Arts or Hotel Management",
        "cost": "Medium",
        "difficulty": "Hard (Working Hours)",
        "description": "Manages kitchen operations, plans menus, and prepares high-quality food in restaurants, hotels, or as a private chef.",
        "fees": "₹2 Lakh - ₹12 Lakh (Total Course)",
        "colleges": [
            "Institute of Hotel Management (IHM) - various branches", "Welcomegroup Graduate School of Hotel Administration, Manipal", 
            "Oberoi Centre of Learning and Development (OCLD)", "Army Institute of Hotel Management and Catering Technology",
            "Christ University (Hotel Management)", "NIMAS Academy", 
            "IIHM - various campuses", "Amity School of Hospitality",
            "Indian Culinary Institute (ICI)", "Rizvi College of Hotel Management"
        ],
        "jobs": [
            "Commis (Entry-Level)", "Chef de Partie", "Sous Chef", "Executive Chef", 
            "Pastry Chef", "Food Consultant", "Catering Manager", "Food Stylist/Blogger",
            "Restaurant Owner/Entrepreneur", "Culinary Educator"
        ],
        "internships": [
            {"role": "Kitchen Intern", "company": "Taj/Oberoi Hotel", "duration": "6 months"},
            {"role": "Catering Trainee", "company": "Event Management Company", "duration": "3 months"},
            {"role": "Pastry Assistant", "company": "Local Bakery", "duration": "4 months"}
        ]
    },
    {
        "topic": "Electrical Engineer",
        "stream": "Science-A/PCM",
        "aptitude": "Physics, Circuitry, Logic, Math",
        "personality": "Detail-Oriented, Problem-Solver, Practical",
        "interest": "Power Systems, Electronics, Renewable Energy",
        "education": "B.Tech/BE (Electrical/Electronics)",
        "cost": "Medium-High",
        "difficulty": "Hard",
        "description": "Designs and develops electrical equipment, from small electronic devices to large power grids and transmission systems.",
        "fees": "₹4 Lakh - ₹20 Lakh (Total Course)",
        "colleges": [
            "IIT Delhi", "IIT Kharagpur", "NIT Trichy", "Delhi Technological University (DTU)", "Jadavpur University",
            "BITS Pilani", "Anna University", "College of Engineering, Pune (COEP)", "VIT Vellore",
            "Manipal Institute of Technology"
        ],
        "jobs": [
            "Power Engineer", "Control Systems Engineer", "Electronics Designer", "R&D Engineer", 
            "Test Engineer", "Field Service Engineer", "Transmission Specialist", "Substation Manager",
            "Automation Engineer", "Telecom Engineer"
        ],
        "internships": [
            {"role": "Project Intern", "company": "BHEL/NTPC", "duration": "6 months"},
            {"role": "Design Trainee", "company": "Siemens/GE", "duration": "3 months"},
            {"role": "Maintenance Intern", "company": "Power Grid Corporation", "duration": "4 months"}
        ]
    },
    {
        "topic": "Petroleum Engineer",
        "stream": "Science-A/PCM",
        "aptitude": "Geology, Chemistry, Problem-Solver, High Stamina",
        "personality": "Resilient, Analytical, Team Player, Fieldwork Ready",
        "interest": "Oil & Gas Exploration, Earth Science, Energy",
        "education": "B.Tech/BE (Petroleum/Chemical)",
        "cost": "High",
        "difficulty": "Hard",
        "description": "Works on the exploration and production of crude oil and natural gas, often in challenging remote locations.",
        "fees": "₹5 Lakh - ₹25 Lakh (Total Course)",
        "colleges": [
            "Indian Institute of Technology (IIT) Kharagpur", "IIT Bombay", "University of Petroleum and Energy Studies (UPES), Dehradun",
            "Indian Institute of Technology (ISM), Dhanbad", "Maharashtra Institute of Technology (MIT), Pune",
            "Pandit Deendayal Energy University (PDEU)", "Rajiv Gandhi Institute of Petroleum Technology (RGIPT)",
            "BITS Pilani", "Anna University", "Osmania University"
        ],
        "jobs": [
            "Drilling Engineer", "Reservoir Engineer", "Production Engineer", "Completion Engineer", 
            "Subsurface Manager", "Geophysicist", "Petrochemical Engineer", "Safety Engineer",
            "Field Engineer", "Well Log Analyst"
        ],
        "internships": [
            {"role": "Field Intern", "company": "ONGC/Oil India", "duration": "6 months"},
            {"role": "Reservoir Trainee", "company": "Schlumberger/Halliburton", "duration": "3 months"},
            {"role": "Process Intern", "company": "Reliance Industries", "duration": "4 months"}
        ]
    },
    {
        "topic": "Naval Architect",
        "stream": "Science-A/PCM",
        "aptitude": "Design, Fluid Dynamics, Practical, Math",
        "personality": "Creative, Analytical, Detail-Oriented, Problem-Solver",
        "interest": "Ships, Submarines, Maritime Systems",
        "education": "B.Tech/BE (Naval Architecture & Ocean Eng)",
        "cost": "Medium-High",
        "difficulty": "Hard",
        "description": "Designs, constructs, and repairs marine vessels and structures, ensuring they are safe, seaworthy, and efficient.",
        "fees": "₹4 Lakh - ₹20 Lakh (Total Course)",
        "colleges": [
            "Indian Institute of Technology (IIT) Kharagpur", "IIT Madras", "Cochin University of Science and Technology (CUSAT)",
            "Andhra University", "Indian Maritime University (IMU)", 
            "Visakhapatnam Shipyard", "LBS College of Engineering", "MIT, Manipal",
            "Defence Institute of Advanced Technology (DIAT)", "Indian Naval Academy (through UPSC)"
        ],
        "jobs": [
            "Ship Designer", "Marine Surveyor", "Yacht Builder", "Offshore Platform Designer", 
            "Hydrodynamics Specialist", "Production Manager (Shipyard)", "Ship Repair Manager", "Marine Engineer",
            "Naval Officer", "Consultant"
        ],
        "internships": [
            {"role": "Design Intern", "company": "Mazagon Dock Shipbuilders", "duration": "6 months"},
            {"role": "Shipyard Trainee", "company": "Cochin Shipyard Ltd.", "duration": "3 months"},
            {"role": "Naval Internship", "company": "Indian Navy Workshop", "duration": "4 months"}
        ]
    },
    {
        "topic": "Space Scientist/Astrophysicist",
        "stream": "Science-A/PCM",
        "aptitude": "Advanced Maths, Physics, Theory, Research",
        "personality": "Intellectual, Patient, Inquisitive, Independent",
        "interest": "Astronomy, Cosmology, Space Exploration",
        "education": "M.Sc. + Ph.D. (Astrophysics/Space Science)",
        "cost": "Medium-Low",
        "difficulty": "Very Hard",
        "description": "Studies the physical properties of objects in space, develops astronomical theories, and works on space missions.",
        "fees": "₹1 Lakh - ₹10 Lakh (Total Post-Grad/Ph.D.)",
        "colleges": [
            "Indian Institute of Science (IISc), Bangalore", "Tata Institute of Fundamental Research (TIFR)", 
            "Indian Institute of Science Education and Research (IISER)", "Inter-University Centre for Astronomy and Astrophysics (IUCAA)",
            "Physical Research Laboratory (PRL)", "Raman Research Institute", 
            "Jawaharlal Nehru University (JNU)", "University of Delhi",
            "Indian Institute of Astrophysics (IIA)", "Space Physics Lab (ISRO)"
        ],
        "jobs": [
            "Research Scientist (ISRO/DRDO)", "Academic Professor", "Observational Astronomer", "Theoretical Astrophysicist", 
            "Cosmologist", "Payload Specialist", "Data Scientist (Space Data)", "Science Communicator",
            "Mission Planner", "Aerospace Consultant"
        ],
        "internships": [
            {"role": "Research Fellow", "company": "IUCAA/TIFR", "duration": "6 months"},
            {"role": "Student Intern", "company": "ISRO/PRL", "duration": "3 months"},
            {"role": "Project Assistant", "company": "University Physics Dept.", "duration": "4 months"}
        ]
    },
    {
        "topic": "Geologist",
        "stream": "Science-A/PCM, Science-B/PCB",
        "aptitude": "Fieldwork, Observation, Earth Science, Mapping",
        "personality": "Practical, Observant, Resilient, Detail-Oriented",
        "interest": "Rocks, Minerals, Earth's History, Natural Resources",
        "education": "B.Sc. + M.Sc. (Geology/Applied Geology)",
        "cost": "Medium",
        "difficulty": "Medium",
        "description": "Studies the composition, structure, and processes of the Earth, searching for natural resources and analyzing hazards.",
        "fees": "₹1 Lakh - ₹8 Lakh (Total Course)",
        "colleges": [
            "Indian Institute of Technology (ISM), Dhanbad", "Jawaharlal Nehru University (JNU)", "University of Delhi",
            "Banaras Hindu University (BHU)", "Presidency University, Kolkata", 
            "Wadia Institute of Himalayan Geology", "Anna University",
            "Indian Institute of Science Education and Research (IISER)", "University of Calcutta", "Osmania University"
        ],
        "jobs": [
            "Field Geologist", "Hydrogeologist (Water)", "Mining Geologist", "Petroleum Geologist", 
            "Seismologist", "Environmental Consultant", "Geological Survey of India Officer", "Geotechnical Engineer",
            "Academic Professor", "Museum Curator"
        ],
        "internships": [
            {"role": "Field Intern", "company": "Geological Survey of India (GSI)", "duration": "6 months"},
            {"role": "Mining Trainee", "company": "Coal India/Vedanta", "duration": "3 months"},
            {"role": "Environmental Intern", "company": "Consulting Firm", "duration": "4 months"}
        ]
    },
    {
        "topic": "Microbiologist",
        "stream": "Science-B/PCB",
        "aptitude": "Biology, Detail, Lab Work, Methodical",
        "personality": "Patient, Analytical, Precise, Inquisitive",
        "interest": "Bacteria, Viruses, Research, Infectious Diseases",
        "education": "B.Sc. + M.Sc. (Microbiology/Virology)",
        "cost": "Medium",
        "difficulty": "Medium-Hard",
        "description": "Studies microscopic organisms like bacteria, viruses, algae, and fungi, working in healthcare, food science, or research.",
        "fees": "₹1 Lakh - ₹8 Lakh (Total Course)",
        "colleges": [
            "All India Institute of Medical Sciences (AIIMS)", "Christian Medical College (CMC), Vellore", 
            "Jawaharlal Nehru University (JNU)", "University of Delhi", "University of Calcutta", 
            "National Institute of Virology (NIV)", "Manipal Academy of Higher Education",
            "Amity University", "BITS Pilani (Applied Sciences)", "University of Madras"
        ],
        "jobs": [
            "Clinical Microbiologist", "Virologist", "Food Safety Specialist", "Industrial Microbiologist", 
            "Biotechnologist", "Immunologist", "Quality Control Manager", "Research Scientist",
            "Infection Control Officer", "Academic Professor"
        ],
        "internships": [
            {"role": "Lab Technician Trainee", "company": "Diagnostics Lab/Hospital", "duration": "6 months"},
            {"role": "Research Intern", "company": "NIV/ICMR", "duration": "3 months"},
            {"role": "QC Intern", "company": "Food/Pharma Manufacturing Unit", "duration": "4 months"}
        ]
    },
    {
        "topic": "Physiotherapist",
        "stream": "Science-B/PCB",
        "aptitude": "Empathy, Anatomy, Practical, Patience",
        "personality": "Caring, Encouraging, Patient, Hands-on",
        "interest": "Rehabilitation, Sports Medicine, Human Movement",
        "education": "B.P.T. (Bachelor of Physiotherapy)",
        "cost": "Medium",
        "difficulty": "Medium",
        "description": "Helps patients restore function, improve mobility, relieve pain, and prevent permanent physical disabilities through physical exercises and therapy.",
        "fees": "₹2 Lakh - ₹15 Lakh (Total Course)",
        "colleges": [
            "All India Institute of Medical Sciences (AIIMS)", "Christian Medical College (CMC), Vellore", 
            "Manipal College of Health Professions", "Post Graduate Institute of Medical Education and Research (PGIMER)",
            "Jamia Hamdard University", "Guru Gobind Singh Indraprastha University (GGSIPU)", 
            "Apollo College of Physiotherapy", "Indian Spinal Injuries Centre",
            "SRM Institute of Science and Technology", "Various Government Hospitals"
        ],
        "jobs": [
            "Clinical Physiotherapist", "Sports Physiotherapist", "Orthopedic Physiotherapist", "Neurological Physiotherapist", 
            "Pediatric Physiotherapist", "Rehabilitation Specialist", "Ergonomics Consultant", "Fitness Trainer",
            "Academic Lecturer", "Clinic Owner"
        ],
        "internships": [
            {"role": "Clinical Rotations", "company": "Hospital Physiotherapy Dept.", "duration": "Mandatory"},
            {"role": "Sports Intern", "company": "Sports Team/Gym", "duration": "6 months"},
            {"role": "Rehab Trainee", "company": "Specialized Clinic", "duration": "3 months"}
        ]
    },
    {
        "topic": "Ayurvedic Doctor (BAMS)",
        "stream": "Science-B/PCB",
        "aptitude": "Biology, Traditional Medicine, Observation, Patience",
        "personality": "Holistic Thinker, Patient, Dedicated",
        "interest": "Traditional Healing, Herbalism, Wellness",
        "education": "BAMS (Bachelor of Ayurvedic Medicine and Surgery)",
        "cost": "Medium",
        "difficulty": "Hard",
        "description": "Practices traditional Indian medicine (Ayurveda), focusing on holistic wellness through natural herbs, diet, and lifestyle adjustments.",
        "fees": "₹2 Lakh - ₹15 Lakh (Total Course)",
        "colleges": [
            "All India Institute of Ayurveda (AIIA), Delhi", "Banaras Hindu University (BHU)", "Gujarat Ayurved University",
            "National Institute of Ayurveda (NIA), Jaipur", "Ayurveda Mahavidyalaya, Pune", 
            "Tilak Ayurveda Mahavidyalaya, Pune", "Shri Krishna Ayurvedic College, Kurukshetra",
            "Dayanand Ayurvedic College, Jalandhar", "Government Ayurveda College, Trivandrum",
            "Rajiv Gandhi University of Health Sciences"
        ],
        "jobs": [
            "Ayurvedic Practitioner", "Panchakarma Therapist", "Ayurvedic Research Scientist", "Herbal Consultant", 
            "Wellness Coach", "Academic Professor", "Drug Manufacturing Specialist", "Hospital Administrator",
            "Medical Officer (Govt. AYUSH)", "Spa/Wellness Centre Manager"
        ],
        "internships": [
            {"role": "Clinical Internship", "company": "Ayurvedic Hospital", "duration": "1 year (Mandatory)"},
            {"role": "Panchakarma Trainee", "company": "Wellness Centre", "duration": "3 months"},
            {"role": "Research Assistant", "company": "Herbal Drug Lab", "duration": "4 months"}
        ]
    },
    {
        "topic": "Dietitian/Nutritionist",
        "stream": "Science-B/PCB",
        "aptitude": "Biology, Health, Counselling, Communication",
        "personality": "Caring, Motivational, Analytical, Empathetic",
        "interest": "Food Science, Health, Preventative Care",
        "education": "B.Sc. + M.Sc. (Nutrition & Dietetics)",
        "cost": "Medium",
        "difficulty": "Medium",
        "description": "Assesses the nutritional needs of individuals and groups, developing dietary plans to promote health and manage disease.",
        "fees": "₹1 Lakh - ₹10 Lakh (Total Course)",
        "colleges": [
            "Lady Irwin College, DU", "Institute of Home Economics, DU", "Osmania University", "University of Madras",
            "National Institute of Nutrition (NIN), Hyderabad", "Manipal School of Allied Health Sciences", 
            "Mount Carmel College, Bangalore", "SVPU, Meerut",
            "Jamia Hamdard University", "Various Government Colleges"
        ],
        "jobs": [
            "Clinical Dietitian", "Sports Nutritionist", "Public Health Nutritionist", "Food Product Developer", 
            "Wellness Coach (Corporate)", "Academic Lecturer", "Catering/Food Service Manager", "Research Scientist",
            "Private Practitioner/Consultant", "Media Spokesperson (Health)"
        ],
        "internships": [
            {"role": "Clinical Dietitian Intern", "company": "Hospital Kitchen/Wards", "duration": "6 months"},
            {"role": "Wellness Intern", "company": "Corporate Wellness Program", "duration": "3 months"},
            {"role": "Research Assistant", "company": "NIN/Food Lab", "duration": "4 months"}
        ]
    },
    {
        "topic": "Company Secretary (CS)",
        "stream": "Commerce/Any",
        "aptitude": "Corporate Law, Compliance, Detail, Organization",
        "personality": "Ethical, Methodical, Responsible, Organized",
        "interest": "Corporate Governance, Legal Frameworks, Compliance",
        "education": "CS (ICSI) - Foundation, Executive, Professional",
        "cost": "Low (Exam Fees)",
        "difficulty": "Very Hard",
        "description": "Responsible for corporate governance, legal compliance, and administration of a company, ensuring the board's decisions are implemented.",
        "fees": "₹40,000 - ₹1,00,000 (Total CS Course Fees)",
        "colleges": [
            "The Institute of Company Secretaries of India (ICSI)", "Shri Ram College of Commerce (SRCC), Delhi", 
            "Hindu College, Delhi", "Loyola College, Chennai", "Christ University, Bangalore", "St. Xavier's College, Kolkata",
            "Narsee Monjee College of Commerce and Economics, Mumbai", "Presidency College, Chennai", 
            "Hans Raj College, Delhi", "Symbiosis College of Arts and Commerce, Pune"
        ],
        "jobs": [
            "Compliance Officer", "Corporate Governance Specialist", "Legal Advisor (Corporate)", "Board Secretary", 
            "Risk Manager", "Internal Auditor", "Tax Consultant", "Registrar and Share Transfer Agent",
            "Academics", "Financial Reporting Specialist"
        ],
        "internships": [
            {"role": "Article-ship/Trainee", "company": "CA/CS Firm", "duration": "1-3 years (Mandatory)"},
            {"role": "Compliance Intern", "company": "Large Corporate Legal Dept.", "duration": "6 months"},
            {"role": "Legal Trainee", "company": "Boutique Law Firm", "duration": "4 months"}
        ]
    },
    {
        "topic": "Insurance/Actuarial Analyst",
        "stream": "Commerce/Any",
        "aptitude": "Advanced Maths, Risk, Statistics, Analysis",
        "personality": "Analytical, Detail-Oriented, Objective",
        "interest": "Risk Management, Probability, Financial Modeling",
        "education": "B.Sc./B.Com + Actuarial Exams (IAI/Global)",
        "cost": "Medium-High",
        "difficulty": "Very Hard",
        "description": "Uses mathematical and statistical models to assess risk in the insurance and finance industries, determining pricing and reserves.",
        "fees": "₹5 Lakh - ₹20 Lakh (Exams + Coaching)",
        "colleges": [
            "Institute of Actuaries of India (IAI) - Exam Body", "Delhi School of Economics (DSE)", 
            "Indian Statistical Institute (ISI), Kolkata", "BITS Pilani", "Christ University, Bangalore", 
            "St. Stephen's College, DU", "University of Mumbai (Statistics)",
            "Amity University (Actuarial Science)", "University of Delhi (Statistics)", "Madras School of Economics"
        ],
        "jobs": [
            "Actuary (Life/General/Health)", "Risk Analyst", "Pricing Specialist", "Reinsurance Analyst", 
            "Valuation Consultant", "Predictive Modeler", "Data Scientist (Insurance)", "Underwriter",
            "Investment Strategist", "Academic Professor"
        ],
        "internships": [
            {"role": "Actuarial Intern", "company": "HDFC Life/Max Life", "duration": "6 months"},
            {"role": "Risk Analyst Trainee", "company": "General Insurance Firm", "duration": "3 months"},
            {"role": "Pricing Intern", "company": "Reinsurance Broker", "duration": "4 months"}
        ]
    },
    {
        "topic": "Tax Consultant (GST/IT)",
        "stream": "Commerce/Any",
        "aptitude": "Law, Taxation, Detail, Organization",
        "personality": "Ethical, Methodical, Responsible, Client-Facing",
        "interest": "Tax Policy, Accounting, Finance",
        "education": "B.Com + M.Com/CA/CS + Diploma in Taxation Law",
        "cost": "Medium-Low",
        "difficulty": "Hard",
        "description": "Advises individuals and businesses on tax compliance, planning, and minimization strategies (Income Tax, GST, etc.).",
        "fees": "₹1 Lakh - ₹8 Lakh (Total Course)",
        "colleges": [
            "ICAI/ICSI/ICMAI (Certifications)", "Shri Ram College of Commerce (SRCC), Delhi", 
            "Faculty of Law, Delhi University (DU)", "Symbiosis Law School, Pune", 
            "Loyola College, Chennai", "Christ University, Bangalore",
            "Narsee Monjee College of Commerce and Economics, Mumbai", "Presidency College, Chennai", 
            "Hans Raj College, Delhi", "University of Mumbai"
        ],
        "jobs": [
            "Income Tax Advisor", "GST Consultant", "Transfer Pricing Specialist", "International Tax Expert", 
            "Tax Auditor", "Litigation Specialist (Tax Tribunals)", "Financial Planner", "Compliance Officer",
            "Tax Manager (Corporate)", "Academics"
        ],
        "internships": [
            {"role": "Taxation Article-ship", "company": "CA Firm", "duration": "3 years (Mandatory for CA)"},
            {"role": "Tax Intern", "company": "Big 4 Firm (e.g., Deloitte Tax)", "duration": "6 months"},
            {"role": "Compliance Trainee", "company": "Mid-Sized Accounting Firm", "duration": "4 months"}
        ]
    },
    {
        "topic": "Supply Chain Manager",
        "stream": "Commerce/Any",
        "aptitude": "Logistics, Planning, Negotiation, Organization",
        "personality": "Efficient, Decisive, Strategic, Problem-Solver",
        "interest": "Logistics, Manufacturing, Global Trade",
        "education": "B.Tech/Any Grad + MBA (Operations/Supply Chain)",
        "cost": "Medium-High",
        "difficulty": "Medium-Hard",
        "description": "Oversees the entire process of sourcing raw materials, manufacturing products, and delivering them to the consumer efficiently.",
        "fees": "₹5 Lakh - ₹30 Lakh (MBA/PGP)",
        "colleges": [
            "IIM Calcutta", "IIM Bangalore", "XLRI Jamshedpur", "SPJIMR Mumbai", 
            "NITIE Mumbai (now IIM Mumbai)", "Symbiosis Institute of Operations Management (SIOM)",
            "Indian School of Business (ISB)", "BITS Pilani",
            "Delhi Technological University (DTU - MBA)", "Anna University"
        ],
        "jobs": [
            "Logistics Manager", "Procurement Manager", "Inventory Analyst", "Warehouse Manager", 
            "Operations Manager", "Vendor Manager", "Demand Planner", "Quality Control Specialist",
            "Global Supply Chain Director", "ERP/Systems Analyst"
        ],
        "internships": [
            {"role": "Operations Intern", "company": "Amazon/Flipkart", "duration": "6 months"},
            {"role": "Logistics Trainee", "company": "Maruti Suzuki/Hyundai", "duration": "3 months"},
            {"role": "Procurement Intern", "company": "FMCG Company", "duration": "4 months"}
        ]
    },
    {
        "topic": "Real Estate Broker/Consultant",
        "stream": "Commerce/Any",
        "aptitude": "Sales, Negotiation, Market Knowledge, Communication",
        "personality": "Outgoing, Persuasive, Trustworthy, Goal-Oriented",
        "interest": "Property, Finance, Investment, Architecture",
        "education": "BBA/B.Com + Certification/MBA (Real Estate)",
        "cost": "Low (Skill-Based)",
        "difficulty": "Medium-Hard (Commission-Based)",
        "description": "Facilitates the buying, selling, and renting of property, often advising clients on market trends and valuations.",
        "fees": "₹1 Lakh - ₹15 Lakh (Formal Education Optional)",
        "colleges": [
            "RICS School of Built Environment, Amity University", "CEPT University, Ahmedabad (Planning)", 
            "NMIMS Mumbai (Real Estate Management)", "IIM (Executive Programs)", 
            "Symbiosis (Various Management Courses)", "Various Local Real Estate Institutions",
            "College of Engineering, Pune (COEP - Construction Mgmt)", "Anna University",
            "University of Mumbai (Commerce)", "Christ University (Management)"
        ],
        "jobs": [
            "Residential Broker", "Commercial Broker", "Property Consultant", "Valuation Surveyor", 
            "Investment Advisor (Real Estate)", "Leasing Specialist", "Property Manager", "Real Estate Developer",
            "Market Analyst", "Auctioneer"
        ],
        "internships": [
            {"role": "Sales Trainee", "company": "DLF/Godrej Properties", "duration": "6 months"},
            {"role": "Market Research Intern", "company": "JLL/CBRE", "duration": "3 months"},
            {"role": "Property Assistant", "company": "Local Brokerage Firm", "duration": "4 months"}
        ]
    },
    {
        "topic": "Film Director/Cinematographer",
        "stream": "Arts/Any",
        "aptitude": "Visual Storytelling, Leadership, Creativity, Technical Skills",
        "personality": "Visionary, Decisive, High Stress Tolerance, Communicator",
        "interest": "Movies, Photography, Visual Arts, Drama",
        "education": "B.A. / Diploma in Film Making / Mass Comm",
        "cost": "High",
        "difficulty": "Hard (Industry Entry)",
        "description": "The Director guides the creative vision, and the Cinematographer (DOP) is responsible for the look and visual elements of a film/show.",
        "fees": "₹5 Lakh - ₹25 Lakh (Total Course)",
        "colleges": [
            "Film and Television Institute of India (FTII), Pune", "Satyajit Ray Film & Television Institute (SRFTI), Kolkata", 
            "Whistling Woods International (WWI), Mumbai", "Asian Academy of Film & TV (AAFT)",
            "National Institute of Design (NID)", "L.V. Prasad Film & TV Academy", 
            "Annapurna International School of Film & Media", "Amity School of Communication",
            "Delhi University (B.A. Multimedia)", "Christ University (Media)"
        ],
        "jobs": [
            "Director (Film/TV/Web)", "Cinematographer (DOP)", "Assistant Director", "Script Writer", 
            "Film Editor", "Producer", "Gaffer/Lighting Technician", "Colorist",
            "Casting Director", "Visual Effects (VFX) Artist"
        ],
        "internships": [
            {"role": "Assistant Director", "company": "Bollywood/Regional Film Set", "duration": "6-12 months"},
            {"role": "Camera Intern", "company": "Production House", "duration": "3 months"},
            {"role": "Editing Trainee", "company": "Post-Production Studio", "duration": "4 months"}
        ]
    },
    {
        "topic": "Museum Curator",
        "stream": "Arts/Any",
        "aptitude": "History, Research, Public Speaking, Organization",
        "personality": "Methodical, Detail-Oriented, Academic, Communicative",
        "interest": "Art, History, Preservation, Public Education",
        "education": "M.A. (History/Museology) / Ph.D.",
        "cost": "Medium-Low",
        "difficulty": "Medium",
        "description": "Manages a museum's collection, organizes exhibitions, conducts research, and educates the public about historical artifacts or art.",
        "fees": "₹1 Lakh - ₹8 Lakh (Total Post-Grad)",
        "colleges": [
            "National Museum Institute of History of Art, Conservation and Museology (NMI)", "University of Calcutta (Museology)", 
            "Maharaja Sayajirao University of Baroda", "Jawaharlal Nehru University (JNU)",
            "Delhi University (History/Art History)", "Banaras Hindu University (BHU)", 
            "Aligarh Muslim University (AMU)", "Various Art Colleges",
            "Indira Gandhi National Centre for the Arts (IGNCA)", "TISS (Conservation)"
        ],
        "jobs": [
            "Curator (Art/History/Science)", "Collections Manager", "Exhibition Designer", "Archivist", 
            "Conservation Scientist", "Museum Educator", "Gallery Director", "Art Appraiser",
            "Academic Professor", "Heritage Consultant"
        ],
        "internships": [
            {"role": "Collections Intern", "company": "National Museum, Delhi", "duration": "6 months"},
            {"role": "Exhibition Assistant", "company": "Private Art Gallery", "duration": "3 months"},
            {"role": "Archival Trainee", "company": "State Archives", "duration": "4 months"}
        ]
    },
    {
        "topic": "Librarian/Archivist",
        "stream": "Arts/Any",
        "aptitude": "Organization, Research, Patience, Information Management",
        "personality": "Methodical, Calm, Detail-Oriented, Helpful",
        "interest": "Books, Information Systems, Cataloging",
        "education": "B.Lib.I.Sc. + M.Lib.I.Sc. (Library Science)",
        "cost": "Low",
        "difficulty": "Medium",
        "description": "Manages, organizes, and maintains library and archive resources, assisting users with information retrieval and research.",
        "fees": "₹50,000 - ₹5 Lakh (Total Course)",
        "colleges": [
            "Delhi University (Department of Library & Information Science)", "Jawaharlal Nehru University (JNU)", 
            "Banaras Hindu University (BHU)", "Aligarh Muslim University (AMU)", 
            "University of Calcutta", "University of Mumbai", "Madras University",
            "IGNCA (Archival Studies)", "Various State Universities", "IGNOU (Distance Learning)"
        ],
        "jobs": [
            "Academic Librarian", "Public Librarian", "Corporate Archivist", "Digital Librarian", 
            "Metadata Specialist", "Information Scientist", "Records Manager", "Research Assistant",
            "Museum Archivist", "Academics"
        ],
        "internships": [
            {"role": "Cataloging Intern", "company": "University Library", "duration": "6 months"},
            {"role": "Archival Trainee", "company": "National Archives of India", "duration": "3 months"},
            {"role": "Digitalization Assistant", "company": "E-Library Project", "duration": "4 months"}
        ]
    },
    {
        "topic": "Event Manager",
        "stream": "Arts/Any",
        "aptitude": "Planning, Leadership, Communication, Stress Mgt",
        "personality": "Outgoing, Decisive, Organized, Resilient",
        "interest": "Events, Hospitality, Logistics, Networking",
        "education": "Diploma/Degree in Event Management/Hospitality",
        "cost": "Medium",
        "difficulty": "Medium-Hard",
        "description": "Plans, organizes, and executes various events (corporate, weddings, concerts), managing budgets, vendors, and logistics.",
        "fees": "₹3 Lakh - ₹15 Lakh (Total Course)",
        "colleges": [
            "National Institute of Event Management (NIEM)", "Indian Institute of Event Management (IIEM)", 
            "Amity University (Hospitality/Event Mgmt)", "Whistling Woods International", 
            "Symbiosis (Various Management Courses)", "Welingkar Institute of Management",
            "NIIT (Event Management Diplomas)", "Various Hotel Management Institutes",
            "Christ University (Management)", "Mumbai Educational Trust (MET)"
        ],
        "jobs": [
            "Wedding Planner", "Corporate Event Organizer", "Concert/Festival Promoter", "Venue Manager", 
            "Logistics Coordinator", "Sponsorship Manager", "PR Specialist (Events)", "Client Servicing Manager",
            "Event Production Specialist", "Freelance Consultant"
        ],
        "internships": [
            {"role": "Event Coordinator Intern", "company": "Wizcraft/Cineyug", "duration": "6 months"},
            {"role": "Hospitality Trainee", "company": "5-Star Hotel", "duration": "3 months"},
            {"role": "Logistics Assistant", "company": "Local Event Company", "duration": "4 months"}
        ]
    },
    {
        "topic": "Urban Planner",
        "stream": "Arts/Science/Any",
        "aptitude": "Policy, Design, Data Analysis, Systems Thinking",
        "personality": "Strategic, Analytical, Visionary, Communicative",
        "interest": "City Design, Infrastructure, Sustainability",
        "education": "B.Arch/B.Tech + M.Plan (Urban Planning)",
        "cost": "Medium-High",
        "difficulty": "Medium-Hard",
        "description": "Develops plans and policies for the use of land and resources, focusing on the future growth and sustainability of cities and towns.",
        "fees": "₹4 Lakh - ₹20 Lakh (Total Course)",
        "colleges": [
            "School of Planning and Architecture (SPA), Delhi", "IIT Kharagpur", "CEPT University, Ahmedabad",
            "NIT Calicut", "Anna University (M.Plan)", "Jadavpur University", 
            "Maharaja Sayajirao University of Baroda", "School of Architecture, Mumbai",
            "Indian Institute of Science (IISc - Sustainable Planning)", "CEPT University (Planning)"
        ],
        "jobs": [
            "City Planner", "Transportation Planner", "Land Use Analyst", "Policy Consultant", 
            "GIS Specialist", "Zoning Administrator", "Environmental Planner", "Housing Developer",
            "Community Development Specialist", "Academic Professor"
        ],
        "internships": [
            {"role": "Planning Intern", "company": "Local Municipal Corporation/Development Authority", "duration": "6 months"},
            {"role": "Research Assistant", "company": "Urban Think Tank/NGO", "duration": "3 months"},
            {"role": "GIS Analyst Trainee", "company": "Consulting Firm", "duration": "4 months"}
        ]
    },
    {
        "topic": "Teacher/Professor",
        "stream": "Arts/Science/Commerce/Any",
        "aptitude": "Communication, Patience, Subject Expert, Empathy",
        "personality": "Patient, Enthusiastic, Inspiring, Ethical",
        "interest": "Education, Subject Research, Mentoring",
        "education": "B.Ed. (School) / NET/Ph.D. (College)",
        "cost": "Medium",
        "difficulty": "Medium-Hard (NET/Ph.D.)",
        "description": "Educates students at various levels (school, college, university) in a specialized subject, often conducting research (Professor).",
        "fees": "₹1 Lakh - ₹10 Lakh (Total Course)",
        "colleges": [
            "Delhi University (B.Ed/M.Ed)", "Jawaharlal Nehru University (JNU)", "University of Hyderabad", 
            "Banaras Hindu University (BHU)", "All National/State Universities", 
            "Tata Institute of Social Sciences (TISS)", "Amity University (Education)",
            "IGNOU (Distance Learning)", "Regional Institute of Education (NCERT)", "Christ University"
        ],
        "jobs": [
            "School Teacher (PGT/TGT)", "University Assistant Professor", "Research Fellow", "Academic Dean", 
            "Curriculum Designer", "Educational Consultant", "Tutor (Private/Online)", "Content Developer (EdTech)",
            "School Principal/Administrator", "Education Policy Analyst"
        ],
        "internships": [
            {"role": "Teaching Practice", "company": "Local School", "duration": "Mandatory"},
            {"role": "Research Assistant", "company": "University Department", "duration": "6 months"},
            {"role": "Content Creation Intern", "company": "EdTech Startup", "duration": "3 months"}
        ]
    },
    # --- Remaining 24 entries to complete the 50 total ---
    {
        "topic": "Chemical Engineer",
        "stream": "Science-A/PCM",
        "aptitude": "Chemistry, Physics, Process Design, Math",
        "personality": "Methodical, Analytical, Detail-Oriented",
        "interest": "Industrial Processes, Manufacturing, Pharmaceuticals",
        "education": "B.Tech/BE (Chemical)",
        "cost": "Medium-High",
        "difficulty": "Hard",
        "description": "Designs industrial processes to transform raw materials into useful products in a cost-effective and safe manner.",
        "fees": "₹4 Lakh - ₹20 Lakh (Total Course)",
        "colleges": [
            "IIT Bombay", "IIT Madras", "Institute of Chemical Technology (ICT), Mumbai", "BITS Pilani",
            "NIT Trichy", "Anna University", "Jadavpur University", "University of Calcutta",
            "College of Engineering, Pune (COEP)", "VIT Vellore"
        ],
        "jobs": [
            "Process Engineer", "R&D Scientist", "Plant Manager", "Quality Control Manager", 
            "Environmental Engineer", "Biochemical Engineer", "Polymer Scientist", "Safety Engineer",
            "Design Consultant", "Field Engineer"
        ],
        "internships": [
            {"role": "Process Intern", "company": "Reliance Industries", "duration": "6 months"},
            {"role": "R&D Trainee", "company": "Dr. Reddy's Labs", "duration": "3 months"},
            {"role": "Plant Intern", "company": "Manufacturing Unit", "duration": "4 months"}
        ]
    },
    {
        "topic": "Industrial Designer",
        "stream": "Science-A/PCM/Arts/Any",
        "aptitude": "Creativity, Drawing, Ergonomics, Technical",
        "personality": "Innovative, Practical, User-Focused",
        "interest": "Product Design, Aesthetics, Manufacturing",
        "education": "B.Des (Industrial Design)",
        "cost": "High",
        "difficulty": "Medium",
        "description": "Designs everyday manufactured products (cars, electronics, furniture) based on user needs and production feasibility.",
        "fees": "₹6 Lakh - ₹30 Lakh (Total Course)",
        "colleges": [
            "National Institute of Design (NID), Ahmedabad", "Industrial Design Centre (IDC), IIT Bombay", 
            "NIFT", "Symbiosis Institute of Design (SID)", "Pearl Academy", 
            "Srishti Institute of Art, Design and Technology", "MIT Institute of Design",
            "IICD Jaipur", "CEPT University", "Amity School of Design"
        ],
        "jobs": [
            "Product Designer", "Automotive Designer", "Furniture Designer", "Packaging Designer", 
            "Toy Designer", "UI/UX Designer", "Design Consultant", "Design Researcher",
            "CAD Specialist", "Art Director"
        ],
        "internships": [
            {"role": "Design Intern", "company": "Tata Motors/Tech MNC", "duration": "6 months"},
            {"role": "R&D Trainee", "company": "Electronics Company", "duration": "3 months"},
            {"role": "Design Assistant", "company": "Startup", "duration": "4 months"}
        ]
    },
    {
        "topic": "Environmental Scientist",
        "stream": "Science-B/PCB/Any",
        "aptitude": "Biology, Chemistry, Ecology, Data Analysis",
        "personality": "Ethical, Observant, Analytical, Fieldwork Ready",
        "interest": "Pollution, Conservation, Climate Change",
        "education": "B.Sc. + M.Sc. (Environmental Science)",
        "cost": "Medium",
        "difficulty": "Medium",
        "description": "Studies the environment and human impact on it, working to solve pollution problems and manage natural resources sustainably.",
        "fees": "₹1 Lakh - ₹8 Lakh (Total Course)",
        "colleges": [
            "Jawaharlal Nehru University (JNU)", "Indian Institute of Science (IISc), Bangalore", 
            "TERI School of Advanced Studies", "University of Delhi", "Banaras Hindu University (BHU)",
            "Anna University", "IITs/NITs (Environmental Engg)",
            "University of Calcutta", "Manipal Academy", "Various Agricultural Universities"
        ],
        "jobs": [
            "Environmental Consultant", "Conservation Scientist", "Pollution Control Officer", "Waste Management Specialist", 
            "Hydrologist", "Policy Analyst", "Ecology Researcher", "Sustainability Manager (Corporate)",
            "Academic Professor", "Field Technician"
        ],
        "internships": [
            {"role": "Field Research Intern", "company": "CSIR Labs", "duration": "6 months"},
            {"role": "Sustainability Trainee", "company": "MNC/NGO", "duration": "3 months"},
            {"role": "Policy Assistant", "company": "Government/Think Tank", "duration": "4 months"}
        ]
    },
    {
        "topic": "Forensic Scientist",
        "stream": "Science-B/PCB/Any",
        "aptitude": "Chemistry, Biology, Detail, Logic",
        "personality": "Methodical, Objective, Patient, Ethical",
        "interest": "Crime Analysis, Lab Work, Law",
        "education": "B.Sc. + M.Sc. (Forensic Science)",
        "cost": "Medium",
        "difficulty": "Hard",
        "description": "Applies scientific methods and techniques to analyze crime scene evidence for use in legal proceedings.",
        "fees": "₹2 Lakh - ₹10 Lakh (Total Course)",
        "colleges": [
            "Gujarat Forensic Sciences University (GFSU)", "LNJN National Institute of Criminology and Forensic Science", 
            "Osmania University", "Punjabi University, Patiala", "Amity University (Forensic Science)", 
            "University of Delhi (Science Dept)", "AIIMS (Toxicology)",
            "Jain University", "Manipal Academy", "Various State Universities"
        ],
        "jobs": [
            "Crime Scene Investigator (CSI)", "Forensic Chemist", "Ballistics Expert", "Forensic Biologist", 
            "Document Analyst", "Cyber Forensic Specialist", "Toxicologist", "Fingerprint Expert",
            "Academic Professor", "Expert Witness"
        ],
        "internships": [
            {"role": "Lab Intern", "company": "Forensic Science Lab (FSL)", "duration": "6 months"},
            {"role": "CSI Trainee", "company": "Police Department", "duration": "3 months"},
            {"role": "Research Assistant", "company": "University Lab", "duration": "4 months"}
        ]
    },
    {
        "topic": "Zoologist/Botantist",
        "stream": "Science-B/PCB",
        "aptitude": "Biology, Observation, Research, Fieldwork",
        "personality": "Patient, Inquisitive, Detail-Oriented",
        "interest": "Animal/Plant Life, Ecology, Conservation",
        "education": "B.Sc. + M.Sc. (Zoology/Botany)",
        "cost": "Low-Medium",
        "difficulty": "Medium",
        "description": "Studies animals or plants in their natural habitats and labs to understand their structure, function, and relationship with the environment.",
        "fees": "₹1 Lakh - ₹5 Lakh (Total Course)",
        "colleges": [
            "Jawaharlal Nehru University (JNU)", "University of Delhi", "Indian Institute of Science (IISc), Bangalore", 
            "Madras Christian College (MCC)", "Banaras Hindu University (BHU)",
            "Aligarh Muslim University (AMU)", "Centre for Cellular and Molecular Biology (CCMB)",
            "University of Calcutta", "Christ University", "Osmania University"
        ],
        "jobs": [
            "Wildlife Biologist", "Taxonomist", "Ecology Consultant", "Conservation Scientist", 
            "Botanical Survey of India Officer", "Zoo/Museum Curator", "Academic Professor", "Pharmaceutical Researcher",
            "Horticulturist", "Field Researcher (Govt/NGO)"
        ],
        "internships": [
            {"role": "Field Research Intern", "company": "Forest Department/NGO", "duration": "6 months"},
            {"role": "Lab Assistant", "company": "University Research Lab", "duration": "3 months"},
            {"role": "Data Analyst Trainee", "company": "Conservation Project", "duration": "4 months"}
        ]
    },
    {
        "topic": "Hospitality Manager",
        "stream": "Commerce/Arts/Any",
        "aptitude": "Communication, Leadership, Customer Service, Organization",
        "personality": "Outgoing, Patient, Problem-Solver, Team Leader",
        "interest": "Hotels, Tourism, Service Industry",
        "education": "BHM (Bachelor of Hotel Management)",
        "cost": "Medium-High",
        "difficulty": "Medium",
        "description": "Manages operations in hotels, resorts, or restaurants, ensuring high levels of customer satisfaction and efficient service delivery.",
        "fees": "₹4 Lakh - ₹15 Lakh (Total Course)",
        "colleges": [
            "Institute of Hotel Management (IHM) - various branches", "Welcomegroup Graduate School of Hotel Administration, Manipal", 
            "Oberoi Centre of Learning and Development (OCLD)", "Army Institute of Hotel Management and Catering Technology",
            "Christ University", "Amity School of Hospitality", 
            "IIHM - various campuses", "Banasthali Vidyapith",
            "Jain University", "Rizvi College of Hotel Management"
        ],
        "jobs": [
            "Hotel Manager (General/Dept)", "Restaurant Manager", "Front Office Manager", "Food & Beverage Manager", 
            "Sales & Marketing Manager (Hotel)", "Catering Specialist", "Event Manager", "Cruise Ship Manager",
            "Client Relations Specialist", "Tourism Operator"
        ],
        "internships": [
            {"role": "F&B Trainee", "company": "Taj/Oberoi Hotel", "duration": "6 months (Mandatory)"},
            {"role": "Front Office Intern", "company": "Luxury Resort", "duration": "3 months"},
            {"role": "Events Assistant", "company": "Hospitality Firm", "duration": "4 months"}
        ]
    },
    {
        "topic": "Auditor (Internal/External)",
        "stream": "Commerce/Any",
        "aptitude": "Detail, Logic, Accounts, Ethics",
        "personality": "Methodical, Objective, Skeptical, Ethical",
        "interest": "Compliance, Financial Statements, Risk",
        "education": "B.Com + CA/CPA/M.Com/MBA (Audit)",
        "cost": "Low-Medium",
        "difficulty": "Hard (CA Exams)",
        "description": "Examines an organization's financial records to ensure they are accurate, fair, and compliant with laws and regulations.",
        "fees": "₹1 Lakh - ₹15 Lakh (Varies on qualification)",
        "colleges": [
            "ICAI (CA Qualification)", "Shri Ram College of Commerce (SRCC), Delhi", 
            "Christ University, Bangalore", "Loyola College, Chennai", 
            "Narsee Monjee College of Commerce and Economics, Mumbai", "Hans Raj College, Delhi",
            "Presidency College, Chennai", "Symbiosis College of Arts and Commerce, Pune", 
            "IIM/FMS (MBA in Finance)", "University of Mumbai"
        ],
        "jobs": [
            "Statutory Auditor", "Internal Auditor", "Tax Auditor", "IT Auditor", 
            "Forensic Auditor", "Risk Consultant", "Compliance Officer", "CFO",
            "Audit Manager (Big 4)", "Government Auditor"
        ],
        "internships": [
            {"role": "Audit Article-ship", "company": "Big 4 Firm (e.g., EY/PwC)", "duration": "3 years (Mandatory)"},
            {"role": "Internal Audit Intern", "company": "Large Corporate", "duration": "6 months"},
            {"role": "Compliance Trainee", "company": "Financial Institution", "duration": "4 months"}
        ]
    },
    {
        "topic": "Public Relations (PR) Specialist",
        "stream": "Arts/Any",
        "aptitude": "Communication, Writing, Networking, Crisis Mgt",
        "personality": "Outgoing, Persuasive, Trustworthy, Quick Thinker",
        "interest": "Media, Branding, Public Image",
        "education": "B.A. + M.A. (Mass Comm/PR)",
        "cost": "Medium",
        "difficulty": "Medium",
        "description": "Manages the public image and reputation of a company or individual, often dealing with media relations and crisis communications.",
        "fees": "₹2 Lakh - ₹10 Lakh (Total Course)",
        "colleges": [
            "Indian Institute of Mass Communication (IIMC), Delhi", "Xavier Institute of Communications (XIC), Mumbai", 
            "Mudra Institute of Communications (MICA)", "Symbiosis Institute of Media and Communication (SIMC)",
            "Delhi University (various colleges)", "Christ University", 
            "Pearl Academy (Media)", "Amity School of Communication",
            "Manipal Institute of Communication", "Makhanlal Chaturvedi National University"
        ],
        "jobs": [
            "Media Relations Manager", "Publicist", "Crisis Communicator", "Corporate Communications Specialist", 
            "Brand Manager (PR Focus)", "Social Media Manager", "Event Publicist", "Content Strategist",
            "Lobbyist/Govt Liaison", "Freelance Consultant"
        ],
        "internships": [
            {"role": "PR Intern", "company": "Edelman/Weber Shandwick", "duration": "6 months"},
            {"role": "Media Assistant", "company": "Corporate Communications Dept.", "duration": "3 months"},
            {"role": "Social Media Trainee", "company": "Digital Agency", "duration": "4 months"}
        ]
    },
    {
        "topic": "Renewable Energy Engineer",
        "stream": "Science-A/PCM",
        "aptitude": "Physics, Design, Systems Integration, Math",
        "personality": "Sustainable, Innovative, Problem-Solver",
        "interest": "Solar, Wind, Geothermal, Energy Policy",
        "education": "B.Tech/BE (Electrical/Mechanical) + M.Tech (Renewable Energy)",
        "cost": "Medium-High",
        "difficulty": "Hard",
        "description": "Focuses on designing, developing, and deploying sustainable energy systems such as solar, wind, and hydro power.",
        "fees": "₹4 Lakh - ₹25 Lakh (Total Course)",
        "colleges": [
            "IIT Delhi", "IIT Kharagpur", "NIT Trichy", "The Energy and Resources Institute (TERI)", 
            "University of Petroleum and Energy Studies (UPES)", "Anna University", 
            "BITS Pilani", "Manipal Institute of Technology",
            "Jadavpur University", "VIT Vellore"
        ],
        "jobs": [
            "Solar Energy System Designer", "Wind Turbine Engineer", "Energy Auditor", "Project Manager (Solar Farms)", 
            "Sustainability Consultant", "R&D Scientist", "Policy Analyst (Energy)", "Environmental Engineer",
            "Installation Supervisor", "Business Development Manager"
        ],
        "internships": [
            {"role": "Project Intern", "company": "Tata Power Solar", "duration": "6 months"},
            {"role": "Energy Audit Trainee", "company": "Consulting Firm", "duration": "3 months"},
            {"role": "R&D Intern", "company": "University Lab", "duration": "4 months"}
        ]
    },
    {
        "topic": "Robotics Engineer",
        "stream": "Science-A/PCM",
        "aptitude": "Maths, Coding, Mechanical Systems, AI",
        "personality": "Innovative, Problem-Solver, Interdisciplinary",
        "interest": "Automation, AI, Machine Design",
        "education": "B.Tech/BE (Robotics/Mechatronics/CS)",
        "cost": "High",
        "difficulty": "Hard",
        "description": "Designs, builds, programs, and tests robots and robotic systems used in manufacturing, medicine, or research.",
        "fees": "₹5 Lakh - ₹25 Lakh (Total Course)",
        "colleges": [
            "IIT Madras", "IIT Kanpur", "BITS Pilani", "Vellore Institute of Technology (VIT)", 
            "PEC Chandigarh", "Manipal Institute of Technology", 
            "Anna University", "University of Hyderabad",
            "College of Engineering, Pune (COEP)", "IIIT Hyderabad"
        ],
        "jobs": [
            "Robotics Programmer", "Automation Engineer", "Control Systems Engineer", "Machine Vision Specialist", 
            "AI/ML Engineer", "Design Engineer", "Field Service Technician", "R&D Scientist",
            "Mechatronics Engineer", "Surgical Robotics Specialist"
        ],
        "internships": [
            {"role": "R&D Intern", "company": "TCS/Infosys Labs", "duration": "6 months"},
            {"role": "Automation Trainee", "company": "Manufacturing Plant", "duration": "3 months"},
            {"role": "Programming Intern", "company": "AI Startup", "duration": "4 months"}
        ]
    },
    {
        "topic": "Biomedical Engineer",
        "stream": "Science-B/PCB/PCM",
        "aptitude": "Biology, Engineering, Problem-Solver, Design",
        "personality": "Innovative, Ethical, Analytical",
        "interest": "Medical Devices, Prosthetics, Healthcare Tech",
        "education": "B.Tech/BE (Biomedical Engineering)",
        "cost": "Medium-High",
        "difficulty": "Hard",
        "description": "Combines engineering principles with medical sciences to design and create equipment, devices, and computer systems used in healthcare.",
        "fees": "₹4 Lakh - ₹20 Lakh (Total Course)",
        "colleges": [
            "IIT Madras", "IIT Bombay", "All India Institute of Medical Sciences (AIIMS)", "Manipal Institute of Technology", 
            "Anna University", "BITS Pilani", "VIT Vellore", 
            "Amity University", "Indian Institute of Science (IISc)", "Jadavpur University"
        ],
        "jobs": [
            "Medical Device Designer", "Clinical Engineer", "Rehabilitation Engineer", "Bioinstrumentation Specialist", 
            "Biomaterials Engineer", "Quality Assurance Engineer", "Research Scientist", "Sales/Service Engineer (Medical)",
            "Prosthetics Specialist", "Regulatory Affairs Officer"
        ],
        "internships": [
            {"role": "Design Intern", "company": "Medical Device Company", "duration": "6 months"},
            {"role": "Clinical Trainee", "company": "Hospital Bio-Engineering Dept.", "duration": "3 months"},
            {"role": "R&D Intern", "company": "University Lab", "duration": "4 months"}
        ]
    },
    {
        "topic": "Food Scientist",
        "stream": "Science-B/PCB/Any",
        "aptitude": "Chemistry, Biology, Detail, Process Control",
        "personality": "Methodical, Innovative, Quality-Focused",
        "interest": "Food Quality, Nutrition, Food Processing",
        "education": "B.Sc./B.Tech + M.Sc./M.Tech (Food Technology)",
        "cost": "Medium",
        "difficulty": "Medium",
        "description": "Applies scientific principles to the study of food processing, preservation, quality control, and improvement of nutritional value.",
        "fees": "₹2 Lakh - ₹15 Lakh (Total Course)",
        "colleges": [
            "CFTRI, Mysore", "Institute of Chemical Technology (ICT), Mumbai", "Punjab Agricultural University", 
            "GB Pant University of Agriculture and Technology", "Anna University", 
            "Jadavpur University", "National Institute of Nutrition (NIN)",
            "Amity University", "Manipal Academy", "Various Agricultural Universities"
        ],
        "jobs": [
            "Food Technologist", "Quality Assurance Specialist", "Product Development Scientist", "Flavorist", 
            "Food Safety Auditor", "Sensory Scientist", "R&D Specialist", "Regulatory Affairs Officer",
            "Academic Professor", "Food Inspector (Govt)"
        ],
        "internships": [
            {"role": "QC Intern", "company": "Nestle/HUL", "duration": "6 months"},
            {"role": "R&D Trainee", "company": "Food Processing Unit", "duration": "3 months"},
            {"role": "Process Intern", "company": "Dairy/Beverage Plant", "duration": "4 months"}
        ]
    },
    {
        "topic": "Forester/Wildlife Manager",
        "stream": "Science-B/PCB/Any",
        "aptitude": "Biology, Fieldwork, Observation, Management",
        "personality": "Resilient, Dedicated, Ethical, Practical",
        "interest": "Forests, Wildlife, Conservation, Fieldwork",
        "education": "B.Sc. (Forestry) / Indian Forest Service (IFS)",
        "cost": "Medium",
        "difficulty": "Hard (IFS Exam)",
        "description": "Manages natural resources in forests, parks, and protected areas, focusing on conservation, wildlife population control, and sustainability.",
        "fees": "₹1 Lakh - ₹8 Lakh (Total Course)",
        "colleges": [
            "Forest Research Institute (FRI), Dehradun", "Various Agricultural Universities (Forestry Dept)", 
            "Wildlife Institute of India (WII)", "Indian Institute of Forest Management (IIFM), Bhopal",
            "Jawaharlal Nehru University (JNU - Ecology)", "University of Delhi", 
            "Anna University", "Banaras Hindu University (BHU)",
            "University of Calcutta", "IGNOU (Distance Learning)"
        ],
        "jobs": [
            "Indian Forest Service Officer (IFS)", "Wildlife Biologist", "Park Ranger/Manager", "Conservation Scientist", 
            "Ecotourism Specialist", "Environmental Consultant", "Policy Analyst", "Research Fellow",
            "Academic Professor", "Forest Pathologist"
        ],
        "internships": [
            {"role": "Field Intern", "company": "Local Forest Division", "duration": "6 months"},
            {"role": "Research Assistant", "company": "WII/NGO", "duration": "3 months"},
            {"role": "Ecotourism Trainee", "company": "Private Resort/Govt.", "duration": "4 months"}
        ]
    },
    {
        "topic": "Chartered Financial Analyst (CFA)",
        "stream": "Commerce/Any",
        "aptitude": "Advanced Finance, Ethics, Analysis, Logic",
        "personality": "Methodical, Highly Analytical, Ethical, High Stamina",
        "interest": "Investing, Portfolio Management, Wealth",
        "education": "Any Grad + CFA Program (3 levels)",
        "cost": "Medium-High (Exam Fees)",
        "difficulty": "Very Hard",
        "description": "A globally recognized qualification specializing in investment management, financial analysis, and portfolio strategy.",
        "fees": "₹5 Lakh - ₹15 Lakh (Total Cost of Exams and Coaching)",
        "colleges": [
            "CFA Institute (Global Body)", "IIM/ISB (MBA Background Helpful)", "NMIMS Mumbai", "FMS Delhi",
            "Shri Ram College of Commerce (SRCC), Delhi", "Christ University, Bangalore", 
            "Loyola College, Chennai", "St. Xavier's College, Kolkata",
            "Indian Institute of Capital Markets", "Various Private Institutes for Coaching"
        ],
        "jobs": [
            "Portfolio Manager", "Equity Research Analyst", "Wealth Manager", "Chief Investment Officer (CIO)", 
            "Hedge Fund Analyst", "Risk Manager", "Financial Planner", "Credit Analyst",
            "Investment Banker", "Academic Professor (Finance)"
        ],
        "internships": [
            {"role": "Research Analyst Intern", "company": "Edelweiss/Motilal Oswal", "duration": "6 months"},
            {"role": "Portfolio Assistant", "company": "Asset Management Company (AMC)", "duration": "3 months"},
            {"role": "Credit Analyst Trainee", "company": "Rating Agency (e.g., CRISIL)", "duration": "4 months"}
        ]
    },
    {
        "topic": "Risk Manager",
        "stream": "Commerce/Any",
        "aptitude": "Statistics, Logic, Finance, Policy",
        "personality": "Objective, Analytical, Cautious, Strategic",
        "interest": "Financial Markets, Compliance, Predictive Analysis",
        "education": "B.Com/B.Tech + MBA (Finance) / FRM Certification",
        "cost": "Medium-High",
        "difficulty": "Hard",
        "description": "Identifies, assesses, and controls threats to an organization's earnings and capital. Critical in banking and finance sectors.",
        "fees": "₹5 Lakh - ₹25 Lakh (Total Course)",
        "colleges": [
            "IIM Ahmedabad", "IIM Bangalore", "Indian School of Business (ISB)", "FMS Delhi", 
            "NMIMS Mumbai", "XLRI Jamshedpur", "SPJIMR Mumbai", "BITS Pilani",
            "Delhi Technological University (DTU - MBA)", "University of Mumbai"
        ],
        "jobs": [
            "Credit Risk Analyst", "Market Risk Manager", "Operational Risk Manager", "Compliance Officer", 
            "Financial Analyst", "Internal Auditor", "Quantitative Analyst", "Treasury Manager",
            "Chief Risk Officer (CRO)", "Insurance Underwriter"
        ],
        "internships": [
            {"role": "Risk Analyst Intern", "company": "HDFC Bank/ICICI Bank", "duration": "6 months"},
            {"role": "Compliance Trainee", "company": "Financial Institution", "duration": "3 months"},
            {"role": "Quant Intern", "company": "Investment Bank", "duration": "4 months"}
        ]
    },
    {
        "topic": "Ethical Hacker/Cyber Security",
        "stream": "Science-A/PCM",
        "aptitude": "Coding, Logic, Problem-Solver, Detail",
        "personality": "Inquisitive, Patient, Methodical, Ethical",
        "interest": "Networking, Systems, Hacking, Data Protection",
        "education": "B.Tech/BE (CS/IT) + CEH/CISSP Certification",
        "cost": "Medium-High",
        "difficulty": "Hard",
        "description": "Protects computer systems and networks from threats by proactively identifying vulnerabilities and exploiting them (ethically).",
        "fees": "₹4 Lakh - ₹20 Lakh (Total Course)",
        "colleges": [
            "IIT Madras", "IIIT Hyderabad", "NIT Trichy", "BITS Pilani",
            "CDAC (Advanced Diplomas)", "Delhi Technological University (DTU)", 
            "Anna University", "VIT Vellore",
            "Manipal Academy", "Amity University (Cyber Security)"
        ],
        "jobs": [
            "Security Analyst", "Penetration Tester", "Chief Information Security Officer (CISO)", "Security Architect", 
            "Forensic Investigator", "Vulnerability Researcher", "Cryptographer", "Security Auditor",
            "Incident Responder", "Threat Intelligence Analyst"
        ],
        "internships": [
            {"role": "Security Intern", "company": "TCS/Infosys/Wipro", "duration": "6 months"},
            {"role": "Pen Testing Trainee", "company": "Cyber Security Firm", "duration": "3 months"},
            {"role": "Incident Response Intern", "company": "Financial Institution", "duration": "4 months"}
        ]
    },
    {
        "topic": "Product Manager",
        "stream": "Commerce/Science/Any",
        "aptitude": "Communication, Logic, Strategy, Market Knowledge",
        "personality": "Leader, Visionary, Empathetic (User focus), Decisive",
        "interest": "Technology, Business Strategy, User Experience",
        "education": "B.Tech/Any Grad + MBA (Strategy/Marketing)",
        "cost": "High",
        "difficulty": "Hard",
        "description": "Defines the 'why,' 'what,' and 'when' of the product that the engineering team builds. It’s the intersection of business, technology, and user experience.",
        "fees": "₹5 Lakh - ₹30 Lakh (MBA/PGP)",
        "colleges": [
            "IIM Ahmedabad", "IIM Bangalore", "Indian School of Business (ISB)", "FMS Delhi", 
            "NMIMS Mumbai", "XLRI Jamshedpur", "SPJIMR Mumbai", "BITS Pilani (Management)",
            "IIIT Hyderabad", "IITs (Management Studies)"
        ],
        "jobs": [
            "Associate Product Manager (APM)", "Product Manager (PM)", "Group Product Manager", "VP of Product", 
            "Product Marketing Manager (PMM)", "UX Researcher", "Data Analyst (Product Focus)", "Strategy Consultant",
            "Business Analyst", "Technical Program Manager"
        ],
        "internships": [
            {"role": "APM Intern", "company": "Google/Microsoft/Amazon", "duration": "10 weeks"},
            {"role": "Product Intern", "company": "Startup", "duration": "6 months"},
            {"role": "Business Analyst Trainee", "company": "MNC Tech Firm", "duration": "4 months"}
        ]
    },
    {
        "topic": "Urban Designer (Public Spaces)",
        "stream": "Arts/Science/Any",
        "aptitude": "Design, Policy, Aesthetics, Visualization",
        "personality": "Collaborative, Creative, Strategic, Public-Focused",
        "interest": "City Aesthetics, Placemaking, Community Building",
        "education": "B.Arch/B.Plan + M.Arch/M.Des (Urban Design)",
        "cost": "Medium-High",
        "difficulty": "Medium",
        "description": "Focuses on the arrangement, appearance, and function of public spaces in cities, bridging architecture and urban planning.",
        "fees": "₹5 Lakh - ₹20 Lakh (Total Course)",
        "colleges": [
            "School of Planning and Architecture (SPA), Delhi", "CEPT University, Ahmedabad", "IIT Kharagpur",
            "NIT Calicut", "Sir JJ College of Architecture, Mumbai", 
            "Anna University", "Jadavpur University", "NID, Gandhinagar",
            "SPA Vijayawada", "School of Architecture, Mumbai"
        ],
        "jobs": [
            "Urban Designer", "Landscape Architect", "Master Planner", "Design Reviewer", 
            "Policy Consultant", "GIS Specialist", "Community Engagement Specialist", "Architect",
            "Academic Professor", "Sustainability Consultant"
        ],
        "internships": [
            {"role": "Design Intern", "company": "Architecture/Planning Firm", "duration": "6 months"},
            {"role": "Research Assistant", "company": "Think Tank/University", "duration": "3 months"},
            {"role": "Project Assistant", "company": "Development Authority", "duration": "4 months"}
        ]
    },
    {
        "topic": "Journalist (Investigative)",
        "stream": "Arts/Any",
        "aptitude": "Research, Skepticism, Writing, Persistence",
        "personality": "Curious, Resilient, Ethical, Detail-Oriented",
        "interest": "Current Affairs, Justice, Public Policy",
        "education": "BA/BJMC + M.A. (Journalism)",
        "cost": "Medium",
        "difficulty": "Hard",
        "description": "Deeply researches a single topic of public interest, often exposing illegal activities, corruption, or hidden truths.",
        "fees": "₹1 Lakh - ₹8 Lakh (Total Course)",
        "colleges": [
            "Indian Institute of Mass Communication (IIMC), Delhi", "Asian College of Journalism (ACJ), Chennai", 
            "Xavier Institute of Communications (XIC), Mumbai", "Symbiosis Institute of Media and Communication (SIMC)",
            "Delhi University (various colleges)", "Christ University", 
            "Manipal Institute of Communication", "Mudra Institute of Communications (MICA)",
            "Makhanlal Chaturvedi National University", "Amity School of Communication"
        ],
        "jobs": [
            "Investigative Reporter", "Editor", "Data Journalist", "Documentary Filmmaker", 
            "War Correspondent", "Freelance Writer", "Fact Checker", "Public Policy Analyst",
            "Academic Professor", "Media Law Expert"
        ],
        "internships": [
            {"role": "Research Intern", "company": "The Indian Express/The Hindu", "duration": "6 months"},
            {"role": "Data Analyst Trainee", "company": "News Organization", "duration": "3 months"},
            {"role": "Field Assistant", "company": "NGO/News Channel", "duration": "4 months"}
        ]
    },
    {
        "topic": "Linguistics/Cognitive Scientist",
        "stream": "Arts/Science/Any",
        "aptitude": "Language, Logic, Philosophy, Research",
        "personality": "Intellectual, Analytical, Methodical",
        "interest": "How the mind works, Language Structure, AI",
        "education": "M.A. (Linguistics) / M.Sc. (Cognitive Science)",
        "cost": "Medium-Low",
        "difficulty": "Hard",
        "description": "Studies the nature of human language, thought, and intelligence, often working at the intersection of psychology, computer science, and philosophy.",
        "fees": "₹1 Lakh - ₹10 Lakh (Total Post-Grad/Ph.D.)",
        "colleges": [
            "Jawaharlal Nehru University (JNU)", "University of Hyderabad", "Indian Institute of Technology (IIT) Delhi (Cognitive Science)", 
            "University of Delhi", "Indian Institute of Science (IISc), Bangalore", 
            "Centre for Cognitive Science, IIT Kanpur", "University of Calcutta", "BITS Pilani",
            "Manipal Academy", "Various Liberal Arts Colleges"
        ],
        "jobs": [
            "NLP (Natural Language Processing) Specialist", "UX Writer", "Computational Linguist", "AI Researcher", 
            "Language Acquisition Specialist", "Academic Professor", "Speech Therapist", "Translator (Specialized)",
            "Psycholinguist", "Machine Learning Engineer (NLP)"
        ],
        "internships": [
            {"role": "Research Fellow", "company": "University Cognitive Lab", "duration": "6 months"},
            {"role": "NLP Intern", "company": "Tech Company", "duration": "3 months"},
            {"role": "Linguistics Trainee", "company": "Dictionary/Translation Service", "duration": "4 months"}
        ]
    },
    {
        "topic": "Choreographer/Dancer",
        "stream": "Arts/Any",
        "aptitude": "Creativity, Physical Stamina, Rhythm, Teaching",
        "personality": "Passionate, Disciplined, Expressive, Resilient",
        "interest": "Dance, Performance, Music, Culture",
        "education": "Diploma/Degree in Dance/Performing Arts",
        "cost": "Low (Skill-Based)",
        "difficulty": "Hard (Physically and Career Stability)",
        "description": "Creates and arranges sequences of movements for dances, and teaches others for stage, film, or competition.",
        "fees": "₹1 Lakh - ₹10 Lakh (Formal Education/Classes)",
        "colleges": [
            "National School of Drama (NSD)", "Delhi University (Performing Arts)", "BHU (Performing Arts)", 
            "Kalakshetra Foundation, Chennai", "Gandharva Mahavidyalaya", 
            "Various Private Dance Academies (Shiamak Davar etc.)", "IGNOU (Distance Learning)",
            "Christ University", "Manipal Academy", "Amity University (Performing Arts)"
        ],
        "jobs": [
            "Choreographer (Film/Stage)", "Dance Instructor", "Performer/Dancer", "Artistic Director", 
            "Movement Therapist", "Fitness Instructor", "Stage Manager", "Costume Designer",
            "Dance Critic/Blogger", "Studio Owner/Entrepreneur"
        ],
        "internships": [
            {"role": "Assistant Choreographer", "company": "Film Set/Dance Company", "duration": "6 months"},
            {"role": "Studio Assistant", "company": "Local Dance School", "duration": "3 months"},
            {"role": "Touring Dancer", "company": "Professional Troupe", "duration": "Ongoing"}
        ]
    },
    {
        "topic": "Public Administration/UPSC Officer",
        "stream": "Arts/Science/Commerce/Any",
        "aptitude": "General Knowledge, Writing, Logic, Leadership",
        "personality": "Ethical, Decisive, Highly Disciplined, Resilient",
        "interest": "Governance, Policy, Social Welfare, Law",
        "education": "Any Bachelor's Degree + UPSC Exam",
        "cost": "Medium (Coaching/Books)",
        "difficulty": "Very Hard",
        "description": "Manages local or central government affairs, enforcing laws, implementing policies, and providing public service (IAS, IPS, IFS, etc.).",
        "fees": "₹1 Lakh - ₹10 Lakh (Coaching Cost)",
        "colleges": [
            "Any Recognized University (for Graduation)", "Delhi University (various colleges for BA/B.Com)", 
            "JNU (for MA/Ph.D.)", "IGNOU (Distance Learning)", 
            "Tata Institute of Social Sciences (TISS)", "Various State Universities",
            "Lal Bahadur Shastri National Academy of Administration (LBSNAA) - Training Institute",
            "Sardar Vallabhbhai Patel National Police Academy (SVPNPA)",
            "Foreign Service Institute", "Indian Institute of Public Administration (IIPA)"
        ],
        "jobs": [
            "IAS Officer", "IPS Officer", "IFS Officer (Foreign/Forest)", "Revenue Service Officer (IRS)", 
            "Policy Analyst", "District Magistrate/Collector", "Superintendent of Police", "Joint Secretary (Govt)",
            "Diplomat/Ambassador", "Academic Professor (Public Policy)"
        ],
        "internships": [
            {"role": "Research Assistant", "company": "Policy Think Tank/NGO", "duration": "6 months"},
            {"role": "Administrative Intern", "company": "District Collector's Office", "duration": "3 months"},
            {"role": "UPSC Preparation", "company": "Self-Study/Coaching", "duration": "1-3 years"}
        ]
    },
    {
        "topic": "Ethical Entrepreneur",
        "stream": "Commerce/Science/Arts/Any",
        "aptitude": "Leadership, Risk-Taking, Innovation, Finance",
        "personality": "Visionary, Decisive, Resilient, Ethical",
        "interest": "Starting a business, Social Impact, Innovation",
        "education": "Any Grad + Business Experience / MBA (Entrepreneurship)",
        "cost": "Varies (Startup Capital)",
        "difficulty": "Very Hard",
        "description": "Starts and runs a business focused on profitability while ensuring positive social or environmental impact (e.g., sustainable clothing, clean tech).",
        "fees": "₹0 - ₹25 Lakh (Education/Mentorship)",
        "colleges": [
            "Indian School of Business (ISB)", "IIM Bangalore (NSRCEL Incubator)", "IIT Madras (Incubation Cell)", 
            "XLRI Jamshedpur", "BITS Pilani (Management)", 
            "Amity University (Entrepreneurship)", "SPJIMR Mumbai",
            "Various Startup Accelerators", "Christ University", "Draper University (Global)"
        ],
        "jobs": [
            "Founder/CEO", "Chief Operating Officer (COO)", "Venture Capitalist", "Social Impact Consultant", 
            "Business Mentor", "Product Developer", "Sales Head", "Chief Strategy Officer (CSO)",
            "Angel Investor", "Board Member"
        ],
        "internships": [
            {"role": "Business Development Intern", "company": "Startup/Unicorn", "duration": "6 months"},
            {"role": "Operations Trainee", "company": "SME", "duration": "3 months"},
            {"role": "Product Research Intern", "company": "E-commerce Firm", "duration": "4 months"}
        ]
    },
    {
        "topic": "Technical Writer",
        "stream": "Science-A/PCM/Any",
        "aptitude": "Writing, Logic, Detail, Technical Understanding",
        "personality": "Methodical, Patient, Clear Communicator",
        "interest": "Technology, Documentation, Teaching",
        "education": "B.Tech/BE/B.Sc. + Technical Writing Diploma",
        "cost": "Low-Medium",
        "difficulty": "Medium",
        "description": "Creates easy-to-understand documentation, such as user manuals, software guides, and technical reports for a specific audience.",
        "fees": "₹1 Lakh - ₹8 Lakh (Total Course)",
        "colleges": [
            "IGNOU (Technical Writing Course)", "University of Delhi (Journalism/Comm)", "Pune University (Technical Writing)", 
            "Amity University (Comm)", "Various Technical Institutes (Diploma)",
            "IITs/NITs (Engineering Background)", "BITS Pilani",
            "Christ University", "Manipal Academy", "Online Courses (Coursera/Udemy)"
        ],
        "jobs": [
            "Technical Author", "Documentation Specialist", "UX Writer", "Content Strategist", 
            "Instructional Designer", "Information Architect", "Editor (Technical)", "API Writer",
            "Online Help Specialist", "Academic Researcher"
        ],
        "internships": [
            {"role": "Technical Writing Intern", "company": "Microsoft/TCS/Infosys", "duration": "6 months"},
            {"role": "Documentation Trainee", "company": "Software Startup", "duration": "3 months"},
            {"role": "Content Assistant", "company": "EdTech Firm", "duration": "4 months"}
        ]
    },
    {
        "topic": "Public Health Specialist",
        "stream": "Science-B/PCB/Any",
        "aptitude": "Biology, Statistics, Policy, Empathy",
        "personality": "Ethical, Analytical, Community Focused, Strategic",
        "interest": "Disease Prevention, Health Policy, Community Health",
        "education": "MBBS/Any Grad + MPH (Master of Public Health)",
        "cost": "Medium-High",
        "difficulty": "Hard",
        "description": "Protects and improves the health of communities through education, policy-making, and research into disease and injury prevention.",
        "fees": "₹3 Lakh - ₹15 Lakh (Total MPH)",
        "colleges": [
            "All India Institute of Medical Sciences (AIIMS)", "Tata Institute of Social Sciences (TISS), Mumbai", 
            "Jawaharlal Nehru University (JNU)", "National Institute of Epidemiology (NIE)",
            "Indian Institute of Public Health (IIPH)", "Christian Medical College (CMC), Vellore", 
            "University of Hyderabad", "Manipal Academy",
            "Amity University", "Various Medical Colleges (Preventative Medicine)"
        ],
        "jobs": [
            "Epidemiologist", "Health Policy Analyst", "Biostatistician", "NGO Program Manager", 
            "Community Health Worker", "Disease Control Specialist", "Public Health Director (Govt.)", "Health Educator",
            "Research Scientist", "Biostatistician"
        ],
        "internships": [
            {"role": "Research Assistant", "company": "WHO/UNICEF (Local Office)", "duration": "6 months"},
            {"role": "Field Intern", "company": "Local NGO/Health Department", "duration": "3 months"},
            {"role": "Data Analyst Trainee", "company": "Public Health Lab", "duration": "4 months"}
        ]
    },
    {
        "topic": "Speech Therapist/Audiologist",
        "stream": "Science-B/PCB/Any",
        "aptitude": "Empathy, Communication, Listening, Detail",
        "personality": "Patient, Caring, Good Listener, Analytical",
        "interest": "Hearing, Speech, Communication Disorders",
        "education": "B.Sc. (ASLP) / MASLP",
        "cost": "Medium",
        "difficulty": "Medium",
        "description": "Diagnoses and treats speech, language, communication, and hearing disorders in children and adults.",
        "fees": "₹2 Lakh - ₹10 Lakh (Total Course)",
        "colleges": [
            "All India Institute of Speech and Hearing (AIISH), Mysore", "All India Institute of Medical Sciences (AIIMS)", 
            "Post Graduate Institute of Medical Education and Research (PGIMER)", "Jawaharlal Nehru Medical College",
            "University of Mumbai", "University of Mysore", 
            "Manipal Academy of Higher Education", "SRM Institute of Science and Technology",
            "Ali Yavar Jung National Institute of Speech and Hearing Disabilities", "Various Medical Colleges"
        ],
        "jobs": [
            "Speech-Language Pathologist (SLP)", "Audiologist", "Hearing Aid Specialist", "Clinical Researcher", 
            "Rehabilitation Specialist", "Academic Professor", "Special Educator", "Voice Specialist",
            "Private Practitioner", "Hospital Clinician"
        ],
        "internships": [
            {"role": "Clinical Rotations", "company": "AIISH/Hospital", "duration": "Mandatory"},
            {"role": "Audiometry Trainee", "company": "Hearing Clinic", "duration": "6 months"},
            {"role": "Rehabilitation Intern", "company": "Special Needs School", "duration": "3 months"}
        ]
    },
    {
        "topic": "Foreign Service Officer (IFS)",
        "stream": "Arts/Science/Commerce/Any",
        "aptitude": "Communication, General Knowledge, Diplomacy, Ethics",
        "personality": "Diplomatic, Outgoing, Culturally Aware, Resilient",
        "interest": "Global Politics, International Law, Travel",
        "education": "Any Bachelor's Degree + UPSC Exam",
        "cost": "Medium (Coaching/Books)",
        "difficulty": "Very Hard",
        "description": "Represents the country's interests abroad, working in embassies and consulates to manage diplomatic, trade, and cultural relations.",
        "fees": "₹1 Lakh - ₹10 Lakh (Coaching Cost)",
        "colleges": [
            "Any Recognized University (for Graduation)", "Jawaharlal Nehru University (JNU - International Relations)", 
            "Delhi University (for BA/MA)", "IGNOU (Distance Learning)", 
            "Tata Institute of Social Sciences (TISS)", "Indian Institute of Public Administration (IIPA)",
            "Foreign Service Institute (Training Institute)", "Various International Relations Programs",
            "Christ University", "Symbiosis School of International Studies"
        ],
        "jobs": [
            "Ambassador/High Commissioner", "First/Second Secretary", "Consul General", "Policy Advisor", 
            "Diplomatic Correspondent", "International Law Expert", "Trade Negotiator", "Protocol Officer",
            "United Nations Delegate", "Academic Professor (IR)"
        ],
        "internships": [
            {"role": "Research Assistant", "company": "Think Tank/University (IR Focus)", "duration": "6 months"},
            {"role": "Embassy Intern", "company": "Foreign Embassy in India", "duration": "3 months"},
            {"role": "UPSC Preparation", "company": "Self-Study/Coaching", "duration": "1-3 years"}
        ]
    },
    {
        "topic": "Art Restorer/Conservator",
        "stream": "Arts/Science/Any",
        "aptitude": "Detail, Chemistry, Patience, Fine Motor Skills",
        "personality": "Methodical, Patient, Artistic, Ethical",
        "interest": "Art, History, Chemistry, Preservation",
        "education": "M.A. (Conservation/Museology) / Diploma",
        "cost": "Medium",
        "difficulty": "Medium",
        "description": "Preserves and restores damaged or decaying artwork, historical artifacts, and monuments, often requiring knowledge of chemistry and materials.",
        "fees": "₹1 Lakh - ₹8 Lakh (Total Course)",
        "colleges": [
            "National Museum Institute of History of Art, Conservation and Museology (NMI)", "National Research Laboratory for Conservation of Cultural Property (NRLC)", 
            "University of Calcutta (Conservation)", "Jawaharlal Nehru University (JNU)",
            "Delhi University (Chemistry/Art History)", "M.S. University of Baroda",
            "IGNCA (Conservation)", "Various Art Colleges",
            "SRM Institute of Science and Technology", "TISS (Conservation)"
        ],
        "jobs": [
            "Art Conservator", "Monument Restorer", "Paper/Textile Conservator", "Curator (Conservation)", 
            "Conservation Scientist", "Museum Technician", "Archival Specialist", "Freelance Restorer",
            "Academic Professor", "Heritage Consultant"
        ],
        "internships": [
            {"role": "Conservation Intern", "company": "National Museum/ASI", "duration": "6 months"},
            {"role": "Restoration Trainee", "company": "Private Restoration Studio", "duration": "3 months"},
            {"role": "Research Assistant", "company": "Conservation Lab", "duration": "4 months"}
        ]
    },
    {
        "topic": "UX/UI Designer",
        "stream": "Science-A/PCM/Arts/Any",
        "aptitude": "Design, Empathy (User Focus), Logic, Communication",
        "personality": "Creative, Analytical, User-Focused, Collaborative",
        "interest": "Apps, Websites, User Experience, Psychology",
        "education": "B.Des / Certification in UX/UI / B.Tech (CS)",
        "cost": "Medium-High",
        "difficulty": "Medium-Hard",
        "description": "UX (User Experience) focuses on how a product works and feels; UI (User Interface) focuses on how a product looks and functions visually.",
        "fees": "₹4 Lakh - ₹25 Lakh (Total Course)",
        "colleges": [
            "National Institute of Design (NID)", "Industrial Design Centre (IDC), IIT Bombay", 
            "Symbiosis Institute of Design (SID)", "Pearl Academy", 
            "CEPT University", "BITS Pilani (Management/Design)",
            "MIT Institute of Design", "Whistling Woods International",
            "IIIT Hyderabad", "Amity School of Design"
        ],
        "jobs": [
            "UX Researcher", "Interaction Designer", "Visual Designer", "Product Designer", 
            "Information Architect", "Content Strategist", "Front-End Developer (Design Focus)", "Design Systems Lead",
            "Creative Director", "Freelance Consultant"
        ],
        "internships": [
            {"role": "UX Intern", "company": "Google/Microsoft/Amazon", "duration": "6 months"},
            {"role": "Design Trainee", "company": "Tech Startup", "duration": "3 months"},
            {"role": "Research Assistant", "company": "Design Consulting Firm", "duration": "4 months"}
        ]
    },
    {
        "topic": "Theatre Artist/Actor",
        "stream": "Arts/Any",
        "aptitude": "Creativity, Communication, Stage Presence, Memory",
        "personality": "Expressive, Disciplined, Resilient, Team Player",
        "interest": "Drama, Performance, Storytelling, Culture",
        "education": "Diploma/Degree in Performing Arts/Theatre",
        "cost": "Low (Skill-Based)",
        "difficulty": "Very Hard (Career Stability)",
        "description": "Performs roles in plays, films, or TV, or works backstage in production, directing, or writing plays.",
        "fees": "₹1 Lakh - ₹8 Lakh (Formal Education/Training)",
        "colleges": [
            "National School of Drama (NSD), Delhi", "Film and Television Institute of India (FTII), Pune", 
            "Satyajit Ray Film & Television Institute (SRFTI), Kolkata", "Delhi University (Theatre)",
            "BHU (Performing Arts)", "Whistling Woods International", 
            "Amity School of Performing Arts", "Christ University",
            "Stella Maris College, Chennai", "St. Xavier's College, Mumbai"
        ],
        "jobs": [
            "Stage Actor", "Film/TV Actor", "Theatre Director", "Playwright", 
            "Voice Artist/Dubbing", "Casting Director", "Drama Teacher", "Production Designer",
            "Theatre Technician", "Stand-up Comedian"
        ],
        "internships": [
            {"role": "Apprentice", "company": "Reputed Theatre Group", "duration": "6 months"},
            {"role": "Production Assistant", "company": "Film/TV Set", "duration": "3 months"},
            {"role": "Acting Workshop", "company": "Private Academy", "duration": "Flexible"}
        ]
    },
    {
        "topic": "Data Architect",
        "stream": "Science-A/PCM",
        "aptitude": "Logic, Coding, Systems Design, Data Modeling",
        "personality": "Strategic, Detail-Oriented, Analytical",
        "interest": "Databases, Cloud Computing, System Structures",
        "education": "B.Tech/BE (CS/IT) + Certifications",
        "cost": "Medium-High",
        "difficulty": "Hard",
        "description": "Designs, creates, deploys, and manages an organization's data architecture, ensuring data systems are integrated and secure.",
        "fees": "₹4 Lakh - ₹20 Lakh (Total Course)",
        "colleges": [
            "IIT Bombay", "IIIT Hyderabad", "BITS Pilani", "NIT Trichy", 
            "Delhi Technological University (DTU)", "Anna University", 
            "VIT Vellore", "Manipal Institute of Technology",
            "Amity University (Data Science)", "Various Online/Global Certification Bodies"
        ],
        "jobs": [
            "Cloud Architect", "Database Administrator (DBA)", "Enterprise Architect", "Big Data Engineer", 
            "Data Governance Specialist", "Solutions Architect", "Data Modeler", "Business Intelligence Manager",
            "ETL Specialist", "Data Security Engineer"
        ],
        "internships": [
            {"role": "Data Intern", "company": "Microsoft/Amazon Web Services", "duration": "6 months"},
            {"role": "DBA Trainee", "company": "Large Tech Firm", "duration": "3 months"},
            {"role": "Cloud Assistant", "company": "Cloud Consulting Firm", "duration": "4 months"}
        ]
    },
    {
        "topic": "Neuroscientist",
        "stream": "Science-B/PCB",
        "aptitude": "Biology, Research, Advanced Science, Logic",
        "personality": "Inquisitive, Patient, Analytical, Independent",
        "interest": "Brain, Nervous System, Consciousness",
        "education": "M.Sc. + Ph.D. (Neuroscience/Biomedical Science)",
        "cost": "Medium-High",
        "difficulty": "Very Hard",
        "description": "Studies the nervous system, including the brain, spinal cord, and sensory neurons, to understand function and disease.",
        "fees": "₹2 Lakh - ₹15 Lakh (Total Post-Grad/Ph.D.)",
        "colleges": [
            "National Institute of Mental Health and Neuro-Sciences (NIMHANS), Bangalore", "Indian Institute of Science (IISc), Bangalore", 
            "All India Institute of Medical Sciences (AIIMS)", "Jawaharlal Nehru University (JNU)", 
            "University of Hyderabad", "Centre for Cellular and Molecular Biology (CCMB)",
            "University of Delhi", "Manipal Academy",
            "BITS Pilani", "IIT Madras (Biomedical Engg)"
        ],
        "jobs": [
            "Research Scientist (Lab/Academic)", "Clinical Neuroscientist (with MD)", "Cognitive Neuroscientist", "Pharmaceutical Researcher", 
            "Neuro-Radiologist", "Biomedical Engineer (Neuro)", "Academic Professor", "Data Analyst (Brain Imaging)",
            "Neurology Technician", "Neuro-Marketing Specialist"
        ],
        "internships": [
            {"role": "Research Fellow", "company": "NIMHANS/IISc Lab", "duration": "6 months"},
            {"role": "Lab Assistant", "company": "University Research Project", "duration": "3 months"},
            {"role": "Clinical Trainee", "company": "Hospital Neurology Dept.", "duration": "4 months"}
        ]
    },
    {
        "topic": "Agricultural Scientist",
        "stream": "Science-B/PCB/Any",
        "aptitude": "Biology, Practical, Research, Fieldwork",
        "personality": "Practical, Resilient, Problem-Solver (Rural focus)",
        "interest": "Farming, Crop Science, Food Security",
        "education": "B.Sc. + M.Sc. (Agriculture/Horticulture)",
        "cost": "Medium",
        "difficulty": "Medium",
        "description": "Studies and develops new farming techniques, crop varieties, and soil management to improve yield and sustainability.",
        "fees": "₹1 Lakh - ₹8 Lakh (Total Course)",
        "colleges": [
            "Indian Agricultural Research Institute (IARI), Pusa", "Punjab Agricultural University", 
            "GB Pant University of Agriculture and Technology", "Tamil Nadu Agricultural University",
            "Indian Council of Agricultural Research (ICAR) Institutes", "University of Agricultural Sciences, Bangalore", 
            "Anna University", "BHU (Agriculture)",
            "Aligarh Muslim University (AMU)", "Various State Agricultural Universities"
        ],
        "jobs": [
            "Agronomist", "Horticulturist", "Soil Scientist", "Agricultural Consultant", 
            "Plant Breeder/Geneticist", "ICAR Scientist", "Farm Manager", "Academic Professor",
            "Agricultural Economist", "Extension Officer (Govt.)"
        ],
        "internships": [
            {"role": "Field Intern", "company": "ICAR/Agricultural University Farm", "duration": "6 months"},
            {"role": "Research Assistant", "company": "Seed/Fertilizer Company", "duration": "3 months"},
            {"role": "Consultancy Trainee", "company": "Agricultural NGO", "duration": "4 months"}
        ]
    },
    {
        "topic": "Financial Planner",
        "stream": "Commerce/Any",
        "aptitude": "Finance, Communication, Empathy, Logic",
        "personality": "Trustworthy, Patient, Client-Focused, Analytical",
        "interest": "Personal Finance, Investment, Wealth Management",
        "education": "B.Com/BBA/Any Grad + CFP Certification",
        "cost": "Medium",
        "difficulty": "Medium",
        "description": "Advises individuals on managing their money, investments, insurance, and retirement planning to meet long-term financial goals.",
        "fees": "₹2 Lakh - ₹10 Lakh (Certifications/Education)",
        "colleges": [
            "Financial Planning Standards Board India (FPSB) - Cert Body", "IIM/FMS (MBA Helpful)", 
            "NMIMS Mumbai", "Christ University, Bangalore", "Symbiosis Institute of Management",
            "Various Commerce Colleges (B.Com)", "Amity University (Finance)",
            "University of Mumbai", "Loyola College, Chennai", "Hans Raj College, Delhi"
        ],
        "jobs": [
            "Certified Financial Planner (CFP)", "Wealth Manager", "Investment Advisor", "Insurance Broker", 
            "Retirement Consultant", "Estate Planner", "Relationship Manager (Banking)", "Mutual Fund Specialist",
            "Freelance Consultant", "Academic Lecturer"
        ],
        "internships": [
            {"role": "Advisory Intern", "company": "HDFC/ICICI Wealth", "duration": "6 months"},
            {"role": "Research Assistant", "company": "Financial Planning Firm", "duration": "3 months"},
            {"role": "Sales Trainee", "company": "Insurance Company", "duration": "4 months"}
        ]
    },
    {
        "topic": "Public Policy Analyst",
        "stream": "Arts/Science/Commerce/Any",
        "aptitude": "Research, Writing, Logic, Policy Analysis",
        "personality": "Analytical, Objective, Strategic, Ethical",
        "interest": "Government, Law, Social Issues, Economics",
        "education": "B.A./Any Grad + M.A. (Public Policy)",
        "cost": "Medium-High",
        "difficulty": "Hard",
        "description": "Evaluates government policies and programs, recommending changes or new strategies to address social, economic, or environmental problems.",
        "fees": "₹2 Lakh - ₹15 Lakh (Total Master's)",
        "colleges": [
            "Tata Institute of Social Sciences (TISS), Mumbai", "Jawaharlal Nehru University (JNU)", "Indian School of Business (ISB)", 
            "Indian Institute of Public Health (IIPH)", "Ashoka University", 
            "Delhi University (Political Science/Economics)", "University of Hyderabad",
            "National Law School of India University (NLSIU)", "IIM (Public Policy)", "Azim Premji University"
        ],
        "jobs": [
            "Policy Analyst (Think Tank/Govt)", "Legislative Aide", "Economist (Policy Focus)", "Lobbyist", 
            "Non-Profit Director", "Social Sector Consultant", "Research Fellow", "Academic Professor",
            "Urban Planner", "Civil Service Officer"
        ],
        "internships": [
            {"role": "Policy Research Intern", "company": "NITI Aayog/Think Tank", "duration": "6 months"},
            {"role": "Legislative Assistant", "company": "Member of Parliament (LAMP)", "duration": "3 months"},
            {"role": "NGO Analyst", "company": "Oxfam/World Bank (local)", "duration": "4 months"}
        ]
    },
    {
        "topic": "Cinematographer/DOP",
        "stream": "Arts/Any",
        "aptitude": "Photography, Visual Arts, Lighting, Technical",
        "personality": "Creative, Detail-Oriented, Technical, Collaborative",
        "interest": "Film, Photography, Lighting, Visual Aesthetics",
        "education": "Diploma/Degree in Cinematography/Film Making",
        "cost": "High",
        "difficulty": "Medium-Hard",
        "description": "The Director of Photography (DOP) is responsible for the overall visual look of a film, overseeing cameras, lighting, and composition.",
        "fees": "₹5 Lakh - ₹25 Lakh (Total Course)",
        "colleges": [
            "Film and Television Institute of India (FTII), Pune", "Satyajit Ray Film & Television Institute (SRFTI), Kolkata", 
            "Whistling Woods International (WWI), Mumbai", "Asian Academy of Film & TV (AAFT)",
            "National Institute of Design (NID)", "L.V. Prasad Film & TV Academy", 
            "Annapurna International School of Film & Media", "Amity School of Communication",
            "Christ University (Media)", "Various Photography/Art Schools"
        ],
        "jobs": [
            "Director of Photography (DOP)", "Camera Operator", "Gaffer (Chief Lighting Tech)", "Colorist", 
            "Video Editor", "Still Photographer", "Gimbal/Drone Operator", "VFX Artist",
            "Director (Film/TV)", "Film Educator"
        ],
        "internships": [
            {"role": "Camera Assistant", "company": "Film/TV Set", "duration": "6 months"},
            {"role": "Lighting Intern", "company": "Production House", "duration": "3 months"},
            {"role": "Post-Production Trainee", "company": "Studio", "duration": "4 months"}
        ]
    },
    {
        "topic": "Activist/Social Worker",
        "stream": "Arts/Science/Commerce/Any",
        "aptitude": "Empathy, Communication, Resilience, Organization",
        "personality": "Passionate, Ethical, Resilient, Community Focused",
        "interest": "Social Justice, Poverty, Human Rights, Policy",
        "education": "B.A./Any Grad + M.A. (Social Work - MSW)",
        "cost": "Low-Medium",
        "difficulty": "Hard (Emotional Labor/Low Pay)",
        "description": "Works to improve the lives of individuals, families, and communities, addressing societal problems through direct action and advocacy.",
        "fees": "₹1 Lakh - ₹10 Lakh (Total Course)",
        "colleges": [
            "Tata Institute of Social Sciences (TISS), Mumbai", "Delhi School of Social Work (DSSW), DU", 
            "Jamia Millia Islamia", "Loyola College, Chennai", "Christ University, Bangalore", 
            "Amity University", "IGNOU (Distance Learning)", "Azim Premji University",
            "Jawaharlal Nehru University (JNU)", "University of Calcutta"
        ],
        "jobs": [
            "NGO Program Manager", "Community Organizer", "Social Worker (Clinical/Medical)", "Fundraiser", 
            "Advocate/Lobbyist", "Policy Analyst", "Counsellor", "Rehabilitation Specialist",
            "Research Fellow", "Academic Professor"
        ],
        "internships": [
            {"role": "Field Intern", "company": "Local NGO", "duration": "6 months"},
            {"role": "Advocacy Assistant", "company": "Human Rights Organization", "duration": "3 months"},
            {"role": "Program Trainee", "company": "International Aid Agency (local office)", "duration": "4 months"}
        ]
    },
    {
        "topic": "Aerodynamics Specialist",
        "stream": "Science-A/PCM",
        "aptitude": "Physics, Fluid Dynamics, Advanced Math, Modeling",
        "personality": "Analytical, Detail-Oriented, Research-Focused",
        "interest": "Flight, Wind Tunnels, Vehicle Efficiency",
        "education": "B.Tech/BE (Aerospace/Mech) + M.Tech (Aerodynamics)",
        "cost": "High",
        "difficulty": "Very Hard",
        "description": "Studies the movement of air and the forces (lift, drag) created by objects moving through it, critical for aircraft and vehicle design.",
        "fees": "₹6 Lakh - ₹30 Lakh (Total Course)",
        "colleges": [
            "Indian Institute of Technology (IIT) Bombay", "IIT Madras", "Indian Institute of Science (IISc), Bangalore",
            "PEC Chandigarh", "Madras Institute of Technology (MIT)", "Amity University (Noida)", "Hindustan University",
            "UPES Dehradun", "Manipal Academy of Higher Education", "JNTU Hyderabad"
        ],
        "jobs": [
            "Aerodynamicist", "Computational Fluid Dynamics (CFD) Analyst", "Flight Test Engineer", "Wind Tunnel Specialist", 
            "Formula 1 Designer", "Aeroacoustics Engineer", "R&D Scientist", "Aircraft Designer",
            "Missile Design Specialist", "Academic Researcher"
        ],
        "internships": [
            {"role": "CFD Intern", "company": "HAL/DRDO Labs", "duration": "6 months"},
            {"role": "Research Intern", "company": "IISc/IIT Lab", "duration": "3 months"},
            {"role": "Design Trainee", "company": "Automotive R&D Centre", "duration": "4 months"}
        ]
    },
    {
        "topic": "Genetics Counselor",
        "stream": "Science-B/PCB",
        "aptitude": "Biology, Genetics, Empathy, Communication",
        "personality": "Caring, Patient, Scientific, Ethical",
        "interest": "Inheritance, DNA, Medical Science, Counselling",
        "education": "M.Sc. (Genetics/Genetic Counselling)",
        "cost": "Medium-High",
        "difficulty": "Hard",
        "description": "Assesses individual or family risk for various inherited conditions and counsels them on genetic testing options and results.",
        "fees": "₹3 Lakh - ₹15 Lakh (Total Master's)",
        "colleges": [
            "All India Institute of Medical Sciences (AIIMS)", "Sanjay Gandhi Post Graduate Institute of Medical Sciences (SGPGIMS)", 
            "Christian Medical College (CMC), Vellore", "Manipal Academy of Higher Education", 
            "Jawaharlal Nehru University (JNU)", "University of Delhi", "University of Hyderabad",
            "BITS Pilani", "Amity University", "Various Medical Colleges"
        ],
        "jobs": [
            "Genetic Counselor", "Clinical Geneticist", "Lab Manager (Genetics)", "Research Scientist", 
            "Public Health Specialist (Genetics)", "Academic Professor", "Bioethics Consultant", "Drug Development Scientist",
            "Counselling Psychologist (Specialized)", "Medical Writer"
        ],
        "internships": [
            {"role": "Clinical Trainee", "company": "Hospital Genetics Dept.", "duration": "6 months"},
            {"role": "Research Intern", "company": "CCMB/Research Lab", "duration": "3 months"},
            {"role": "Counselling Assistant", "company": "Private Clinic", "duration": "4 months"}
        ]
    },
    {
        "topic": "Patent Attorney/Agent",
        "stream": "Science-A/PCM/Any",
        "aptitude": "Law, Science/Tech Knowledge, Detail, Writing",
        "personality": "Methodical, Detail-Oriented, Ethical, Analytical",
        "interest": "Intellectual Property, Inventions, Law",
        "education": "B.Tech/B.Sc. + LLB + Patent Agent Exam",
        "cost": "Medium-High",
        "difficulty": "Very Hard",
        "description": "Specializes in protecting intellectual property, specifically guiding inventors through the process of filing and defending patents.",
        "fees": "₹5 Lakh - ₹20 Lakh (Total Course)",
        "colleges": [
            "National Law School of India University (NLSIU), Bangalore (IP Law)", "IIT Kharagpur (IP Law School)", 
            "NALSAR University of Law, Hyderabad", "Faculty of Law, Delhi University (DU)",
            "Symbiosis Law School, Pune", "BITS Pilani (Science/Engg)",
            "Anna University", "University of Mumbai",
            "Indian Patent Office (Exam Body)", "Various Patent/IP Firms"
        ],
        "jobs": [
            "Patent Agent", "Patent Lawyer", "IP Counsel (in-house)", "Legal Consultant (IP)", 
            "Technology Transfer Officer", "Research Analyst (Patent Search)", "Compliance Officer", "IP Valuation Specialist",
            "Academic Professor", "Litigation Lawyer (IP)"
        ],
        "internships": [
            {"role": "Legal Intern", "company": "Patent Law Firm", "duration": "6 months"},
            {"role": "Research Trainee", "company": "Technology Transfer Office", "duration": "3 months"},
            {"role": "IP Assistant", "company": "Large Corporate Legal Dept.", "duration": "4 months"}
        ]
    },
    {
        "topic": "Quantitative Analyst (Quant)",
        "stream": "Commerce/Science-A/PCM",
        "aptitude": "Advanced Maths, Coding (Python/R), Statistics, Finance",
        "personality": "Highly Analytical, Objective, High Pressure Tolerance",
        "interest": "Stock Market, Algorithms, Financial Modeling",
        "education": "M.Sc. (Statistics/Quant Finance) / B.Tech + MBA",
        "cost": "Very High",
        "difficulty": "Very Hard",
        "description": "Uses complex mathematical and statistical models to predict market movements, manage risk, and develop trading strategies for financial institutions.",
        "fees": "₹10 Lakh - ₹40 Lakh (M.Sc./MBA)",
        "colleges": [
            "Indian Statistical Institute (ISI), Kolkata", "IIT Bombay (Financial Engineering)", "IIT Kharagpur (Financial Engineering)", 
            "IIM Ahmedabad (Finance)", "FMS Delhi", 
            "NMIMS Mumbai", "BITS Pilani", "University of Delhi (Statistics)",
            "Madras School of Economics", "Various Foreign Universities (MS Quant Finance)"
        ],
        "jobs": [
            "Quant Trader", "Risk Modeler", "Quantitative Developer", "Investment Strategist", 
            "Data Scientist (Finance)", "Algorithm Developer", "Portfolio Manager", "Credit Risk Analyst",
            "Hedge Fund Analyst", "Academic Professor (Quant Finance)"
        ],
        "internships": [
            {"role": "Quant Intern", "company": "Goldman Sachs/JP Morgan", "duration": "10 weeks"},
            {"role": "Research Analyst Trainee", "company": "Hedge Fund", "duration": "3 months"},
            {"role": "Algo Trading Assistant", "company": "Boutique Trading Firm", "duration": "4 months"}
        ]
    },
    {
        "topic": "Air Traffic Controller (ATC)",
        "stream": "Science-A/PCM/Any",
        "aptitude": "Focus, Decision-Making, Spatial Awareness, Communication",
        "personality": "Resilient, Calm, Highly Responsible, Quick Thinker",
        "interest": "Aviation, Logistics, High Pressure Operations",
        "education": "Any Grad (Science Background Preferred) + AAI Exam",
        "cost": "Low (Govt. Exam)",
        "difficulty": "Hard",
        "description": "Guides aircraft safely through takeoff, landing, and flight paths, maintaining separation and managing air traffic flow.",
        "fees": "₹50,000 - ₹5 Lakh (Coaching/Training)",
        "colleges": [
            "Airports Authority of India (AAI) - Training Academy", "Jawaharlal Nehru University (JNU)", 
            "University of Delhi", "Various Engineering Colleges (Electronics/Comm)",
            "Indira Gandhi Rashtriya Uran Akademi (IGRUA)", "BITS Pilani (Relevant Engg)",
            "Manipal Academy", "Amity University (Aviation)",
            "Government Aviation Training Institute", "Various Govt. Exam Coaching Centers"
        ],
        "jobs": [
            "Tower Controller", "Radar Controller", "Ground Controller", "Flow Management Specialist", 
            "Airspace Planner", "Training Instructor", "ATC Manager", "Safety Inspector",
            "Aviation Consultant", "Regulatory Affairs Officer"
        ],
        "internships": [
            {"role": "Observer Intern", "company": "AAI Control Tower", "duration": "6 months (Restricted Access)"},
            {"role": "Ground Operations Trainee", "company": "Airport Authority", "duration": "3 months"},
            {"role": "Simulator Training", "company": "Flying Academy", "duration": "Flexible"}
        ]
    },
    {
        "topic": "Journalist (Sports/Entertainment)",
        "stream": "Arts/Any",
        "aptitude": "Writing, Communication, Subject Knowledge, Interviewing",
        "personality": "Outgoing, Enthusiastic, Opinionated, Quick Witted",
        "interest": "Sports, Movies, Celebrities, Pop Culture",
        "education": "BA/BJMC + Diploma in Sports/Arts Journalism",
        "cost": "Medium",
        "difficulty": "Medium-Hard",
        "description": "Reports and provides commentary on sports events, movie reviews, and entertainment industry news for various media platforms.",
        "fees": "₹1 Lakh - ₹8 Lakh (Total Course)",
        "colleges": [
            "Asian College of Journalism (ACJ), Chennai", "Indian Institute of Mass Communication (IIMC)", 
            "Xavier Institute of Communications (XIC), Mumbai", "Symbiosis Institute of Media and Communication (SIMC)",
            "Sports Journalism Academies", "Christ University", 
            "Manipal Institute of Communication", "Mudra Institute of Communications (MICA)",
            "Whistling Woods International", "Amity School of Communication"
        ],
        "jobs": [
            "Sports Reporter", "Film Critic", "Entertainment Editor", "Talk Show Host", 
            "Live Commentator", "Podcast Producer", "Columnist/Blogger", "Social Media Manager (Media)",
            "Publicist", "Content Strategist"
        ],
        "internships": [
            {"role": "Reporting Intern", "company": "Star Sports/ESPN (India)", "duration": "6 months"},
            {"role": "Media Assistant", "company": "Film Magazine/Website", "duration": "3 months"},
            {"role": "Broadcast Trainee", "company": "News Channel", "duration": "4 months"}
        ]
    },
    {
        "topic": "Ethical Sourcing/Procurement Manager",
        "stream": "Commerce/Any",
        "aptitude": "Negotiation, Logistics, Ethics, Finance",
        "personality": "Ethical, Decisive, Strategic, Detail-Oriented",
        "interest": "Supply Chain, Sustainability, Global Trade",
        "education": "B.Com/Any Grad + MBA (Supply Chain/Ethical Mgmt)",
        "cost": "Medium-High",
        "difficulty": "Medium-Hard",
        "description": "Manages the acquisition of goods and services, ensuring the process is both cost-effective and compliant with ethical and sustainable standards.",
        "fees": "₹5 Lakh - ₹30 Lakh (MBA/PGP)",
        "colleges": [
            "IIM Calcutta", "IIM Bangalore", "NITIE Mumbai (now IIM Mumbai)", "XLRI Jamshedpur", 
            "Symbiosis Institute of Operations Management (SIOM)", "Indian School of Business (ISB)",
            "BITS Pilani (Management)", "TERI School of Advanced Studies (Sustainability)",
            "Delhi Technological University (DTU - MBA)", "Anna University"
        ],
        "jobs": [
            "Procurement Manager", "Sourcing Specialist", "Vendor Manager", "Logistics Manager", 
            "Sustainability Officer", "Compliance Officer", "Contract Negotiator", "Supply Chain Consultant",
            "Chief Procurement Officer (CPO)", "CSR Specialist"
        ],
        "internships": [
            {"role": "Procurement Intern", "company": "Large Manufacturing/Retail MNC", "duration": "6 months"},
            {"role": "Sourcing Trainee", "company": "FMCG Company", "duration": "3 months"},
            {"role": "Sustainability Intern", "company": "NGO/Corporate CSR Dept.", "duration": "4 months"}
        ]
    },
    {
        "topic": "Corporate Trainer/L&D Specialist",
        "stream": "Arts/Science/Commerce/Any",
        "aptitude": "Communication, Teaching, Empathy, Organization",
        "personality": "Outgoing, Motivational, Patient, Subject Expert",
        "interest": "Teaching, Adult Education, Corporate Culture",
        "education": "Any Grad + MBA (HR) / Certification in Training/L&D",
        "cost": "Medium",
        "difficulty": "Medium",
        "description": "Designs and delivers educational programs to employees to improve skills, knowledge, and performance within a company.",
        "fees": "₹3 Lakh - ₹15 Lakh (Total Course)",
        "colleges": [
            "XLRI Jamshedpur", "Tata Institute of Social Sciences (TISS), Mumbai", "IIM Calcutta (MBA)",
            "Symbiosis Institute of Business Management (SIBM)", "NMIMS Mumbai", 
            "Mudra Institute of Communications (MICA)", "Indian School of Business (ISB)",
            "Amity University (HR/OD)", "Various Certification Bodies (ATD)", "IGNOU (Distance Learning)"
        ],
        "jobs": [
            "Learning & Development Manager", "Corporate Trainer", "Instructional Designer", "E-Learning Specialist", 
            "HR Business Partner (Training Focus)", "OD Consultant", "Curriculum Developer", "Technical Trainer",
            "Soft Skills Coach", "Training Vendor Manager"
        ],
        "internships": [
            {"role": "L&D Intern", "company": "TCS/Infosys/MNC", "duration": "6 months"},
            {"role": "Training Assistant", "company": "Training Firm", "duration": "3 months"},
            {"role": "Instructional Design Trainee", "company": "EdTech Company", "duration": "4 months"}
        ]
    },
    {
        "topic": "Horticulturist/Landscape Designer",
        "stream": "Science-B/PCB/Arts/Any",
        "aptitude": "Biology, Design, Practical, Aesthetics",
        "personality": "Creative, Patient, Hands-on, Detail-Oriented",
        "interest": "Gardens, Plants, Outdoor Spaces, Design",
        "education": "B.Sc. + M.Sc. (Horticulture/Landscape Architecture)",
        "cost": "Medium",
        "difficulty": "Medium",
        "description": "Designs and manages outdoor spaces (parks, gardens) and the cultivation of plants, focusing on aesthetics, ecology, and utility.",
        "fees": "₹1 Lakh - ₹10 Lakh (Total Course)",
        "colleges": [
            "Indian Agricultural Research Institute (IARI), Pusa", "Punjab Agricultural University", 
            "GB Pant University of Agriculture and Technology", "School of Planning and Architecture (SPA), Delhi (Landscape)",
            "Anna University", "Tamil Nadu Agricultural University", 
            "CEPT University, Ahmedabad", "NIT Calicut",
            "University of Agricultural Sciences, Bangalore", "Various Architecture/Design Colleges"
        ],
        "jobs": [
            "Landscape Architect", "Garden Designer", "Arborist", "Plant Pathologist", 
            "Nursery Manager", "Park Manager", "Urban Greening Specialist", "Horticultural Consultant",
            "Academic Professor", "Field Technician"
        ],
        "internships": [
            {"role": "Design Intern", "company": "Landscape Architecture Firm", "duration": "6 months"},
            {"role": "Nursery Trainee", "company": "Commercial Nursery", "duration": "3 months"},
            {"role": "Field Assistant", "company": "Municipal/Govt Park Dept.", "duration": "4 months"}
        ]
    },
    {
        "topic": "Geographic Information Systems (GIS) Specialist",
        "stream": "Science-A/PCM/Any",
        "aptitude": "Data Analysis, Logic, Spatial Reasoning, Coding",
        "personality": "Analytical, Detail-Oriented, Methodical",
        "interest": "Mapping, Data Visualization, Urban Planning",
        "education": "M.Sc./M.Tech (GIS/Remote Sensing)",
        "cost": "Medium",
        "difficulty": "Medium",
        "description": "Uses software systems (GIS) to capture, store, manipulate, analyze, and present all types of geographical data in maps and databases.",
        "fees": "₹2 Lakh - ₹12 Lakh (Total Course)",
        "colleges": [
            "Indian Institute of Remote Sensing (IIRS), Dehradun", "IIT Bombay (Centre of Studies in Resources Engineering)", 
            "Anna University", "Jawaharlal Nehru University (JNU)", "University of Hyderabad", 
            "CEPT University, Ahmedabad", "BITS Pilani (Science)",
            "University of Pune", "Amity University (GIS)", "Various Engineering Colleges"
        ],
        "jobs": [
            "GIS Analyst", "Cartographer", "Remote Sensing Specialist", "Photogrammetrist", 
            "Surveyor", "Urban Planner", "Environmental Consultant", "Data Scientist (Spatial)",
            "Disaster Management Specialist", "Infrastructure Planner"
        ],
        "internships": [
            {"role": "GIS Intern", "company": "Urban Development Authority", "duration": "6 months"},
            {"role": "Data Analyst Trainee", "company": "Tech/Mapping Company", "duration": "3 months"},
            {"role": "Field Research Assistant", "company": "Environmental NGO/Govt.", "duration": "4 months"}
        ]
    },
    {
        "topic": "Patent Examiner",
        "stream": "Science-A/PCM/Science-B/PCB",
        "aptitude": "Science/Tech Knowledge, Detail, Logic, Research",
        "personality": "Methodical, Objective, Ethical, Patient",
        "interest": "Inventions, Law, Technical Research",
        "education": "B.Tech/BE/M.Sc. + UPSC/Recruitment Exam (Govt.)",
        "cost": "Low (Govt. Exam)",
        "difficulty": "Very Hard (Exam)",
        "description": "Works for the government (Indian Patent Office), reviewing patent applications to determine if an invention is novel, non-obvious, and useful.",
        "fees": "₹50,000 - ₹5 Lakh (Coaching/Preparation)",
        "colleges": [
            "Indian Patent Office (Recruitment)", "IITs/NITs (Engineering Background)", 
            "University of Delhi (Science)", "BITS Pilani", "Jawaharlal Nehru University (JNU)", 
            "University of Hyderabad", "Anna University",
            "Various Law Schools (IP Law Diploma)", "Various Government Exam Coaching Centers", "Amity University (IP Law)"
        ],
        "jobs": [
            "Patent Examiner/Analyst", "Patent Office Official", "IP Analyst", "Technical Researcher", 
            "Academic Professor", "Patent Agent (Private Practice)", "Government Policy Advisor (IP)", "Research Scientist",
            "Technology Transfer Officer", "IP Valuator"
        ],
        "internships": [
            {"role": "Technical Research Intern", "company": "University R&D Dept.", "duration": "6 months"},
            {"role": "IP Trainee", "company": "Patent Law Firm (for research support)", "duration": "3 months"},
            {"role": "Govt. Exam Preparation", "company": "Self-Study/Coaching", "duration": "1-3 years"}
        ]
    },
    {
        "topic": "Machine Learning Engineer",
        "stream": "Science-A/PCM",
        "aptitude": "Coding, Advanced Math, Statistics, Logic",
        "personality": "Analytical, Innovative, Problem-Solver, Research-Oriented",
        "interest": "AI, Algorithms, Data Science, Robotics",
        "education": "B.Tech/BE (CS/IT) + M.Tech/M.Sc. (AI/ML)",
        "cost": "High",
        "difficulty": "Very Hard",
        "description": "Designs, builds, and deploys algorithms and models that allow computers to learn from data and make predictions or decisions (Artificial Intelligence).",
        "fees": "₹5 Lakh - ₹25 Lakh (Total Course)",
        "colleges": [
            "IIT Madras (AI/ML)", "IIIT Hyderabad", "Indian Statistical Institute (ISI), Kolkata", "BITS Pilani",
            "IIT Delhi", "NIT Trichy", "Anna University", "University of Hyderabad",
            "SRMIST", "Amity University (AI/ML)"
        ],
        "jobs": [
            "AI/ML Engineer", "Data Scientist", "Deep Learning Specialist", "Computer Vision Engineer", 
            "Natural Language Processing (NLP) Specialist", "Algorithm Developer", "Robotics Engineer", "Quant Analyst",
            "Research Scientist", "Tech Lead (AI)"
        ],
        "internships": [
            {"role": "ML Intern", "company": "Google/Microsoft/Amazon", "duration": "6 months"},
            {"role": "AI Research Trainee", "company": "TCS/Infosys Labs", "duration": "3 months"},
            {"role": "Algorithm Assistant", "company": "Tech Startup", "duration": "4 months"}
        ]
    },
    {
        "topic": "Financial Modeler",
        "stream": "Commerce/Any",
        "aptitude": "Advanced Excel, Finance, Logic, Detail",
        "personality": "Methodical, Highly Analytical, Detail-Oriented",
        "interest": "Valuation, M&A, Capital Markets, Spreadsheet Mastery",
        "education": "B.Com/BBA/B.Tech + MBA (Finance) / Financial Modeling Cert.",
        "cost": "Medium-High",
        "difficulty": "Hard",
        "description": "Builds complex mathematical models in spreadsheets (often Excel) to forecast a company's financial performance or value an asset.",
        "fees": "₹5 Lakh - ₹25 Lakh (MBA/Certifications)",
        "colleges": [
            "IIM Ahmedabad", "IIM Bangalore", "Indian School of Business (ISB)", "FMS Delhi", 
            "NMIMS Mumbai", "XLRI Jamshedpur", "SPJIMR Mumbai", "SRCC, DU",
            "Christ University, Bangalore", "Various Financial Institutes (Certifications)"
        ],
        "jobs": [
            "Financial Analyst", "Investment Banker", "Equity Research Analyst", "Portfolio Manager", 
            "Valuation Specialist", "M&A Analyst", "Credit Analyst", "Financial Controller",
            "Risk Manager", "Venture Capital Analyst"
        ],
        "internships": [
            {"role": "Financial Analyst Intern", "company": "Investment Bank", "duration": "6 months"},
            {"role": "Valuation Trainee", "company": "Accounting/Consulting Firm", "duration": "3 months"},
            {"role": "Equity Research Assistant", "company": "Brokerage Firm", "duration": "4 months"}
        ]
    },
    {
        "topic": "Cryptocurrency/Blockchain Developer",
        "stream": "Science-A/PCM",
        "aptitude": "Coding, Cryptography, Logic, Finance",
        "personality": "Innovative, Problem-Solver, Technical",
        "interest": "Decentralization, FinTech, Digital Assets",
        "education": "B.Tech/BE (CS/IT) + Blockchain Certification",
        "cost": "Medium-High",
        "difficulty": "Very Hard",
        "description": "Designs and develops decentralized applications (DApps) and smart contracts on blockchain platforms like Ethereum or Hyperledger.",
        "fees": "₹4 Lakh - ₹20 Lakh (Total Course)",
        "colleges": [
            "IIT Madras", "IIIT Hyderabad", "BITS Pilani", "NIT Trichy", 
            "CDAC (Advanced Diplomas)", "Delhi Technological University (DTU)", 
            "Anna University", "VIT Vellore",
            "Manipal Academy", "Amity University (Blockchain/FinTech)"
        ],
        "jobs": [
            "Blockchain Developer (Solidity)", "Smart Contract Engineer", "Cryptocurrency Exchange Architect", "Full-Stack Developer (Web3)", 
            "Security Analyst (Blockchain)", "FinTech Consultant", "Cryptography Specialist", "Wallet Developer",
            "Tokenomics Designer", "Auditor (Smart Contract)"
        ],
        "internships": [
            {"role": "Blockchain Intern", "company": "FinTech Startup", "duration": "6 months"},
            {"role": "Smart Contract Trainee", "company": "Crypto Exchange", "duration": "3 months"},
            {"role": "Web3 Assistant", "company": "Tech/Venture Capital Firm", "duration": "4 months"}
        ]
    },
    {
        "topic": "Medical Writer",
        "stream": "Science-B/PCB/Any",
        "aptitude": "Writing, Biology, Detail, Communication",
        "personality": "Methodical, Patient, Clear Communicator",
        "interest": "Science, Health, Documentation, Research",
        "education": "M.Sc./M.Pharm/BDS/MBBS + Diploma in Medical Writing",
        "cost": "Medium",
        "difficulty": "Medium",
        "description": "Prepares scientific documents, regulatory submissions, drug safety reports, and educational materials for the healthcare industry.",
        "fees": "₹1 Lakh - ₹10 Lakh (Total Post-Grad/Diploma)",
        "colleges": [
            "All India Institute of Medical Sciences (AIIMS)", "Christian Medical College (CMC), Vellore", 
            "Manipal Academy of Higher Education", "Jawaharlal Nehru University (JNU)", 
            "University of Delhi (Science)", "Various Pharma Colleges",
            "Amity University (Biotech/Pharma)", "IGNOU (Distance Learning)",
            "Various Online/Private Institutes for Diploma", "BITS Pilani"
        ],
        "jobs": [
            "Regulatory Medical Writer", "Scientific Editor", "Drug Safety Specialist", "Clinical Research Associate (CRA)", 
            "Medical Journalist", "Pharmacovigilance Specialist", "Training Material Developer", "Health Educator",
            "Pharmaceutical Consultant", "Freelance Writer"
        ],
        "internships": [
            {"role": "Medical Writing Intern", "company": "TCS/Cognizant (Pharma vertical)", "duration": "6 months"},
            {"role": "Regulatory Trainee", "company": "Pharmaceutical Company", "duration": "3 months"},
            {"role": "Clinical Research Assistant", "company": "Clinical Research Organization (CRO)", "duration": "4 months"}
        ]
    },
    {
        "topic": "Art Director",
        "stream": "Arts/Any",
        "aptitude": "Creativity, Leadership, Visual Arts, Communication",
        "personality": "Visionary, Decisive, Persuasive, Team Leader",
        "interest": "Advertising, Branding, Photography, Film",
        "education": "B.Des/BFA/Diploma in Visual Communication",
        "cost": "High",
        "difficulty": "Medium-Hard",
        "description": "Leads the creative team in an advertising agency or media company, responsible for the overall visual style and images in campaigns or publications.",
        "fees": "₹6 Lakh - ₹30 Lakh (Total Course)",
        "colleges": [
            "National Institute of Design (NID)", "National Institute of Fashion Technology (NIFT)", 
            "Industrial Design Centre (IDC), IIT Bombay", "Symbiosis Institute of Design (SID)",
            "Mudra Institute of Communications (MICA)", "Pearl Academy", 
            "College of Art, Delhi", "Whistling Woods International",
            "Amity School of Design", "Srishti Institute of Art, Design and Technology"
        ],
        "jobs": [
            "Art Director (Advertising)", "Creative Director", "Visualizer", "Graphic Designer (Senior)", 
            "Production Designer (Film)", "Brand Consultant", "UX/UI Lead", "Photography Director",
            "Academic Professor (Design)", "Freelance Consultant"
        ],
        "internships": [
            {"role": "Visualizer Intern", "company": "Ogilvy/FCB/WPP Agency", "duration": "6 months"},
            {"role": "Design Trainee", "company": "Creative Startup", "duration": "3 months"},
            {"role": "Art Assistant", "company": "Media Production House", "duration": "4 months"}
        ]
    },
    {
        "topic": "Urban Economist",
        "stream": "Commerce/Arts/Any",
        "aptitude": "Economics, Statistics, Policy, Math",
        "personality": "Analytical, Objective, Research-Oriented",
        "interest": "City Growth, Real Estate, Infrastructure",
        "education": "M.A. (Economics) + Specialization in Urban Economics",
        "cost": "Medium-High",
        "difficulty": "Hard",
        "description": "Focuses on the economic efficiency and distribution issues of urban areas, advising on housing, transport, and development projects.",
        "fees": "₹3 Lakh - ₹15 Lakh (Total Master's)",
        "colleges": [
            "Delhi School of Economics (DSE), DU", "Jawaharlal Nehru University (JNU)", "Indian Statistical Institute (ISI), Kolkata", 
            "CEPT University, Ahmedabad (Planning)", "Madras School of Economics", 
            "Ashoka University", "Gokhale Institute of Politics and Economics",
            "IIM (Economics)", "University of Hyderabad", "Anna University (Urban Planning)"
        ],
        "jobs": [
            "Economic Advisor (Urban Development)", "Policy Analyst", "Market Research Analyst (Real Estate)", "Urban Planner", 
            "Infrastructure Consultant", "Academic Professor", "Financial Consultant", "Data Scientist (Economic)",
            "Regional Development Specialist", "GIS Analyst"
        ],
        "internships": [
            {"role": "Research Intern", "company": "NITI Aayog/Planning Commission", "duration": "6 months"},
            {"role": "Analyst Trainee", "company": "World Bank/ADB (local office)", "duration": "3 months"},
            {"role": "Policy Assistant", "company": "Urban Development Authority", "duration": "4 months"}
        ]
    },
    {
        "topic": "Venture Capital Analyst (VC)",
        "stream": "Commerce/Science/Any",
        "aptitude": "Finance, Innovation, Analysis, Risk-Taking",
        "personality": "Quick Thinker, Networker, Visionary, Decisive",
        "interest": "Startups, Technology, Investment, Entrepreneurship",
        "education": "B.Tech/Any Grad + MBA (Finance/Strategy)",
        "cost": "High",
        "difficulty": "Very Hard",
        "description": "Analyzes pitch decks, market opportunities, and financial models of high-growth startups to recommend investments for a VC firm.",
        "fees": "₹5 Lakh - ₹30 Lakh (MBA/PGP)",
        "colleges": [
            "Indian School of Business (ISB), Hyderabad", "IIM Ahmedabad", "IIM Bangalore", "FMS Delhi",
            "NMIMS Mumbai", "XLRI Jamshedpur", "SPJIMR Mumbai", "BITS Pilani (Management)",
            "IITs (Management Studies)", "Various Global VC Courses"
        ],
        "jobs": [
            "VC Analyst/Associate", "Investment Manager (VC)", "Private Equity Analyst", "Startup Founder", 
            "Business Development Manager (Startup)", "Portfolio Manager (VC Funds)", "Strategy Consultant", "M&A Specialist",
            "Data Scientist (Market Trend)", "Investment Banker"
        ],
        "internships": [
            {"role": "VC Intern", "company": "Sequoia/Kalaari/Accel (India)", "duration": "6 months"},
            {"role": "Analyst Trainee", "company": "Boutique Investment Firm", "duration": "3 months"},
            {"role": "Research Assistant", "company": "Startup Incubator", "duration": "4 months"}
        ]
    },
    {
        "topic": "Cyber Law Specialist",
        "stream": "Arts/Science/Commerce/Any",
        "aptitude": "Law, Technology, Logic, Ethics",
        "personality": "Ethical, Methodical, Analytical, Detail-Oriented",
        "interest": "Digital Crimes, Data Privacy, IT Act",
        "education": "LLB + LLM (Cyber Law) / Diploma",
        "cost": "Medium-High",
        "difficulty": "Hard",
        "description": "Specializes in legal issues related to the internet, IT, and digital security, advising companies on data privacy and cybercrime.",
        "fees": "₹3 Lakh - ₹15 Lakh (Total Course)",
        "colleges": [
            "National Law School of India University (NLSIU), Bangalore", "NALSAR University of Law, Hyderabad", 
            "National Law University (NLU), Delhi", "Faculty of Law, Delhi University (DU)",
            "Symbiosis Law School, Pune", "Amity Law School (Cyber Law)", 
            "Indian Law Institute (ILI)", "Various Engineering Colleges (with Law Dept)",
            "Jindal Global Law School", "ILS Law College, Pune"
        ],
        "jobs": [
            "Cyber Law Consultant", "Data Privacy Officer (DPO)", "Legal Counsel (IT/Tech)", "IP Attorney", 
            "Compliance Officer", "Forensic Analyst (Legal Focus)", "Cybercrime Investigator", "Policy Analyst (Tech)",
            "Academic Professor", "Litigation Lawyer (Cyber)"
        ],
        "internships": [
            {"role": "Legal Intern", "company": "Tech Company Legal Dept.", "duration": "6 months"},
            {"role": "Research Trainee", "company": "Cyber Law Firm", "duration": "3 months"},
            {"role": "Policy Assistant", "company": "Govt/Think Tank (IT Policy)", "duration": "4 months"}
        ]
    },
    {
        "topic": "Actuarial Analyst (Property & Casualty)",
        "stream": "Commerce/Science-A/PCM",
        "aptitude": "Advanced Maths, Risk, Statistics, Analysis",
        "personality": "Analytical, Objective, Cautious, Detail-Oriented",
        "interest": "Risk Management, Insurance, Financial Modeling",
        "education": "B.Sc./B.Com + Actuarial Exams (IAI/Global)",
        "cost": "Medium-High",
        "difficulty": "Very Hard",
        "description": "Focuses on quantifying risk for non-life insurance (e.g., car, home, liability), setting premiums, and ensuring reserves are adequate.",
        "fees": "₹5 Lakh - ₹20 Lakh (Exams + Coaching)",
        "colleges": [
            "Institute of Actuaries of India (IAI) - Exam Body", "Delhi School of Economics (DSE)", 
            "Indian Statistical Institute (ISI), Kolkata", "BITS Pilani", "Christ University, Bangalore", 
            "St. Stephen's College, DU", "University of Mumbai (Statistics)",
            "Amity University (Actuarial Science)", "University of Delhi (Statistics)", "Madras School of Economics"
        ],
        "jobs": [
            "Actuary (General Insurance)", "Pricing Specialist", "Reserving Analyst", "Risk Manager", 
            "Reinsurance Specialist", "Product Development Analyst", "Data Scientist (Insurance)", "Underwriter",
            "Academic Professor", "Compliance Officer"
        ],
        "internships": [
            {"role": "Actuarial Intern", "company": "Bajaj Allianz/ICICI Lombard", "duration": "6 months"},
            {"role": "Risk Analyst Trainee", "company": "General Insurance Firm", "duration": "3 months"},
            {"role": "Pricing Intern", "company": "Reinsurance Broker", "duration": "4 months"}
        ]
    },
    {
        "topic": "Financial Crime Analyst",
        "stream": "Commerce/Any",
        "aptitude": "Detail, Law, Logic, Ethics",
        "personality": "Methodical, Objective, Skeptical, Ethical",
        "interest": "Fraud, Money Laundering, Compliance",
        "education": "B.Com/Any Grad + Certification (ACAMS/AML)",
        "cost": "Medium",
        "difficulty": "Medium-Hard",
        "description": "Investigates financial transactions and client behavior to detect and prevent fraud, money laundering, and terrorist financing (AML/KYC).",
        "fees": "₹2 Lakh - ₹10 Lakh (Certifications/Education)",
        "colleges": [
            "ACAMS (Cert Body)", "NMIMS Mumbai (Risk/Finance)", "Christ University, Bangalore", "Symbiosis Institute of Business Management (SIBM)",
            "Tata Institute of Social Sciences (TISS - Criminology)", "University of Delhi (Commerce)", 
            "Amity University (Forensic Science/Finance)", "Various Law Schools",
            "Indian Institute of Banking and Finance (IIBF)", "University of Mumbai"
        ],
        "jobs": [
            "AML Analyst (Anti-Money Laundering)", "KYC Specialist", "Fraud Investigator", "Compliance Officer", 
            "Forensic Accountant", "Risk Manager", "Internal Auditor", "Security Analyst",
            "Financial Crime Consultant", "Regulatory Affairs Officer"
        ],
        "internships": [
            {"role": "AML Intern", "company": "HDFC Bank/HSBC/Financial Institution", "duration": "6 months"},
            {"role": "Compliance Trainee", "company": "FinTech Startup", "duration": "3 months"},
            {"role": "Investigation Assistant", "company": "Accounting/Consulting Firm", "duration": "4 months"}
        ]
    },
]
if len(CAREER_DB) < 10:
    CAREER_DB.extend([
        # Ensure minimum 10 entries for a top 10 list
    ])


# ==========================================================
# 15 Multiple-Choice Questions for Career Fit Analysis
# ==========================================================
QUESTIONS = { 
    1: {"text": "1. APTITUDE: Which core subject do you find most interesting and excel at?", "category": "Aptitude", "options": {"A": "Mathematics/Physics (Logic & Structures)", "B": "Biology/Chemistry (Life & Systems)", "C": "Accounts/Economics (Finance & Trade)", "D": "History/Psychology (People & Society)"}},
    2: {"text": "2. APTITUDE: When faced with a complex problem, what is your preferred approach?", "category": "Aptitude", "options": {"A": "Break it down into a logical, step-by-step code/formula.", "B": "Diagnose the root cause through observation and analysis (like a doctor).", "C": "Assess the financial impact and develop a balanced budget.", "D": "Seek human perspectives and understand the emotional context."}},
    3: {"text": "3. APTITUDE: Which type of entrance exam preparation sounds most appealing?", "category": "Aptitude", "options": {"A": "JEE/BITSAT (Engineering/Architecture)", "B": "NEET/AIIMS (Medical/Allied Sciences)", "C": "CAT/CLAT (Management/Law)", "D": "UPSC/TISS (Civil Services/Social Sciences)"}},
    4: {"text": "4. INTEREST: Which field are you most curious to read articles/news about?", "category": "Interest", "options": {"A": "Artificial Intelligence, Space, New Gadgets.", "B": "Global Health Crises, New Medical Discoveries, Genetics.", "C": "Stock Market, Global Trade, Corporate Mergers.", "D": "Political Events, Human Rights, Literature, Art."}},
    5: {"text": "5. INTEREST: In a school project, what role do you naturally gravitate towards?", "category": "Interest", "options": {"A": "The system architect: designing the core framework and solving technical bugs.", "B": "The researcher: gathering detailed, factual information from primary sources.", "C": "The planner/treasurer: managing budget, timelines, and resources.", "D": "The communicator: presenting the final idea and managing team dynamics."}},
    6: {"text": "6. INTEREST: What kind of activity relaxes you the most?", "category": "Interest", "options": {"A": "Playing strategy games or learning a new programming language.", "B": "Gardening, cooking, or activities involving precise physical craft.", "C": "Creating a personal budget/investment plan or negotiating a good deal.", "D": "Writing, debating, reading a novel, or drawing/designing."}},
    7: {"text": "7. PERSONALITY: How do you prefer to spend your typical workday?", "category": "Personality", "options": {"A": "Working independently on complex problems with clear metrics.", "B": "Hands-on, dealing directly with biological or physical materials/machines.", "C": "In an office environment, leading a team or handling high-stakes negotiations.", "D": "Engaging directly with people: listening, teaching, or advising."}},
    8: {"text": "8. PERSONALITY: How do you handle emotional situations or stress?", "category": "Personality", "options": {"A": "I remain objective and try to find a logical fix (Technical/Analytical).", "B": "I rely on strict protocols and established procedures (Methodical/Structured).", "C": "I take charge and make clear, decisive decisions (Leadership/Decisive).", "D": "I am empathetic and prioritize understanding others' feelings (Caring/Communicative)."}},
    9: {"text": "9. PERSONALITY: Do you prefer a predictable routine or constant change?", "category": "Personality", "options": {"A": "Mostly routine, with challenging, unpredictable problems to solve within the routine.", "B": "Structured, but with critical, high-pressure, moment-to-moment decisions.", "C": "Constantly changing, dynamic environment, especially travel and client meetings.", "D": "A flexible environment that allows for creativity and self-expression."}},
    10: {"text": "10. GOALS: What is your primary career goal?", "category": "Goals & Values", "options": {"A": "To innovate, create new technology, or solve technical global challenges.", "B": "To serve the community directly by improving health or environment.", "C": "To earn a high income and achieve a top leadership position.", "D": "To influence culture, policy, or public opinion."}},
    11: {"text": "11. GOALS: What work setting is your dream?", "category": "Goals & Values", "options": {"A": "A large tech firm, research lab, or modern R&D center.", "B": "A major hospital, clinic, or specialized research institution.", "C": "A financial district, corporate HQ, or startup incubator.", "D": "A university, NGO, media house, or historical site."}},
    12: {"text": "12. GOALS: How important is continuous high-level academic study (e.g., PhD, Specialist Training)?", "category": "Goals & Values", "options": {"A": "Very important, I enjoy deep research and becoming a technical expert.", "B": "Absolutely essential, it's required for practice and specialization (e.g., M.D., M.S.).", "C": "Important for promotions/leadership (e.g., MBA), but not always mandatory.", "D": "Less important; experience and portfolio matter more than degrees."}},
    13: {"text": "13. CONSTRAINTS: What is your preferred academic stream background?", "category": "Constraints", "options": {"A": "Science-A (Physics, Chemistry, Maths) / Technical.", "B": "Science-B (Physics, Chemistry, Biology) / Medical.", "C": "Commerce (Accounts, Economics) / Business.", "D": "Arts / Humanities (History, Psychology) / Social."}},
    14: {"text": "14. CONSTRAINTS: What is your family's budget for higher education (including coaching, etc.)?", "category": "Constraints", "options": {"A": "High (can afford expensive private/foreign education).", "B": "Medium (can afford public/good private institutions).", "C": "Low (prefer government colleges or low-cost options).", "D": "Flexible (willing to take loans for the right course)."}},
    15: {"text": "15. CONSTRAINTS: How much are you willing to invest in the difficulty/length of the course?", "category": "Constraints", "options": {"A": "Very long and hard (e.g., 5-9 years for specialization).", "B": "Long and hard (e.g., 4-6 years of professional degree).", "C": "Medium length and difficulty (e.g., 3-4 year degree with post-grad).", "D": "Shorter courses or diplomas (e.g., 1-2 years)."}},
}
ANSWER_MAP = {
    '1A': {'stream': 'Science-A/PCM', 'aptitude': 'Maths, Logic, Tech'}, '1B': {'stream': 'Science-B/PCB', 'aptitude': 'Biology, Chemistry'}, '1C': {'stream': 'Commerce/Any', 'aptitude': 'Accounts, Economics'}, '1D': {'stream': 'Arts/Any', 'aptitude': 'Human Behaviour, Society'},
    '2A': {'aptitude': 'Maths, Logic, Tech'}, '2B': {'aptitude': 'Biology, Empathy'}, '2C': {'aptitude': 'Finance, Planning'}, '2D': {'aptitude': 'Communication, Empathy'},
    '3A': {'education': 'B.Tech/BE'}, '3B': {'education': 'MBBS, B.Pharm, BDS'}, '3C': {'education': 'BBA, CA, LLB'}, '3D': {'education': 'BA, MA, UPSC'},
    '4A': {'interest': 'Coding, Gadgets, Space'}, '4B': {'interest': 'Healthcare, Research'}, '4C': {'interest': 'Stock Market, Investing'}, '4D': {'interest': 'Media, Arts, Policy'},
    '5A': {'personality': 'Problem-Solver, Problem-Solver'}, '5B': {'personality': 'Methodical, Detail-Oriented'}, '5C': {'personality': 'Leadership, Decisive'}, '5D': {'personality': 'Communicative, Outgoing'},
    '6A': {'interest': 'Coding, Logic'}, '6B': {'interest': 'Physical Craft, Detail-Oriented'}, '6C': {'interest': 'Finance, Negotiation'}, '6D': {'interest': 'Writing, Design, Arts'},
    '7A': {'personality': 'Introvert, Problem-Solver'}, '7B': {'personality': 'Practical, Hands-on'}, '7C': {'personality': 'Leadership, Outgoing'}, '7D': {'personality': 'Caring, Communicative'},
    '8A': {'personality': 'Analytical, Problem-Solver'}, '8B': {'personality': 'Methodical, Responsible'}, '8C': {'personality': 'Decisive, Leadership'}, '8D': {'personality': 'Caring, Empathy'},
    '9A': {'personality': 'Problem-Solver, Technical'}, '9B': {'personality': 'Resilient, Methodical'}, '9C': {'personality': 'Outgoing, Leadership'}, '9D': {'personality': 'Creative, Flexible'},
    '10A': {'topic': 'Engineer, Scientist'}, '10B': {'topic': 'Doctor, Social Worker, Researcher'}, '10C': {'topic': 'CEO, Manager, Investment Banker'}, '10D': {'topic': 'Journalist, Politician, Professor'},
    '11A': {'topic': 'Tech, R&D'}, '11B': {'topic': 'Medical, Health'}, '11C': {'topic': 'Business, Finance'}, '11D': {'topic': 'Arts, Social, Academic'},
    '12A': {'difficulty': 'Hard', 'education': 'PhD'}, '12B': {'difficulty': 'Very Hard', 'education': 'Specialization'}, '12C': {'difficulty': 'Medium-Hard', 'education': 'MBA'}, '12D': {'difficulty': 'Easy', 'education': 'Diploma'},
    '13A': {'stream': 'Science-A/PCM'}, '13B': {'stream': 'Science-B/PCB'}, '13C': {'stream': 'Commerce/Any'}, '13D': {'stream': 'Arts/Any'},
    '14A': {'cost': 'Medium-High'}, '14B': {'cost': 'Medium'}, '14C': {'cost': 'Low'}, '14D': {'cost': 'Flexible'},
    '15A': {'difficulty': 'Very Hard'}, '15B': {'difficulty': 'Hard'}, '15C': {'difficulty': 'Medium'}, '15D': {'difficulty': 'Easy'},
}


class CareerApp(tk.Tk):
    """Main application class for the Career Recommender."""
    def __init__(self):
        super().__init__()
        self.title("PATHPILOT – Database Career Recommender")
        self.geometry("1200x800")
        self.resizable(True, True)
        self.quiz_answers = {}
        self.career_db = CAREER_DB
        
        # --- GUI Setup ---
        self.style = ttk.Style(self)
        self.style.theme_use('clam')
        
        # Define custom colors
        self.bg_color = '#ffffff'  # White background
        self.fg_color = 'black'    # Black foreground text
        self.highlight_color = '#3498db' # Blue highlight
        
        # Custom styles for a 'very good GUI'
        self.style.configure('TLabel', font=('Arial', 12), background=self.bg_color, foreground=self.fg_color)
        self.style.configure('TFrame', background=self.bg_color)
        self.style.configure('TButton', font=('Arial', 12, 'bold'), background=self.highlight_color, foreground='black')
        self.style.map('TButton', background=[('active', '#2980b9')])
        self.style.configure('TQuestion.Label', font=('Arial', 14, 'bold'), background=self.bg_color, foreground=self.fg_color)
        
        # Configure TRadiobutton style 
        self.style.configure('TRadiobutton', background=self.bg_color, foreground=self.fg_color, font=('Arial', 11))
        
        # Color-coding styles for questions (Requirement)
        self.style.configure('Aptitude.TFrame', background='#87CEFA')  # Teal
        self.style.configure('Interest.TFrame', background='#EAD7B7')  # Orange
        self.style.configure('Personality.TFrame', background='#B4CD94')  # Purple
        self.style.configure('Goals & Values.TFrame', background='#FFB6C1') # Red
        self.style.configure('Constraints.TFrame', background='#CC9999') # Dark Grey
        
        # Container for pages
        self.container = ttk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        
        # Initialize pages
        for F in (StartPage, QuizPage, ResultsPage):
            page_name = F.__name__
            frame = F(parent=self.container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name, data=None):
        """Show a frame for the given page name."""
        frame = self.frames[page_name]
        if page_name == "ResultsPage" and data:
            frame.display_results(data)
        frame.tkraise()

    def start_quiz(self):
        self.quiz_answers = {}
        self.show_frame("QuizPage")

    def finish_quiz(self, answers):
        self.quiz_answers = answers
        recommended_careers = self.calculate_fit_score()
        self.show_frame("ResultsPage", data=recommended_careers)

    def calculate_fit_score(self):
        """
        Calculates a fit score for all careers based on the 15 quiz answers.
        Returns a list of the top 5 best-fitting careers.
        """
        user_profile = self.quiz_answers
        scored_careers = []
        
        for career in self.career_db:
            score = 0
            max_score = len(user_profile) * 30  
            
            # --- Scoring Logic ---
            for q_num, user_choice in user_profile.items():
                answer_key = f"{q_num}{user_choice}"
                
                if answer_key in ANSWER_MAP:
                    match_criteria = ANSWER_MAP[answer_key]
                    
                    # 1. Broad Stream/Topic Match (High weight for stream constraint)
                    if 'stream' in match_criteria and match_criteria['stream'] in career['stream']:
                        score += 30 
                    elif 'topic' in match_criteria and any(word in career['topic'] for word in match_criteria['topic'].split(', ')):
                        score += 15

                    # 2. Aptitude/Interest/Personality Match (Medium-High weight)
                    if 'aptitude' in match_criteria and any(attr in career['aptitude'] for attr in match_criteria['aptitude'].split(', ')):
                        score += 10
                    if 'interest' in match_criteria and any(attr in career['interest'] for attr in match_criteria['interest'].split(', ')):
                        score += 10
                    if 'personality' in match_criteria and any(attr in career['personality'] for attr in match_criteria['personality'].split(', ')):
                        score += 10
                        
                    # 3. Constraint/Difficulty/Cost Match (Medium weight)
                    if 'cost' in match_criteria and match_criteria['cost'] in career['cost']:
                        score += 8
                    if 'difficulty' in match_criteria and match_criteria['difficulty'] in career['difficulty']:
                        score += 8

            # Convert to a percentage score
            fit_percentage = round((score / max_score) * 100) if max_score > 0 else 0
            
            scored_careers.append({
                **career, 
                "fit_score": fit_percentage
            })
            
        # Sort by fit score (descending) and return the top 5 (Requested Change)
        scored_careers.sort(key=lambda x: x['fit_score'], reverse=True)
        return scored_careers[:5]


class StartPage(ttk.Frame):
    """The introductory page for the application."""
    def __init__(self, parent, controller):
        super().__init__(parent, style='TFrame')
        self.controller = controller
        
        main_frame = ttk.Frame(self, padding="50", style='TFrame')
        main_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Title
        ttk.Label(main_frame, text="PATHPILOT: AI Career Recommender", font=("Arial", 28, "bold"), 
                  foreground='#191970', background=self.controller.bg_color).pack(pady=20)
        
        # Subtitle
        ttk.Label(main_frame, text="Your personalized guide to 250+ career paths.", font=("Arial", 16), 
                  foreground='#000000', background=self.controller.bg_color).pack(pady=10)
        
        # Description
        description = (
            "This application utilizes a comprehensive local database (as per the Career Handbook) "
            "to provide detailed, data-driven career recommendations.\n\n"
            "Answer 15 multiple-choice questions about your aptitude, interests, and goals to receive a "
            "Fit Score and a top 5 list of careers, complete with 10+ colleges, 10+ jobs, fees, and internships."
        )
        ttk.Label(main_frame, text=description, font=("Arial", 12), justify=tk.CENTER,
                  wraplength=600, background=self.controller.bg_color).pack(pady=30)
        
        # Start Button
        ttk.Button(main_frame, text="START CAREER QUIZ (15 Questions)", 
                   command=controller.start_quiz, style='TButton').pack(pady=40, ipadx=20, ipady=10)


class QuizPage(ttk.Frame):
    """The page for the 15-question career quiz."""
    def __init__(self, parent, controller):
        super().__init__(parent, style='TFrame') 
        self.controller = controller
        self.current_question = 1
        self.answers = {}
        self.v = {}  # Dictionary to hold Radiobutton StringVars for all 15 questions

        # Setup scrollable frame
        self.canvas = tk.Canvas(self, bg=self.controller.bg_color, highlightthickness=0)
        self.scroll_y = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.scroll_y.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.configure(yscrollcommand=self.scroll_y.set)
        
        self.quiz_frame = ttk.Frame(self.canvas, padding="20", style='TFrame')
        self.canvas.create_window((0, 0), window=self.quiz_frame, anchor="nw")
        self.quiz_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        
        # Title
        ttk.Label(self.quiz_frame, text="Career Fit Assessment (15 Questions)", font=("Arial", 20, "bold"), 
                  foreground='#000000', background=self.controller.bg_color).pack(pady=10)
        
        self.create_questions()
        
        # Submit Button
        ttk.Button(self.quiz_frame, text="SUBMIT & GET RESULTS", 
                   command=self.validate_and_submit, style='TButton').pack(pady=40, ipadx=20, ipady=10)

    def create_questions(self):
        """Generates all 15 questions with color-coding."""
        for q_num, q_data in QUESTIONS.items():
            category = q_data['category']
            
            # Use color-coded frame for the question (Requirement)
            q_frame = ttk.Frame(self.quiz_frame, padding="15", style=f'{category}.TFrame')
            q_frame.pack(fill='x', pady=10, padx=10)
            
            # Question Text
            bg_color_lookup = self.controller.style.lookup(f'{category}.TFrame', 'background')
            ttk.Label(q_frame, text=q_data['text'], font=("Arial", 14, "bold"), 
                      foreground='white', background=bg_color_lookup).pack(anchor='w', pady=(0, 10))
            
            # Radiobutton setup
            # The StringVar must be initialized with the frame as its parent
            self.v[q_num] = tk.StringVar(q_frame) 
            
            for option_key, option_text in q_data['options'].items():
                radio_text = f"{option_key}. {option_text}"
                radio = ttk.Radiobutton(q_frame, text=radio_text, variable=self.v[q_num], value=option_key,
                                        style='TRadiobutton')
                radio.pack(anchor='w', padx=15, pady=5)
                # No command is necessary here; selections are read directly on submit.

    def validate_and_submit(self):
        """
        Forcibly collects answers from all StringVars and validates 
        that all 15 questions are answered before submitting.
        """
        # NEW STEP 1: Forcibly update answers from all StringVars (self.v)
        self.answers = {}
        for q_num, var in self.v.items():
            choice = var.get()
            if choice:
                # Store the answer only if a selection was made
                self.answers[int(q_num)] = choice 
        
        # NEW STEP 2: Validation
        answered_count = len(self.answers)
        total_questions = len(QUESTIONS)

        if answered_count != total_questions:
            messagebox.showwarning("Incomplete Quiz", 
                                   f"Please answer all {total_questions} questions before submitting. "
                                   f"Currently answered: {answered_count}.")
            return
        
        # NEW STEP 3: Submission
        # Convert integer keys back to strings for the answer map lookup in finish_quiz
        final_answers = {str(k): v for k, v in self.answers.items()}
        self.controller.finish_quiz(final_answers)


class ResultsPage(ttk.Frame):
    """Page to display the top 5 recommended careers."""
    def __init__(self, parent, controller):
        super().__init__(parent, style='TFrame')
        self.controller = controller
        self.results_data = []

        main_frame = ttk.Frame(self, padding="20", style='TFrame')
        main_frame.pack(fill="both", expand=True)

        ttk.Label(main_frame, text="Your Top 5 Career Recommendations", font=("Arial", 20, "bold"), 
                  foreground='#2ecc71', background=self.controller.bg_color).pack(pady=10)
        
        # Treeview for the list of careers
        columns = ("#", "Career Path", "Fit Score", "Stream", "Cost")
        self.results_tree = ttk.Treeview(main_frame, columns=columns, show='headings', height=5) # Changed height to 5
        
        # Configure Treeview Styles
        self.controller.style.configure('Treeview.Heading', font=('Arial', 12, 'bold'), background='#3498db', foreground='black')
        self.controller.style.configure('Treeview', font=('Arial', 11), rowheight=30, background='#191970', foreground='black')
        
        for col in columns:
            self.results_tree.heading(col, text=col)
            self.results_tree.column(col, width=150, anchor=tk.CENTER)
            
        self.results_tree.column("#", width=50, anchor=tk.CENTER)
        self.results_tree.column("Career Path", width=300, anchor=tk.W)
        self.results_tree.column("Fit Score", width=100, anchor=tk.CENTER)
        
        self.results_tree.bind('<<TreeviewSelect>>', self.show_details_flashcard)
        self.results_tree.pack(fill='x', padx=50, pady=20)
        
        ttk.Label(main_frame, text="Select a career above to view the detailed 'Flash Card' results (10+ Colleges/Jobs).", 
                  font=("Arial", 10, "italic"), foreground='#bdc3c7', background=self.controller.bg_color).pack(pady=5)
        
        # Button to return to Start
        ttk.Button(main_frame, text="RESTART QUIZ", command=lambda: controller.show_frame("StartPage"), style='TButton').pack(pady=20)


    def display_results(self, recommended_careers):
        """Populates the treeview with the top 5 results."""
        self.results_data = recommended_careers
        
        # Clear existing data
        for item in self.results_tree.get_children():
            self.results_tree.delete(item)
            
        # Treeview tags configuration
        self.results_tree.tag_configure('highfit', background='#d4edda', foreground='#155724') # Green
        self.results_tree.tag_configure('medfit', background='#fff3cd', foreground='#856404')  # Yellow
        self.results_tree.tag_configure('lowfit', background='#f8d7da', foreground='#721c24') # Red
            
        # Insert new data
        for i, card in enumerate(self.results_data):
            # Color coding for Fit Score (Good Looking Results)
            tag = 'highfit' if card['fit_score'] >= 75 else ('medfit' if card['fit_score'] >= 50 else 'lowfit')

            self.results_tree.insert('', tk.END, iid=i, tags=(tag,), values=(
                f"#{i+1}", 
                card['topic'], 
                f"{card['fit_score']}%", 
                card['stream'],
                card['cost']
            ))

    def show_details_flashcard(self, event):
        """Displays the detailed results in a new flash card window (Requirement)."""
        selected_item = self.results_tree.focus()
        if not selected_item:
            return

        item_index = int(selected_item)
        card = self.results_data[item_index]
        
        # --- Flash Card Window Setup ---
        detail_window = tk.Toplevel(self.controller, bg=self.controller.bg_color)
        detail_window.title(f"Detailed Card: {card['topic']}")
        detail_window.geometry("800x650")
        
        # Scrollable content area
        canvas = tk.Canvas(detail_window, bg=self.controller.bg_color, highlightthickness=0)
        scroll_y = ttk.Scrollbar(detail_window, orient="vertical", command=canvas.yview)
        scroll_y.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)
        canvas.configure(yscrollcommand=scroll_y.set)
        
        content_frame = ttk.Frame(canvas, padding="20", style='TFrame')
        canvas.create_window((0, 0), window=content_frame, anchor="nw", width=780)
        content_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        
        # Define text styles for detailed output
        def add_line(text, style_tag):
            if style_tag == 'header':
                ttk.Label(content_frame, text=text, font=("Arial", 14, "bold"), foreground='#f1c40f', background=self.controller.bg_color).pack(anchor='w', pady=(15, 5))
            elif style_tag == 'sub_header':
                ttk.Label(content_frame, text=text, font=("Arial", 12, "bold"), foreground='#3498db', background=self.controller.bg_color).pack(anchor='w', pady=(10, 2))
            elif style_tag == 'bullet':
                # Text color is black (self.controller.fg_color)
                ttk.Label(content_frame, text=text, font=("Arial", 11), foreground=self.controller.fg_color, background=self.controller.bg_color, wraplength=740, justify=tk.LEFT).pack(anchor='w', padx=15, pady=1)
        
        
        # --- Flash Card Content ---
        add_line(f"CAREER PATH: {card['topic'].upper()}", "header")
        add_line(f"FIT SCORE: {card['fit_score']}%", "sub_header")
        add_line(f"Description: {card['description']}", "bullet")
        add_line(f"Required Education: {card['education']}", "bullet")
        add_line(f"Aptitude & Personality: {card['aptitude']} / {card['personality']}", "bullet")
        add_line(f"Estimated Fees (Range): {card['fees']} / Cost: {card['cost']} / Difficulty: {card['difficulty']}", "bullet")
        
        add_line("\nTOP COLLEGES (MIN. 10 REQUIRED)", "header")
        for i, college in enumerate(card['colleges'][:10]):
            add_line(f"• {college}", "bullet")

        add_line("\nENTRY-LEVEL JOB ROLES (MIN. 10 REQUIRED)", "header")
        for i, job in enumerate(card['jobs']): 
            add_line(f"• {job}", "bullet")

        add_line("\nINTERNSHIPS / TRAINEE ROLES", "header")
        if card["internships"]:
            for it in card["internships"]:
                add_line(f"• {it['role']} at {it['company']} (Duration: {it['duration']})", "bullet")
        else:
            add_line("• No specific internships extracted.", "bullet")

        
if __name__ == "__main__":
    app = CareerApp()
    app.mainloop()
