"""Callback handlers for the Study Resources navigation."""

from telegram import Update
from telegram.ext import Application, CallbackQueryHandler, ContextTypes

from keyboards.resource_keyboards import (
    curriculum_keyboard,
    grade_keyboard,
    kcse_subject_keyboard,
    pathway_keyboard,
    selected_subject_keyboard,
)
from resources.navigation_data import CBC_PATHWAYS, CURRICULA, KCSE_SUBJECT_GROUPS


def _kcse_subject_title(subject_key: str) -> str | None:
    """Return a known KCSE subject name, or None for unknown callback data."""
    for group in KCSE_SUBJECT_GROUPS:
        for key, title in group["subjects"]:
            if key == subject_key:
                return title
    return None


async def handle_resource_navigation(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    """Render curriculum, grade, pathway, and subject selection screens."""
    query = update.callback_query
    if query is None:
        return

    await query.answer()
    callback_data = query.data or ""

    if callback_data in ("resources", "resources:back:curricula"):
        await query.edit_message_text(
            "📚 Study resources\n\nChoose a curriculum:",
            reply_markup=curriculum_keyboard(),
        )
        return

    if callback_data in ("resources:kcse", "resources:back:kcse"):
        await query.edit_message_text(
            "KCSE · Form 4\n\nChoose a subject you study:",
            reply_markup=kcse_subject_keyboard(),
        )
        return

    if callback_data in ("resources:cbc", "resources:back:cbc"):
        await query.edit_message_text(
            "CBC Senior School\n\nChoose your grade:",
            reply_markup=grade_keyboard(),
        )
        return

    if callback_data.startswith("resources:grade:cbc:"):
        grade_key = callback_data.removeprefix("resources:grade:cbc:")
        grade_title = CURRICULA["cbc"]["levels"].get(grade_key)
        if grade_title:
            await query.edit_message_text(
                f"CBC Senior School · {grade_title}\n\nChoose a learning pathway:",
                reply_markup=pathway_keyboard(grade_key),
            )
            return

    if callback_data.startswith("resources:back:grade:cbc:"):
        grade_key = callback_data.removeprefix("resources:back:grade:cbc:")
        grade_title = CURRICULA["cbc"]["levels"].get(grade_key)
        if grade_title:
            await query.edit_message_text(
                f"CBC Senior School · {grade_title}\n\nChoose a learning pathway:",
                reply_markup=pathway_keyboard(grade_key),
            )
            return

    if callback_data.startswith("resources:pathway:cbc:"):
        parts = callback_data.split(":")
        if len(parts) == 5:
            _, _, _, grade_key, pathway_key = parts
            grade_title = CURRICULA["cbc"]["levels"].get(grade_key)
            pathway_title = dict(CBC_PATHWAYS).get(pathway_key)
            if grade_title and pathway_title:
                await query.edit_message_text(
                    f"CBC Senior School · {grade_title} · {pathway_title}\n\n"
                    "The subject list for this grade and pathway is not "
                    "available yet. It will be added after the official "
                    "KICD grade/pathway mapping is verified. No subject "
                    "combinations or unavailable materials are shown.",
                    reply_markup=pathway_keyboard(grade_key),
                )
                return

    if callback_data.startswith("resources:subject:kcse:"):
        subject_key = callback_data.removeprefix("resources:subject:kcse:")
        subject_title = _kcse_subject_title(subject_key)
        if subject_title:
            await query.edit_message_text(
                f"KCSE · Form 4 · {subject_title}\n\n"
                "No study materials have been uploaded for this subject yet.",
                reply_markup=selected_subject_keyboard(),
            )
            return

    await query.edit_message_text(
        "That selection is not available. Choose where you would like to browse:",
        reply_markup=curriculum_keyboard(),
    )


def register_resource_handlers(application: Application) -> None:
    """Register Study Resources callback routes on the bot application."""
    application.add_handler(
        CallbackQueryHandler(
            handle_resource_navigation,
            pattern=r"^resources(?::.*)?$",
        )
    )
