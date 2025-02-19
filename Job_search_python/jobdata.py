# 'pip install pandas' if Pandas is not installed #
# pip install openpyxl' to install export to excel#
import pandas as pd

# Convert data into a structured dictionary with lists
data = {
    "Company Name": [
        "Dexian", "Omnidian", "SafelyYou", "Accounting Seed", "Charlie Health",
        "Restaurant365", "Comply", "Aquatic Informatics", "Robert Half",
        "Advanced Cloud Solutions", "Sparus Holdings", "TEKsystems", "onX",
        "Tracker RMS", "CorVel", "CorVel", "NTT DATA", "Ascendion",
        "Centene Corporation", "Headway", "AbsenceSoft", "Affirm", "Angi",
        "Patterned Learning AI", "Cloud and Things", "Eventbrite",
        "Synergistic IT", "SafelyYou"
    ],
    "Job Title": [
        "Salesforce Admin", "Salesforce Admin", "Salesforce Admin", "IT/Salesforce Support Admin", "Salesforce Admin",
        "Salesforce Admin", "Salesforce Admin", "Salesforce Admin/BI", "Salesforce Admin",
        "Project Manager/Salesforce Specialist", "IT Support Specialist", "Salesforce Admin", "General Consideration - Engineering",
        "Data Analyst & Developer", "Data Entry Analyst", "Data Entry Analyst (Advanced Role)", "Junior Google Cloud Platform Data Analyst",
        "Data Analyst", "Data Analyst II Healthcare Analytics", "Data Analyst", "Data Analyst", "Analyst II, Go-To-Market Operations & Analytics",
        "Product Analyst", "Junior Application Support Analyst (SQL)", "Data Analyst", "Data Analyst", "Data Analyst", "Salesforce Admin"
    ],
    "Industry": [
        "IT Staffing", "Renewable Energy", "Healthcare Tech", "Accounting Software", "Healthcare",
        "Restaurant SaaS", "Compliance Tech", "Water Data Tech", "IT Staffing",
        "Cloud Consulting", "IT Support", "IT Staffing", "Outdoor Navigation / Tech",
        "Software Development", "Healthcare / Risk Management", "Healthcare / Risk Management", "IT Services / Consulting",
        "IT Consulting", "Healthcare", "Mental Health Tech", "HR Software", "Fintech", "Home Services",
        "AI & Machine Learning", "IT Services", "Event Technology", "IT Training & Placement", "Healthcare Tech"
    ],
    "Application Date": ["2025-02"] * 28,  # Same date for all
    "Response Received": [
        "No response", "No response", "No response", "No response", "No response",
        "No response", "No response", "No response", "No response",
        "No response", "No response", "Connected with recruiter", "No response",
        "No response", "No response", "No response", "No response",
        "Rejected", "No response", "No response", "No response", "No response",
        "No response", "No response", "No response", "No response", "No response", "No response"
    ],
    "Things Liked": [
        "Remote, stable role", "Mission-driven, hybrid work", "Focus on Alzheimer's & Dementia care", "SaaS-based, remote", "Mental health mission, growing company",
        "SaaS experience, admin-heavy role", "Remote, strong process-oriented role", "Unique industry, BI exposure", "Big name, staffing network",
        "Consulting role, Salesforce-heavy", "Hybrid in Missoula, IT-focus", "Local recruiter, staffing network", "Emphasis on continuous learning, engineering growth potential, outdoor tech focus",
        "Blend of SQL and JavaScript work, chance to develop technical and analytical skills", "Strong data accuracy focus, structured workflows, HIPAA compliance exposure",
        "More advanced data work, aligns with experience in user investigations and data retention", "Exposure to Google Cloud Platform, SQL-heavy role, opportunity to work with Looker and data warehousing",
        "Tech consulting opportunities", "Healthcare analytics, mission-driven work", "Mental health accessibility, mission-driven", "Operational data analysis, troubleshooting",
        "Data-driven decision-making in fintech", "Product analytics, user experience research", "SQL-heavy role, exposure to AI-driven development",
        "Government IT projects, claims data analysis", "Customer insights, analytics for event management", "Career development support, SQL-focused role", "Focus on Alzheimer's & Dementia care"
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Print first few rows
print(df.head())

# export to excel
df.to_excel("job_applications.xlsx", index=False, engine='openpyxl')

