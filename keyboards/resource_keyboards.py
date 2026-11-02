"""Inline keyboards for Study Resources navigation."""

from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from resources.navigation_data import CBC_PATHWAYS, CURRICULA, KCSE_SUBJECT_GROUPS


def curriculum_keyboard() -> InlineKeyboardMarkup:
    """Build the curriculum selection keyboard."""
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "KCSE Curriculum", callback_data="resources:kcse"
                )
            ],
            [
                InlineKeyboardButton(
                    "CBC Senior School", callback_data="resources:cbc"
                )
            ],
            [InlineKeyboardButton("🏠 Main menu", callback_data="home")],
        ]
    )


def grade_keyboard() -> InlineKeyboardMarkup:
    """Build the CBC grade selection keyboard."""
    levels = list(CURRICULA["cbc"]["levels"].items())
    rows = [
        [
            InlineKeyboardButton(
                title,
                callback_data=f"resources:grade:cbc:{level_key}",
            )
        ]
        for level_key, title in levels
    ]
    rows.extend(
        [
            [
                InlineKeyboardButton(
                    "⬅️ Curricula", callback_data="resources:back:curricula"
                )
            ],
            [InlineKeyboardButton("🏠 Main menu", callback_data="home")],
        ]
    )
    return InlineKeyboardMarkup(rows)


def pathway_keyboard(grade_key: str) -> InlineKeyboardMarkup:
    """Build the CBC pathway selection keyboard for a selected grade."""
    rows = [
        [
            InlineKeyboardButton(
                title,
                callback_data=f"resources:pathway:cbc:{grade_key}:{pathway_key}",
            )
        ]
        for pathway_key, title in CBC_PATHWAYS
    ]
    rows.extend(
        [
            [
                InlineKeyboardButton(
                    "⬅️ Grades", callback_data="resources:back:cbc"
                )
            ],
            [
                InlineKeyboardButton(
                    "⬅️ Curricula", callback_data="resources:back:curricula"
                )
            ],
            [InlineKeyboardButton("🏠 Main menu", callback_data="home")],
        ]
    )
    return InlineKeyboardMarkup(rows)


def kcse_subject_keyboard() -> InlineKeyboardMarkup:
    """Build the KCSE Form 4 subject selection keyboard."""
    subject_rows = [
        [InlineKeyboardButton(title, callback_data=f"resources:subject:kcse:{key}")]
        for group in KCSE_SUBJECT_GROUPS
        for key, title in group["subjects"]
    ]
    subject_rows.extend(
        [
            [
                InlineKeyboardButton(
                    "⬅️ Curricula", callback_data="resources:back:curricula"
                )
            ],
            [InlineKeyboardButton("🏠 Main menu", callback_data="home")],
        ]
    )
    return InlineKeyboardMarkup(subject_rows)


def selected_subject_keyboard() -> InlineKeyboardMarkup:
    """Build navigation controls after a subject has been selected."""
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "⬅️ KCSE subjects", callback_data="resources:back:kcse"
                )
            ],
            [
                InlineKeyboardButton(
                    "⬅️ Curricula", callback_data="resources:back:curricula"
                )
            ],
            [InlineKeyboardButton("🏠 Main menu", callback_data="home")],
        ]
    )
