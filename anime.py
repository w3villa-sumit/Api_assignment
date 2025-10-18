import requests
import json

GRAPHQL_ENDPOINT = "https://graphql.anilist.co"

def pretty_print_json(response):
    raw_json = response.json()
    print("Raw JSON:")
    print(json.dumps(raw_json, indent=4))
    return raw_json

def fetch_anime(title):
    query = """
    query ($title: String) {
      Media(search: $title, type: ANIME) {
        title {
          romaji
          english
        }
        episodes
        format
      }
    }
    """
    variables = {"title": title}
    response = requests.post(GRAPHQL_ENDPOINT, json={"query": query, "variables": variables})
    print(f"Status code: {response.status_code}")
    raw_json = pretty_print_json(response)
    
    if "errors" in raw_json:
        print("Error:", raw_json["errors"][0]["message"])
        return

    data = raw_json.get('data', {}).get('Media')
    if not data:
        print("Anime not found.")
        return

    title_romaji = data['title']['romaji']
    title_english = data['title'].get('english') or "N/A"
    episodes = data.get('episodes') or "Unknown"
    format_type = data.get('format') or "Unknown"

    print(f"\nFiltered Output:\nAnime: {title_romaji} (English: {title_english}, Episodes: {episodes}, Format: {format_type})")


def fetch_popular_anime(num_anime):
    query = """
    query ($num: Int) {
      Page(perPage: $num) {
        pageInfo {
          total
          hasNextPage
        }
        media(type: ANIME, sort: POPULARITY_DESC) {
          title {
            romaji
            english
          }
          episodes
          format
        }
      }
    }
    """
    variables = {"num": num_anime}
    response = requests.post(GRAPHQL_ENDPOINT, json={"query": query, "variables": variables})
    print(f"Status code: {response.status_code}")
    raw_json = pretty_print_json(response)

    if "errors" in raw_json:
        print("Error:", raw_json["errors"][0]["message"])
        return

    media_list = raw_json.get('data', {}).get('Page', {}).get('media', [])
    if not media_list:
        print("No popular anime found.")
        return

    print("\nFiltered Output:")
    for i, anime in enumerate(media_list, 1):
        title_romaji = anime['title']['romaji']
        title_english = anime['title'].get('english') or "N/A"
        episodes = anime.get('episodes') or "Unknown"
        format_type = anime.get('format') or "Unknown"
        print(f"{i}. {title_romaji} (English: {title_english}, Episodes: {episodes}, Format: {format_type})")


def main():
    query_type = input("Enter query type (anime or popular): ").strip().lower()
    if query_type == "anime":
        title = input("Enter anime title (e.g., Naruto): ").strip()
        fetch_anime(title)
    elif query_type == "popular":
        try:
            num = int(input("Enter number of anime (e.g., 3): ").strip())
            fetch_popular_anime(num)
        except ValueError:
            print("Invalid number.")
    else:
        print("Invalid query type.")

    # Demonstrate malformed query handling
    print("\n--- Error Demonstration ---")
    error_query = "{ invalid }"
    error_response = requests.post(GRAPHQL_ENDPOINT, json={"query": error_query})
    error_json = error_response.json()
    if "errors" in error_json:
        print("Error from malformed query:", error_json["errors"][0]["message"])
    else:
        print("Malformed query response:", json.dumps(error_json, indent=4))


if __name__ == "__main__":
    main()
