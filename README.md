# 📚 Character & Worldbuilding Database

<!-- TABLE OF CONTENTS -->

<details open="open">
  <summary><h2>Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#">Overview</a>
      <ul>
        <li><a href="#">MVP Features</a></li>
      </ul>
    </li>
    <li><a href="#">Tech Stack</a></li>
    <li>
      <a href="#">Installation</a>
      <ul>
        <li><a href="#">Prereq</a></li>
        <li><a href="#">Dev Setup</a></li>
      </ul>
    </li>
    <li><a href="#">Roadmap</a></li>
    <li><a href="#">Contributing</a></li>
    <li><a href="#">Follow</a></li>
    <li><a href="#">License</a></li>
  </ol>
</details>


## 📝 Overview
This is a **mobile-first micro SaaS** tool designed for **worldbuilders, writers and game developers** to **create, organize, and manage characters, worlds, and lore** in a structured, scaleable and searchable way. Built with **Flutter** and **Firebase**, it aims to be an intuitive and accessible tool for creatives of all kinds.

## ✨ MVP Features (Minimum Viable Product)
- 📌 **Character Database** – Store detailed character profiles (name, age, traits, history, relationships)
- 🌍 **Worldbuilding Database** – Track locations, factions, magic systems, and lore elements (MVP supports only single manageable world)
- 🔍 **Search & Filter** – Easily find characters, locations, and important notes
- ☁️ **Cloud Storage** – Sync across devices using Firebase
- 📱 **Mobile-First UI** – Optimized for ease of use on smartphones

## 🏗️ Tech Stack
- **Frontend:** Flutter (Dart)
- **Backend:** Firebase Firestore (Cloud DB)
- **Authentication:** Firebase Auth
- **State Management:** Provider (TBD)
- **Hosting (Future):** Firebase Hosting or Supabase

## 🚀 Installation
### **Prerequisites**
- Install **Flutter**: [Flutter Setup Guide](https://docs.flutter.dev/get-started/install)
- Install **Dart** (comes with Flutter)
- Install **Android Studio** or **VS Code** (for development)
- Clone the repository:
  ```bash
  git clone https://github.com/YOUR_GITHUB_USERNAME/character-worldbuilding-db.git
  cd character-worldbuilding-db
  flutter pub get
  ```

## 🛠️ Development Setup
- **Run the project:**
  ```bash
  flutter run
  ```
- **Connect to Firebase:**
  - Create a Firebase project
  - Add Google Services JSON to `/android/app` (for Android) and `/ios/Runner` (for iOS)

## 📌 Roadmap
- [x] **Week 1:** Base Project setup and Core UI
- [ ] **Week 2:** Build Login Validation Functionality/Authentication 
- [ ] **Week 3:** Build Character & Worldbuilding UI
- [ ] **Week 4:** Local Storage (SQLite integration)
- [ ] **Week 5:** Display & Manage Data
- [ ] **Week 6:** Polish & Prep for Public Launch

## 🤝 Contributing
This is ideally a **solo built project**, but support & contributions are welcome! If you’d like to help:
1. Fork the repo & create a new branch
2. Make your changes & commit with clear messages
3. Submit a PR & describe the update

## 📢 Follow!
Follow me on **[Twitter](https://twitter.com/sarkahnam)** or **[Dev.to](https://dev.to/jamurray)** to connect, chat and see updates!

## ⚖️ License
No License. 
