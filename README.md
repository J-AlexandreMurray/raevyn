# Raevyn, an eBook Social Share MVP

A minimalist KivyMD app that lets you **import eBook text**, automatically **extract quotes**, and preview them in a scrollable, mobile-friendly layout. Ideal for authors, readers, and marketers who want to create shareable content from books.

---

## Features

- **Import Options:**
  - Paste text manually
  - Load `.txt` files

- **Quote Extraction:**
  - Auto-splits text into tweet-sized snippets (≤ 280 characters)
  - Displays in styled cards, perfect for visual feedback

- **Simple Navigation:**
  - Import ➝ Preview ➝ Back (MVP Flow)

---

## Screenshots

> _Coming soon: I'll add demo GIFs and screenshots here._

---

## Tech Stack

- [Python 3.10+](https://www.python.org/)
- [KivyMD](https://github.com/kivymd/KivyMD)
- Mobile-first design

---

## Getting Started

```bash
# Clone this repo
$ git clone https://github.com/yourname/ebook-social-share.git
$ cd ebook-social-share

# (Optional) Create a virtual environment
$ python -m venv venv
$ source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
$ pip install -r requirements.txt

# Run the app
$ python main.py
```

---

## Project Structure

ebook_social_share/
├── main.py
├── app/
│   ├── __init__.py
│   ├── screens/
│   │   ├── import_screen.py
│   │   ├── quote_preview_screen.py
│   │   ├── image_generator.py
│   ├── utils/
│   │   ├── parser.py         # EPUB/TXT parsing
│   │   ├── formatter.py      # Quote extraction & trimming
│   │   ├── image_utils.py    # Quote card generator using Pillow
│   │   ├── hashtags.py       # Genre/theme-based hashtag generation
├── assets/
│   ├── fonts/
│   ├── images/
├── README.md
├── requirements.txt


---

## Future Plans

- [ ] Export quotes as styled images
- [ ] Add support for EPUB, Docx, and PDF
- [ ] Social sharing buttons (Twitter, Instagram)
- [ ] Custom themes & quote filters

---

## License

MIT — free to use, fork, and improve.

---

**Crafted with creativity by _Sarkahn A.M._**
