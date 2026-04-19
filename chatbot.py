import json

# Load saved website content
with open("college_data.json", "r", encoding="utf-8") as file:
    college_data = json.load(file)

# Restricted topics
restricted_keywords = [
    "fees",
    "fee",
    "hostel fee",
    "hostel fees",
    "payment",
    "scholarship",
    "room availability",
    "hostel room"
]


def get_response(user_message):
    question = user_message.lower()

    # Restrict certain questions
    for keyword in restricted_keywords:
        if keyword in question:
            return (
                "For the latest information regarding fees, hostel charges, "
                "scholarships, payment details, or room availability, "
                "please contact the college office or visit the office room directly."
            )

    # Search through website text
    for item in college_data:
        content = item["content"].lower()

        if any(word in content for word in question.split()):
            return (
                "Maroon: Based on the information available on the college website, "
                + item["content"][:700]
                + "..."
            )

    return (
        "Maroon: I could not find verified information for that question on the college website. "
        "Please contact the college office for further assistance."
    )