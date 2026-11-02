# Smart Revision Assistant

A Telegram bot starter for a Kenyan secondary-school revision platform.
The bot provides a `/start` welcome message and an inline menu for study
resources, quizzes, student accounts, and project information. Study
Resources lets students choose KCSE Form 4 subjects or select a CBC Senior
School grade and learning pathway. CBC subject lists are intentionally not
shown until each grade/pathway mapping is verified against official
curriculum information.

## Requirements

- Python 3.10 or later
- A Telegram account
- A bot token created using [BotFather](https://telegram.me/BotFather)

## Set up on Windows

Open PowerShell in this project folder and run:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
Copy-Item .env.example .env
```

Open `.env` in VS Code and replace `replace_with_your_bot_token` with the
token provided by BotFather. Keep `.env` private; it is excluded from Git.

If PowerShell prevents virtual-environment activation, allow scripts for only
the current terminal and retry:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

## Run the bot

With the virtual environment active and `.env` configured:

```powershell
python bot.py
```

The bot uses long polling, so the Python process must remain running while
you interact with it. Open your bot in Telegram and send `/start`.

## Current scope

The welcome screen, existing menu options, and curriculum/form/grade
navigation work once a valid token is configured. No examination papers or
other study materials are listed or delivered yet. Student data, a resource
database, payments, and an administrator dashboard are not implemented.

## Code layout

- `bot.py` starts the Telegram application and keeps the welcome menu and
  existing non-resource menu handlers.
- `handlers/resource_handlers.py` handles curriculum, grade, pathway, and
  subject button selections.
- `keyboards/resource_keyboards.py` builds inline keyboards for each
  navigation screen.
- `resources/navigation_data.py` stores KCSE subjects and CBC pathway labels
  outside the callback handler, ready to be replaced or loaded from a
  database later.
- `requirements.txt` lists the Python packages used by the bot.

## Current Study Resources scope

- KCSE navigation is limited to Form 4 and includes a selectable subject
  catalog.
- CBC navigation supports Grades 10, 11, and 12 and the three pathway labels:
  STEM, Social Sciences, and Arts and Sports Science.
- CBC grade/pathway subject combinations are not displayed until their
  official mapping is verified. KICD's Grade 10, Grade 11, and Grade 12
  curriculum design pages are the starting references:
  [Grade 10](https://kicd.ac.ke/cbc-materials/curriculum-designs/grade-ten/),
  [Grade 11](https://kicd.ac.ke/cbc-materials/curriculum-designs/grade-eleven/),
  [Grade 12](https://kicd.ac.ke/cbc-materials/curriculum-designs/grade-twelve/).
- Selecting a subject currently reports that no study materials have been
  uploaded. The bot does not invent or display unavailable documents.
