import random
from datetime import datetime

# Read all compliments
with open("compliments.txt", "r", encoding="utf-8") as file:
    compliments = [line.strip() for line in file]

# Pick a random compliment
today_compliment = random.choice(compliments)
today = datetime.now().strftime("%d %B %Y")

# Read README
with open("README.md", "r", encoding="utf-8") as file:
    readme = file.read()

# Create the new compliment section
new_section = f"""<!-- COMPLIMENT_START -->

## 💖 Today's Compliment

> ✨ **{today_compliment}**

📅 **Last Updated:** {today}

🤖 *Updated automatically using GitHub Actions.*

<!-- COMPLIMENT_END -->"""

# Replace the old section
start = "<!-- COMPLIMENT_START -->"
end = "<!-- COMPLIMENT_END -->"

start_index = readme.find(start)
end_index = readme.find(end) + len(end)

updated_readme = (
    readme[:start_index]
    + new_section
    + readme[end_index:]
)

# Write the updated README
with open("README.md", "w", encoding="utf-8") as file:
    file.write(updated_readme)

print("✅ README updated successfully!")
