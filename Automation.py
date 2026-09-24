from datetime import date
import smtplib
import schedule
import time
from email.message import EmailMessage
import os

sender = os.environ["SENDER_EMAIL"]
receiver = os.environ["RECEIVER_EMAIL"]
password = os.environ["GMAIL_APP_PASSWORD"]



def days_until_2027():
    today = date.today()
    new_year = date(2027, 1, 1)

    days_left = (new_year - today).days

    send_email(
        "Countdown to 2027 ⏳",
        f"""2027 is coming! 🚀

You have {days_left} days left until 2027.

Use these days wisely.

Keep learning.
Keep building.
Keep improving.

Make every day count. 🔥
"""
    )


def send_email(subject, message):
    msg = EmailMessage()

    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = receiver

    msg.set_content(message)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(sender, password)
        smtp.send_message(msg)

    print(f"Email sent: {subject}")


# ==========================================
# 7:00 AM - GOOD MORNING
# ==========================================

def morning_routine():
    send_email(
        "Good Morning 🌅",
        """Good morning! ☀️

Start your day properly.

💧 Drink some water.

Take a few minutes to wake up and get ready.

Let's make today productive! 🚀
"""
    )


# ==========================================
# 7:30 AM - ENGLISH + POETRY
# ==========================================

def english_practice():
    send_email(
        "English Practice ✍️",
        """Time to improve your English! 📚

Your task:

✍️ Write a small poem in English.

Don't worry about making it perfect.

Focus on:
• New vocabulary
• Sentence formation
• Creativity
• Expressing your thoughts

Write something every day.

Small practice → Better English. 🚀
"""
    )


# ==========================================
# 8:00 AM - PLAY OR RUN
# ==========================================

def exercise_or_game():
    send_email(
        "Move Your Body 🎮🏃",
        """It's 8:00!

Choose one:

🎮 Play some games

OR

🏃 Go for a run.

Have some fun and get some movement before starting your main work.
"""
    )


# ==========================================
# 8:15 AM - BUILD SOMETHING
# ==========================================

def build_something():
    send_email(
        "BUILD SOMETHING 🔨",
        """8:15 AM — BUILD TIME. 🚀

Stop scrolling.

Stop overthinking.

Start building something.

💻 Code something.
🛠️ Create something.
📚 Learn something useful.
🚀 Work on your project.

The goal is simple:

BUILD SOMETHING TODAY.
"""
    )


# ==========================================
# 6:00 PM - PLAY GAMES IN COLLEGE
# ==========================================

def college_games():
    send_email(
        "Game Time 🎮",
        """6:00 PM 🎮

Time to relax.

Play some games with your friends in college.

Enjoy yourself.

You've worked — now have some fun!
"""
    )


# ==========================================
# 7:00 PM - FOCUS AGAIN
# ==========================================

def evening_focus():
    send_email(
        "FOCUS TIME 🔥",
        """7:00 PM — FOCUS AGAIN.

Game time is over.

Now get back to work.

Choose ONE thing to focus on:

💻 Coding
📚 Learning
🛠️ Building
📖 Studying
🚀 Your project

Put your phone away.

Focus for the next session.

Let's get it done. 🔥
"""
    )


# ==========================================
# DAILY SCHEDULE
# ==========================================
schedule.every().day.at("21:00").do(days_until_2027)
schedule.every().day.at("07:00").do(morning_routine)

schedule.every().day.at("07:30").do(english_practice)

schedule.every().day.at("08:00").do(exercise_or_game)

schedule.every().day.at("08:15").do(build_something)

schedule.every().day.at("18:00").do(college_games)

schedule.every().day.at("19:00").do(evening_focus)





while True:
    schedule.run_pending()
    time.sleep(1)
