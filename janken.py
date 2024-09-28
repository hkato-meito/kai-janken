import random
import tkinter as tk
from tkinter import messagebox

def jyanken(player, computer):
    if player == computer:
        return "あいこ"
    elif (player == "グー" and computer == "チョキ") or \
         (player == "チョキ" and computer == "パー") or \
         (player == "パー" and computer == "グー"):
        return "勝ち"
    else:
        return "負け"

def play(player_choice):
    global player_wins, computer_wins, rounds
    computer_choice = random.choice(choices)
    result = jyanken(player_choice, computer_choice)
   
    rounds += 1
    result_text.set(f"第{rounds}回戦\nあなたの手: {player_choice} {emojis[player_choice]}\nコンピュータの手: {computer_choice} {emojis[computer_choice]}\n結果: {result}")
   
    if result == "勝ち":
        result_label.config(fg="red")
        player_wins += 1
    elif result == "負け":
        result_label.config(fg="blue")
        computer_wins += 1
    else:
        result_label.config(fg="black")
   
    score_text.set(f"現在のスコア - あなた: {player_wins}, コンピュータ: {computer_wins}")
   
    if player_wins == 3:
        messagebox.showinfo("結果", "あなたの優勝です！")
        reset_game()
    elif computer_wins == 3:
        messagebox.showinfo("結果", "コンピュータの優勝です！")
        reset_game()

def reset_game():
    global player_wins, computer_wins, rounds
    player_wins = 0
    computer_wins = 0
    rounds = 0
    result_text.set("")
    score_text.set("現在のスコア - あなた: 0, コンピュータ: 0")

choices = ["グー", "チョキ", "パー"]
emojis = {"グー": "✊", "チョキ": "✌", "パー": "✋"}
player_wins = 0
computer_wins = 0
rounds = 0

root = tk.Tk()
root.title("じゃんけんゲーム")

result_text = tk.StringVar()
score_text = tk.StringVar()
score_text.set("現在のスコア - あなた: 0, コンピュータ: 0")

result_label = tk.Label(root, textvariable=result_text, font=("Helvetica", 18))
result_label.pack()
tk.Label(root, textvariable=score_text, font=("Helvetica", 14)).pack()

frame = tk.Frame(root)
frame.pack()

for choice in choices:
    button = tk.Button(frame, text=f"{choice} {emojis[choice]}", font=("Helvetica", 14), command=lambda c=choice: play(c))
    button.pack(side=tk.LEFT, padx=10)

root.mainloop()
