# 🌌 Star Wars API

> Print all characters of a Star Wars movie in order using the SWAPI REST API and Node.js — asynchronous HTTP requests with recursive chaining.

---

## 📖 Description & Objectives

Given a movie ID as a command-line argument, this script fetches the corresponding Star Wars film from the [SWAPI API](https://swapi-api.hbtn.io/) and prints all character names **in the order they appear** in the API response.

The challenge: API calls are asynchronous, so names must be printed in the correct sequence using **recursive chaining** rather than parallel execution.

**Learning objectives:**
- Consume a REST API with Node.js
- Handle asynchronous callbacks in sequence
- Parse JSON responses and extract nested data

---

## 🛠 Technologies Used

| Tool | Version |
|------|---------|
| Node.js | 14+ |
| Package | `request` |
| API | SWAPI (swapi-api.hbtn.io) |
| Style | semistandard |

---

## ✅ Prerequisites

- OS: Linux / macOS / Windows (WSL)
- Node.js 14 or higher
- npm

---

## ⚙️ Installation

```bash
git clone https://github.com/sagalou/holbertonschool-interview.git
cd holbertonschool-interview/starwars_api
npm install request
chmod +x 0-starwars_characters.js
```

---

## 🚀 How to Use

```bash
./0-starwars_characters.js <movie_id>
```

**Example — Movie 3 (Return of the Jedi):**
```bash
./0-starwars_characters.js 3
```

**Output:**
```
Luke Skywalker
C-3PO
R2-D2
Darth Vader
Leia Organa
...
```

---

## ✨ Features

- Accepts any valid SWAPI movie ID (1–7)
- Preserves character order from the API response
- Graceful error handling for network failures and invalid responses
- Recursive async chaining — no parallel race conditions

---

## 📁 Project Structure

```
starwars_api/
├── 0-starwars_characters.js   # Main script
└── README.md
```

---

## 👤 Author

**Sagal Haider** — [@sagalou](https://github.com/sagalou)  
Holberton School — Cybersecurity track