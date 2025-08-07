# 🌧️ RainDrops_Graphics_Design & 💡 Circle_Blinker

This repository contains two interactive computer graphics mini-projects developed using **Python** and **PyOpenGL**.



## 📌 Projects Overview

### 🌧️ 1. RainDrops_Graphics_Design

A visually engaging rain simulation over a house scene. The raindrops fall and interact with the house's rooftop, simulating realistic bouncing and sliding behavior. You can also toggle between **day and night modes** and **change rain direction** interactively.

#### 🔧 Features:
- Rainfall simulation with randomized raindrop speeds.
- Raindrops slide off the rooftop after hitting it.
- Day/Night environment toggle.
- Interactive rain direction control.

#### 🎮 How to Play:
| Key             | Action                         |
|----------------|--------------------------------|
| `→` (Right)    | Move rain direction to right   |
| `←` (Left)     | Move rain direction to left    |
| `D` / `d`      | Switch to **Day** mode         |
| `N` / `n`      | Switch to **Night** mode       |

#### 🖼️ Window:
- **Title:** `Rain Simulation`
- **Size:** 500 x 500 px



### 💡 2. Circle_Blinker

An interactive application where you can create bouncing colored points on the screen. These points bounce around within a frame and start **blinking** when you left-click. You can also **freeze/unfreeze** the animation and **adjust point speed**.

#### 🔧 Features:
- Click to add random-colored bouncing points.
- Left-click to make all points blink.
- Pause and resume motion.
- Increase or decrease bouncing speed.

#### 🎮 How to Play:
| Input          | Action                          |
|----------------|---------------------------------|
| **Right Click**| Create a point at cursor        |
| **Left Click** | All points start blinking       |
| `Spacebar`     | Toggle freeze/unfreeze          |
| `↑ Arrow`      | Increase speed                  |
| `↓ Arrow`      | Decrease speed (min: 0.1)       |

#### 🖼️ Window:
- **Title:** `Circle_Blinker`
- **Size:** 600 x 500 px



## 🚀 Getting Started

### ✅ Prerequisites

Ensure Python is installed, then install `PyOpenGL`:

```bash
pip install PyOpenGL PyOpenGL_accelerate
▶️ Running the Projects
To run either project:

bash
Copy
Edit
python RainDrops_Graphics_Design.py
or

bash
Copy
Edit
python Circle_Blinker.py
Make sure the respective file names match your actual files.

📚 Requirements
Python 3.x

PyOpenGL


📄 License
This project is open-source and free to use under the MIT License.
