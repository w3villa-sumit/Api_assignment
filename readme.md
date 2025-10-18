Got it, Papa. Here’s an updated version of your README that **includes the AniList GraphQL anime fetcher** alongside the Pokémon REST API fetcher — fully formatted, professional, and easy to read:

---

# 🧩 API Fetcher Collection

This repository contains **Python scripts** that dynamically fetch data from public APIs — **PokeAPI** (REST) for Pokémon and **AniList** (GraphQL) for anime.
It demonstrates API requests, response handling, error management, and filtered output display.

---

## 📘 Overview

### 1️⃣ Pokémon API Fetcher (REST)

Fetches Pokémon details using the **[PokeAPI REST API](https://pokeapi.co/)**.
Users can input a Pokémon name to get both:

* **Raw JSON response**
* **Filtered summary** (name, height, and weight)

Handles invalid inputs gracefully.

### 2️⃣ AniList Anime Fetcher (GraphQL)

Fetches anime details from **[AniList GraphQL API](https://anilist.gitbook.io/api-v2/)**.
Users can:

* Search for a specific anime by **title**
* Fetch a list of **popular anime**

Displays:

* **Raw JSON response**
* **Filtered summary** (title, English title, episodes, format)

Also demonstrates handling GraphQL query errors.

---

## ✨ Features

* **🔹 Dynamic Input:** Enter Pokémon or anime name at runtime.
* **🔹 Popular Anime:** Fetch top `n` popular anime using AniList.
* **🔹 Raw JSON Output:** See full API response.
* **🔹 Filtered Output:** Only key fields displayed for readability.
* **🔹 Error Handling:** Gracefully handles invalid input, malformed queries, or failed requests.
* **🔹 REST vs GraphQL:** Demonstrates the difference between fixed REST endpoints and flexible GraphQL queries.

---

## ⚙️ Requirements

* **Python 3.x**
* **requests** library

---

## 🧱 Setup Instructions

1. **Create a virtual environment:**

   ```bash
   python -m venv .venv
   ```

2. **Activate the environment:**

   ```bash
   source .venv/bin/activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

---

## 💻 Example Usage

Run the script:

```bash
python pokemon.py
python anime.py
```

## 🧠 How It Works

### Pokémon API (REST)

1. **User Input:** Prompt for a Pokémon name.
2. **API Request:** GET request to `https://pokeapi.co/api/v2/pokemon/{name}`
3. **Response Processing:**

   * `200` → Print status, raw JSON, and filtered summary.
   * `404` → Print error message.
4. **Function:** `fetch_pokemon(name)` handles fetching, parsing, and displaying.

### AniList API (GraphQL)

1. **User Input:** Prompt for query type (`anime` or `popular`) and relevant details.
2. **API Request:** POST request to `https://graphql.anilist.co` using GraphQL queries with **variables**.
3. **Response Processing:**

   * Check for `errors` key in JSON.
   * Extract and display relevant fields: `title`, `english`, `episodes`, `format`.
4. **Functions:**

   * `fetch_anime(title)` – search by anime title
   * `fetch_popular_anime(num)` – get popular anime

---

## 💻 Example Usage

### Pokémon

```
Enter Pokémon name: pikachu
Status code: 200
Filtered Output:
Name: pikachu
Height: 4
Weight: 60
```

### Anime

```
Enter query type (anime or popular): anime
Enter anime title (e.g., Naruto): Naruto
Status code: 200
Filtered Output:
Anime: Naruto (English: Naruto, Episodes: 220, Format: TV)
```

```
Enter query type (anime or popular): popular
Enter number of anime (e.g., 3): 3
Status code: 200
Filtered Output:
1. One Piece (English: One Piece, Episodes: 1000+, Format: TV)
2. Attack on Titan (English: Attack on Titan, Episodes: 75, Format: TV)
3. Demon Slayer (English: Demon Slayer: Kimetsu no Yaiba, Episodes: 26, Format: TV)
```

---

## 🔍 REST vs GraphQL Comparison

| Concept           | REST                                         | GraphQL                               |
| ----------------- | -------------------------------------------- | ------------------------------------- |
| **Structure**     | Multiple endpoints with predefined responses | Single endpoint with flexible queries |
| **Data Fetching** | Over-fetching / under-fetching common        | Fetch exactly what’s needed           |
| **Pagination**    | Often required                               | Built-in with more control            |
| **Efficiency**    | Larger payloads                              | Smaller, targeted payloads            |

> For Pokémon, REST works fine.
> For anime, GraphQL is more efficient — only requesting the fields you need.

---

## 📝 Notes

* **Internet connection required** for API access.
* **No authentication** needed.
* **Raw JSON** can be large; filtered output is for readability.
* Demonstrates **error handling** for invalid names or queries.

---
