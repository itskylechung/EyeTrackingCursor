## 🧿 Eye-Nose Controlled Screen Switcher

Control your mouse across multiple screens using just your face!
This project uses your **nose position** and **eye location** (via webcam) to detect which monitor you're facing, and moves your mouse to that screen.

A background “Photo Booth” view lets users see their webcam feed for fun or monitoring, and can be toggled to the front when needed.

---

### 🖥️ Features

* 🧠 Face mesh tracking via **MediaPipe**
* 🖱️ Intuitive screen switching via nose position
* 🎥 Optional **Photo Booth** feed window
* 🔀 Supports **multi-monitor setups**
* ⚡ Fast dependency management with [`uv`](https://github.com/astral-sh/uv)

---

### 📦 Requirements

* Python **3.9 – 3.12** (⚠️ Python 3.13 not fully supported yet by some packages)
* `uv` (instead of pip)

Install `uv` if you haven't:

```bash
curl -Ls https://astral.sh/uv/install.sh | sh
```

---

### 🚀 Setup

Clone this project and set up dependencies:

```bash
git clone https://github.com/your-username/eyeball_tracking.git
cd eyeball_tracking
uv venv
source .venv/bin/activate  # or `.venv/Scripts/activate` on Windows
uv pip install -r requirements.txt
```

Or just install directly with `uv add`:

```bash
uv add opencv-python mediapipe pyautogui screeninfo
```

---

### 🏃‍♂️ Run It

```bash
uv run -m src.main
```

* `ESC`: Quit the app
* `P`: Bring the “Photo Booth” window to the front

---

### 📁 File Structure

```
eyeball_tracking/
├── __init__.py       # Monitor detection logic
├── main.py           # Core face-tracking + cursor movement
├── README.md
```

---

### 🔍 Troubleshooting

* **Face tracking not detected**? Make sure you have good lighting and your full face is visible.
* **`screeninfo` not found?** Check for typos: it's `screeninfo`, not `scrreninfo`.
* **Using Python 3.13+?** Some packages like `mediapipe` may not yet support it. Use Python 3.12 or lower.

---

### 📸 Future Ideas

* Add support for **click gestures** (eye blink, mouth open, etc.)
* Enable **snapshot recording** from the Photo Booth
* Add **debounce smoothing** between screens
* Auto-minimize or hide Photo Booth until triggered
* Build a mac/windows app, largely increase accessibility.
