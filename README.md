# Rook Survival Chess Simulation

This project simulates a simplified chess scenario where a rook attempts to survive 15 rounds while moving according to randomized rules, while a stationary bishop tries to capture it using standard diagonal movement. The entire simulation is visualized using **Pygame** and includes interactive UI controls such as a Roll button and a Restart button.

---

## 🎮 How to Play

1. Install Pygame:
   ```bash
   pip3 install pygame
Run the program and click ROLL to begin each round.

The bishop is always stationed at c3.

The rook starts at h1, and each round:

A coin flip determines its movement direction

Heads → moves upward

Tails → moves right

The sum of two dice rolls determines how many squares it moves.

Movement wraps around the board (top → bottom, right → left).

The rook must survive 15 rounds without being captured.

Enjoy the simulation and see if the rook makes it!

🧠 Why Python?
Python was chosen because:
Python was selected because when I first think of chess, I think of game and when coding a game simulation, the first thing that came to my mind was Pygame. Initially I was going to code this in HTML/CSS/JS but I just wanted to build it in python since it has more relevance and easier to use

✅ Pros
1. The Pygame feature and UI shows how the rock moves
2. The roll button creates a interaction experience with the user
3. Easy to add more feature and pieces for future references

❌ Cons
1. There is limited UI designs and adding more features and sprites could drop the performance
2. It is not suited for large simulation and is slower than other langauge such as C++

🖼️ Sample Run
🕹️ Example Rounds
### **Round 1**
<img src="https://github.com/user-attachments/assets/e73e216f-b962-4d2b-995c-d6eeb619108a" width="650" />

### **Round 2**
<img src="https://github.com/user-attachments/assets/7fbc6e21-9982-43a8-b0e7-2f019d50a083" width="650" />

### **Round 3**
<img src="https://github.com/user-attachments/assets/99d33349-6e7e-4ef0-98b5-15330ef803b9" width="650" />

### **Round 4**
<img src="https://github.com/user-attachments/assets/164116d4-d5e3-4266-b5d9-e1bbb5a029c4" width="650" />

### **Round 5**
<img src="https://github.com/user-attachments/assets/286b6443-7d1d-4e20-a08c-7a9416c34fc7" width="650" />

### **Round 6**
<img src="https://github.com/user-attachments/assets/3e74204d-7162-4f4f-9cfd-956793d48d55" width="650" />

### **Round 7**
<img src="https://github.com/user-attachments/assets/0c159e68-b89d-4e16-b2cb-326a27a3383c" width="650" />

