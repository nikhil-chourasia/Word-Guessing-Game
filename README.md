# 🕵🏻 Dict-ective – A Word Guessing Game  

Dict-ective is a fun and interactive **word-guessing game** where players reveal letters one by one by making the right guesses. Can you uncover the hidden word and become the ultimate word detective? 🧐✨  

## 🎮 How to Play  
- The game starts by revealing **only the first letter** of a random word.  
- You have to **guess the next letter** correctly to reveal more.  
- Each correct guess **earns +50 points**, and a wrong guess **deducts -10 points**.  
- Keep guessing until you **fully reveal the word**!  

## 🔥 Features  
- ✅ **Dynamic Letter Reveal** – Unlock letters as you guess them correctly.  
- ✅ **Scoring System** – +50 for correct guesses, -10 for wrong ones.  
- ✅ **Progress Bars** – Smooth loading animations for an engaging experience.  
- ✅ **User-Friendly Interface** – Clear prompts and interactive gameplay.  

## 🚀 Installation & Running the Game  
1. Clone the repository or download the files.  
   ```
   git clone https://github.com/your-username/dict-ective.git
   cd dict-ective
   ```
2. Install the required dependencies:  
   ```
   pip install rich art
   ```
3. Run the game:  
   ```
   python main.py
   ```

## 🛠️ Project Structure  
```
📂 dict-ective
 ├── 📜 main.py       # Runs the game and manages user interaction
 ├── 📜 logic.py      # Core game logic for guessing and scoring
 ├── 📜 word_bank.py  # List of words used in the game
 ├── 📜 README.md     # Documentation
 ├── 📜 requirements.txt # Dependencies (rich, art)
```

## 🏆 Example Gameplay  
```
🕵️ Welcome to the Word Guessing Game!

Current Word: a - - - -
Guess the next letter: p
🎉 Correct! Moving to the next letter...

Current Word: a p - - -
Guess the next letter: x
❌ Wrong! Try again.

Current Word: a p - - -
Guess the next letter: p
🎉 Correct! Moving to the next letter...

...
🎉 You guessed the word: APPLE ✅
```

## 📌 To-Do & Future Improvements  
- [ ] Add different difficulty levels.  
- [ ] Implement GUI for more interactive interface.  
- [ ] Introduce a timer for extra challenge.  
- [ ] Add sound effects for a more interactive experience.  
- [ ] Create a multiplayer mode for competitive gameplay.
      
## 🤝 Contributing  
Contributions are welcome! If you have suggestions for improvements, feel free to fork the repository and submit a pull request.  

## 📜 License  
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.  

---

💡 **Built with Python & Love ❤️** – Happy Guessing! 🚀  

