# 🎮 Memory Game

A fun and colorful memory card matching game built with Python and Tkinter, featuring multiple cute themes!

## ⚡ **Quick Start**
```bash
./START.sh    # One command - that's it! 🚀
```

## 🎯 Features

- **4 Different Themes**: Choose from Jelly, Cats, Food, or Bunny cards
- **Beautiful UI**: Colorful interface with smooth animations  
- **Memory Challenge**: Match pairs of cards in a 4x4 grid
- **Restart Option**: Play again with shuffled cards
- **Theme Selection**: Easy navigation between different card themes

## 🚀 Quick Start

### 🎯 **One-Click Launch** (Recommended)
```bash
./START.sh
```
*That's it! The script will handle everything automatically.*

### 🛠️ Manual Setup (Advanced)
```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate  # On macOS/Linux
# or
venv\Scripts\activate     # On Windows

# Install dependencies
pip install -r requirements.txt

# Run the game
python3 memory_game.py
```

## 🎮 How to Play

1. **Start the Game**: Click "Start" on the main menu
2. **Choose Theme**: Select from Jelly, Cats, Food, or Bunny themes
3. **Match Cards**: Click on cards to flip them and find matching pairs
4. **Win**: Match all pairs to complete the game!
5. **Play Again**: Use "Play Again" or return to theme selection

## 📋 Requirements

- Python 3.6 or higher
- Pillow (PIL) for image handling
- Tkinter (usually included with Python)

## 📁 Project Structure

```
```
memory_game/
├── 🚀 START.sh                    # 🎯 ONE-CLICK LAUNCHER
├── 📄 README.md                   # Complete documentation
├── 📄 requirements.txt            # Python dependencies
├── 🎮 memory_game.py             # Main game file
├── 📁 assets/
│   └── 📁 images/
│       ├── 📁 themes/
│       │   ├── 🍯 jelly/         # Jelly theme cards (8 files)
│       │   ├── 🐱 cats/          # Cat theme cards (8 files)
│       │   ├── 🍔 food/          # Food theme cards (8 files)
│       │   └── 🐰 bunny/         # Bunny theme cards (8 files)
│       └── 📁 ui/
│           └── back.png          # Card back image
├── 📁 scripts/                   # All Python utilities
│   ├── run_game.py              # Alternative launcher
│   ├── test_setup.py            # Setup validation
│   └── setup.py                 # Package configuration
└── 📁 venv/                      # Virtual environment (auto-created)
```
```

## 🎨 Themes

- **🍯 Jelly**: Colorful jelly bean cards
- **🐱 Cats**: Adorable cat illustrations
- **🍔 Food**: Delicious food items
- **🐰 Bunny**: Cute bunny characters

### 🛠️ Development & Testing

**Development Tools:**
```bash
python3 scripts/test_setup.py    # Validate installation
python3 scripts/run_game.py      # Alternative launcher  
python3 scripts/setup.py         # Package configuration
```

**Add New Themes:**
1. Create folder in `assets/images/themes/`
2. Add 8 unique card images (theme1.png to theme8.png)
3. Add corresponding functions in `memory_game.py`

**Customize:**
- **Colors**: Modify tkinter widget configurations
- **Sound**: Integrate pygame for audio effects
- **Difficulty**: Adjust grid size or add timer

## 🐛 Troubleshooting

- **Permission denied**: Run `chmod +x START.sh` to make executable
- **Python not found**: Install Python 3 from [python.org](https://python.org)
- **Images not loading**: Verify files are in `assets/images/` subdirectories
- **Dependencies failed**: Check internet connection for pip install

## 📝 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Feel free to fork this project and submit pull requests for improvements!

---

## 🎯 **Why This Structure?**

- **🚀 START.sh**: One-click launcher at root level - no confusion!
- **🎮 memory_game.py**: Main game file easily identifiable
- **📁 scripts/**: ALL Python utilities tucked away but accessible
- **📁 assets/**: Images organized by theme for easy management
- **🧹 Ultra-Clean Root**: Only 6 items at root level - maximum clarity!

**Enjoy the game!** 🎉