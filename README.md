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

> _Coming soon: We'll add demo GIFs and screenshots here._

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

```
.
├── main.py
├── app/
│   ├── screens/
│   │   ├── import_screen.py
│   │   └── quote_preview_screen.py
│   └── utils/
│       ├── parser.py
│       └── formatter.py
└── README.md
```

---

## Future Plans

- [ ] Export quotes as styled images
- [ ] Add support for EPUB
- [ ] Social sharing buttons (Twitter, Instagram)
- [ ] Custom themes & quote filters

---

## License

MIT — free to use, fork, and improve.

---

**Crafted with creativity by _Sarkahn A.M._**
