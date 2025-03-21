# Raevyn - Worldbuilding Mobile App

## 📌 Overview

Raevyn is a **mobile-first worldbuilding application** **tool **designed for writers, game developers, and RPG enthusiasts. Built with **Python and Kivy**, this app allows users to create, manage, and visualize fictional worlds on **Android and iOS**. The goal is to provide an easy-to-use, **offline-friendly** tool for organizing lore, maps, characters, and more.

## 🚀 Features

- **📜 World Creation**: Build and categorize worlds, continents, cities, factions, and more.
- **🗺️ Interactive Maps**: Upload and annotate custom maps.
- **📖 Character & Story Management**: Create characters with detailed profiles and story timelines.
- **📚 Customizable Entries**: Users can add rich text, images, and links between elements.
- **📂 Export & Backup**: Save your worlds as JSON, SQLite, or cloud storage integration (future feature).
- **🎨 Theming & UI Customization**: Dark mode and customizable UI elements.
- **📱 Mobile-First**: Optimized for Android and iOS with **offline capabilities**.

## 🛠️ Tech Stack

- **Python** (Core logic)
- **Kivy** (GUI framework for mobile apps)
- **SQLite** (Local database storage)
- **Buildozer** (Packaging for Android APK)
- **Plyer** (Accessing mobile-specific features)

## 📲 Installation

### **For Android (Termux Setup)**

1. Install **[Termux](https://f-droid.org/packages/com.termux/)** from F-Droid.
2. Update and install dependencies:
   ```bash
   pkg update && pkg upgrade -y
   pkg install python git clang make libffi-dev openssl ndk-mesa sqlite
   pip install kivy kivymd cython buildozer sqlite-utils
   ```
3. Clone the repository:
   ```bash
   git clone https://github.com/YourUsername/Raevyn.git
   cd Raevyn
   ```
4. Run the application:
   ```bash
   python main.py
   ```

### **For Android APK (Using Buildozer)**

1. Initialize Buildozer:
   ```bash
   buildozer init
   ```
2. Edit `buildozer.spec` (set `android.api = 31` or latest available version).
3. Build the APK:
   ```bash
   buildozer -v android debug
   ```
4. Install the APK on your phone:
   ```bash
   adb install bin/*.apk
   ```

Roadmap

Phase 1: MVP Development (Weeks 1-5)

Week 1: Environment Setup & Basic UI

Set up project repository

Configure Termux / Pydroid3 for mobile development

Install dependencies and test basic Python scripts

Implement a basic UI layout with Kivy (home screen, navigation)

Week 2: Core Data Structures & Database Integration

Design the database schema (Worlds, Characters, Locations, etc.)

Implement basic CRUD operations using SQLite

Create an in-app world creation form

Week 3: Implementing World & Entity Management

Develop functionality for adding/editing/deleting worlds

Implement character and location management

Create simple data storage and retrieval system

Week 4: UI Enhancements & Offline Support

Improve UI layout for a better mobile experience

Implement local storage for offline usage

Add user-friendly notifications and feedback messages

Week 5: Finalizing MVP & Testing

Conduct extensive testing on Android

Fix major bugs and optimize performance

Document MVP version and prepare for next phase

Phase 2: Expansion & Cloud Sync (Weeks 6-10)

Implement cloud storage using Firebase

Add user authentication and profile management

Improve UI/UX with animations and better navigation

Allow collaboration and export options

Phase 3: Monetization & Scaling (Weeks 11+)

Develop a monetization model (subscriptions, one-time purchase, ads)

Optimize performance for larger world databases

Launch beta version and collect user feedback

Prepare for full release on Google Play / App Store


## 🤝 Contributing

Want to help improve **raevyn**? Feel free to link up with me on X and hash out ideas. My DMs are open.

## 📜 License

License - None

## 🌐 Links

- **GitHub Repository**: [https://github.com/j-alexandremurray/raevyn](https://github.com/j-alexandremurray/raevyn)
- **Developer Blog**: [https://dev.to/jamurray](https://dev.to/jamurray)
- **Twitter/X Updates**: [https://x.com/SarkahnAm](https://x.com/SarkahnAm)
- **Medium Blog:** [https://medium.com/@JAMurray\_Tech](https://medium.com/@JAMurray_Tech)

