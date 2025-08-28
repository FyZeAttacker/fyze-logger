# Fyze Logger 🔥

A simple, colorful, and stylish Python logger with `fyze` branding.  
Perfect for terminal applications, debugging, and keeping your logs looking **cool**.

---

## 📦 Installation

Clone the repository:
```bash
git clone https://github.com/yourusername/fyze-logger.git
cd fyze-logger
pip install -r requirements.txt
```

Or install via `pip` (once you publish on PyPI):
```bash
pip install fyze-logger
```

---

## 🚀 Usage

```python
from fyze_logger import FyzeLogger

log = FyzeLogger()

log.success("Operation successful!")
log.error("Something went wrong!")
log.debug("Debug info here")
log.warn("This is a warning")
log.ratelimit("Slow down! You're being rate limited")
```

---

## 🖼 Example Output

```
[06:12:00] [Fyze SUCCESS] » Operation successful!
[06:12:00] [Fyze ERROR] » Something went wrong!
[06:12:00] [Fyze DEBUG] » Debug information
[06:12:00] [Fyze WARN] » Warning message
[06:12:00] [Fyze RATELIMIT] » Ratelimit message
```

---

## 📜 Requirements
- Python 3.8+
- `colorama`

---

## 📄 License
MIT License – do whatever you want, just credit **Fyze** ⚡
