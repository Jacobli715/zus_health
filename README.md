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

Pygame offers a simple but powerful toolset for building 2D visualizations.

It is intuitive and easy to prototype game logic.

Python’s readability supports clean, structured code for algorithms and movement logic.

While this could be implemented in HTML/CSS/JS, Python provided a more natural workflow for simulation-heavy behavior.

✅ Pros
The Pygame UI clearly visualizes rook movement and state changes.

The Roll button makes the simulation interactive and turn-based.

Easy to extend with new pieces, rules, animations, or improved UI.

Movement logic, UI, and game state are cleanly separated.

Great educational example combining probability, game loops, and OOP.

❌ Cons
UI customization in Pygame is limited compared to full game engines.

Adding many sprites or animations may reduce performance.

Pygame (and Python in general) is slower than languages like C++ for large-scale simulations.

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

