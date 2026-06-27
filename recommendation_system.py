print("======================================")
print("     MOVIE RECOMMENDATION SYSTEM")
print("======================================")
movies = {
    "action": [
        "KGF Chapter 2",
        "Pushpa",
        "RRR",
        "Salaar",
        "Leo"
    ],
    "comedy": [
        "Jathi Ratnalu",
        "F2",
        "MAD",
        "DJ Tillu",
        "Bhale Bhale Magadivoy"
    ],
    "romance": [
        "Sita Ramam",
        "Hi Nanna",
        "Geetha Govindam",
        "Majili",
        "Love Story"
    ],
    "horror": [
        "Virupaksha",
        "Masooda",
        "Kanchana",
        "Arundhati",
        "Pizza"
    ],
    "thriller": [
        "Hit",
        "Agent Sai Srinivasa Athreya",
        "Drishyam",
        "Evaru",
        "Rakshasudu"
    ]
}
print("\nAvailable Categories:")
print("- Action")
print("- Comedy")
print("- Romance")
print("- Horror")
print("- Thriller")
choice = input("\nEnter your favorite movie category: ").lower()
if choice in movies:
    print("\nRecommended Movies:\n")
    for movie in movies[choice]:
        print("★", movie)
else:
    print("\nSorry! Category not available.")