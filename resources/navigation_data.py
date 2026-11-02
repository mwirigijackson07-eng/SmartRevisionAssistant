"""Curriculum catalog data kept separate from Telegram navigation logic."""

CURRICULA = {
    "kcse": {
        "title": "KCSE",
        "level_key": "form4",
        "level_title": "Form 4",
    },
    "cbc": {
        "title": "CBC Senior School",
        "levels": {
            "grade10": "Grade 10",
            "grade11": "Grade 11",
            "grade12": "Grade 12",
        },
    },
}

KCSE_SUBJECT_GROUPS = (
    {
        "title": "Languages and mathematics",
        "subjects": (
            ("mathematics", "Mathematics"),
            ("english", "English"),
            ("kiswahili", "Kiswahili"),
        ),
    },
    {
        "title": "Sciences",
        "subjects": (
            ("biology", "Biology"),
            ("chemistry", "Chemistry"),
            ("physics", "Physics"),
        ),
    },
    {
        "title": "Humanities and religious education",
        "subjects": (
            ("geography", "Geography"),
            ("history", "History and Government"),
            ("cre", "Christian Religious Education (CRE)"),
            ("ire", "Islamic Religious Education (IRE)"),
            ("hre", "Hindu Religious Education (HRE)"),
        ),
    },
    {
        "title": "Other examinable subjects",
        "subjects": (
            ("business", "Business Studies"),
            ("agriculture", "Agriculture"),
            ("computer", "Computer Studies"),
            ("home_science", "Home Science"),
            ("art_design", "Art and Design"),
            ("music", "Music"),
            ("french", "French"),
            ("german", "German"),
            ("arabic", "Arabic"),
        ),
    },
)

CBC_PATHWAYS = (
    ("stem", "STEM"),
    ("social_sciences", "Social Sciences"),
    ("arts_sports", "Arts and Sports Science"),
)
