
# nlp/skill_extractor.py

SKILLS_DB = [

    # Programming Languages
    "python", "java", "c++", "c", "javascript", "typescript",
    "go", "rust", "php",

    # Web Development
    "html", "css", "react", "angular", "vue",
    "node", "express", "flask", "django",
    "spring boot", "fastapi",

    # Databases
    "sql", "mysql", "postgresql", "mongodb",
    "sqlite", "oracle", "redis",

    # Cloud Platforms
    "aws", "azure", "gcp", "firebase",

    # DevOps / Tools
    "docker", "kubernetes", "git", "github",
    "gitlab", "linux", "bash",
    "jenkins", "terraform",

    # Data Science / AI
    "machine learning", "deep learning", "nlp",
    "data science", "pandas", "numpy",
    "matplotlib", "scikit-learn",
    "tensorflow", "pytorch",

    # Big Data
    "hadoop", "spark", "kafka",

    # Testing
    "pytest", "junit", "selenium",

    # Soft Skills
    "problem solving", "communication",
    "teamwork", "leadership"
]


def extract_skills(text: str) -> list:
    """
    Extracts technical and soft skills from text
    based on a predefined skills database.
    """
    text = text.lower()
    found_skills = []

    for skill in SKILLS_DB:
        if skill in text:
            found_skills.append(skill)

    return sorted(list(set(found_skills)))


