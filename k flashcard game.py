import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random

# List of simple everyday Korean words
words = [
    {"korean": "안녕하세요", "english": "Hello"},
    {"korean": "감사합니다", "english": "Thank you"},
    {"korean": "사랑해요", "english": "I love you"},
    {"korean": "죄송합니다", "english": "Sorry"},
    {"korean": "네", "english": "Yes"},
    {"korean": "아니요", "english": "No"},
    {"korean": "물", "english": "Water"},
    {"korean": "밥", "english": "Rice/Meal"},
    {"korean": "친구", "english": "Friend"},
    {"korean": "학교", "english": "School"},
    {"korean": "사과", "english": "Apple"},
    {"korean": "바나나", "english": "Banana"},
    {"korean": "오렌지", "english": "Orange"},
    {"korean": "포도", "english": "Grape"},
    {"korean": "하늘", "english": "Sky"},
    {"korean": "땅", "english": "Earth"},
    {"korean": "사람", "english": "Person"},
    {"korean": "여자", "english": "Woman"},
    {"korean": "남자", "english": "Man"},
    {"korean": "아이", "english": "Child"},
    {"korean": "책", "english": "Book"},
    {"korean": "연필", "english": "Pencil"},
    {"korean": "학교", "english": "School"},
    {"korean": "선생님", "english": "Teacher"},
    {"korean": "의사", "english": "Doctor"},
    {"korean": "병원", "english": "Hospital"},
    {"korean": "차", "english": "Car"},
    {"korean": "버스", "english": "Bus"},
    {"korean": "기차", "english": "Train"},
    {"korean": "비행기", "english": "Airplane"},
    {"korean": "옷", "english": "Clothes"},
    {"korean": "신발", "english": "Shoes"},
    {"korean": "가족", "english": "Family"},
    {"korean": "집", "english": "House"},
    {"korean": "강", "english": "River"},
    {"korean": "바다", "english": "Sea"},
    {"korean": "산", "english": "Mountain"},
    {"korean": "길", "english": "Road"},
    {"korean": "꽃", "english": "Flower"},
    {"korean": "나무", "english": "Tree"},
    {"korean": "열쇠", "english": "Key"},
    {"korean": "시계", "english": "Clock"},
    {"korean": "전화", "english": "Phone"},
     {"korean": "잘 지내요?", "english": "How are you?"},
    {"korean": "어디에 가세요?", "english": "Where are you going?"},
    {"korean": "뭐 해요?", "english": "What are you doing?"},
    {"korean": "맛있어요!", "english": "It’s delicious!"},
    {"korean": "천천히 말해 주세요.", "english": "Please speak slowly."},
    {"korean": "다시 한 번 해 주세요.", "english": "Please do it again."},
    {"korean": "이해하지 못했어요.", "english": "I didn’t understand."},
    {"korean": "좋아요!", "english": "That’s good!"},
    {"korean": "축하합니다!", "english": "Congratulations!"},
    {"korean": "행복하세요!", "english": "Be happy!"}
]

current_word = {}

def show_random_word():
    """Show a random Korean word and generate three options."""
    global current_word
    current_word = random.choice(words)
    korean_label.config(text=current_word["korean"])
    generate_options()

def generate_options():
    """Generate three English translation options, including the correct one."""
    options = [current_word["english"]]
    while len(options) < 3:
        option = random.choice(words)["english"]
        if option not in options:
            options.append(option)
    random.shuffle(options)

    # Update the option buttons
    option1_button.config(text=options[0], command=lambda: check_answer(options[0]))
    option2_button.config(text=options[1], command=lambda: check_answer(options[1]))
    option3_button.config(text=options[2], command=lambda: check_answer(options[2]))

def check_answer(selected_option):
    """Check if the selected option is correct and provide feedback."""
    if selected_option == current_word["english"]:
        messagebox.showinfo("Correct!", "Well done! That's the right answer.")
    else:
        messagebox.showerror("Incorrect", f"Sorry, the correct answer is: {current_word['english']}")
    show_random_word()  # Show the next word

def start_game():
    """Start the game and display a random word."""
    start_button.pack_forget()  # Hide start button
    title_label.pack_forget()   # Hide title label
    flag_label.pack_forget()    # Hide flag image
    show_random_word()
    korean_label.pack(pady=20)
    option1_button.pack(pady=5)
    option2_button.pack(pady=5)
    option3_button.pack(pady=5)

# Set up the main application window
root = tk.Tk()
root.title("Korean Flashcard Game")
root.geometry("500x500")
root.configure(bg="#f0f8ff")  # Light blue background

# Center the window
window_width = 500
window_height = 500

# Get screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate x and y coordinates for the center
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

# Set the position of the window
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Load the Korean flag image
flag_image = Image.open(r"C:\Users\rbhol\OneDrive\Pictures\Flag-South-Korea.webp")
flag_image = flag_image.resize((300, 200), Image.LANCZOS)
flag_photo = ImageTk.PhotoImage(flag_image)

# Title label
title_label = tk.Label(root, text="Korean Flashcard Game", font=("Comic Sans MS", 24, "bold"), bg="#f0f8ff", fg="#1f3c88")
title_label.pack(pady=20)

# Flag image label
flag_label = tk.Label(root, image=flag_photo, bg="#f0f8ff")
flag_label.pack(pady=10)

# Start button
start_button = tk.Button(root, text="Start", command=start_game, font=("Comic Sans MS", 16), bg="#1f3c88", fg="white", padx=20, pady=10)
start_button.pack(pady=20)

# Korean word label
korean_label = tk.Label(root, text="", font=("Comic Sans MS", 30), bg="#f0f8ff")

# Option buttons
option1_button = tk.Button(root, text="", font=("Comic Sans MS", 16), width=20, bg="#4caf50", fg="white", padx=10, pady=10)
option2_button = tk.Button(root, text="", font=("Comic Sans MS", 16), width=20, bg="#4caf50", fg="white", padx=10, pady=10)
option3_button = tk.Button(root, text="", font=("Comic Sans MS", 16), width=20, bg="#4caf50", fg="white", padx=10, pady=10)

# Run the application
root.mainloop()
