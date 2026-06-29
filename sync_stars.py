import os
import requests
from collections import defaultdict

GH_TOKEN = os.environ.get("GH_TOKEN")
USERNAME = "J1ezds"
HEADERS = {"Authorization": f"token {GH_TOKEN}"} if GH_TOKEN else {}

def get_starred_repos():
    repos = []
    page = 1
    while True:
        url = f"https://api.github.com/users/{USERNAME}/starred?per_page=100&page={page}"
        resp = requests.get(url, headers=HEADERS)
        resp.raise_for_status()
        data = resp.json()
        if not data:
            break
        repos.extend(data)
        page += 1
    return repos

def categorize_by_language(repos):
    lang_map = defaultdict(list)
    for repo in repos:
        lang = repo.get("language") or "Unknown"
        name = repo["full_name"]
        description = repo.get("description") or ""
        html_url = repo["html_url"]
        lang_map[lang].append({
            "name": name,
            "url": html_url,
            "description": description
        })
    return lang_map

def generate_readme(lang_map):
    lines = [
        "# My Starred Projects",
        "",
        f"> Auto-synced starred repositories for @{USERNAME}",
        "",
    ]
    for lang in sorted(lang_map.keys()):
        lines.append(f"## {lang}")
        lines.append("")
        for repo in sorted(lang_map[lang], key=lambda x: x["name"]):
            desc = repo["description"].replace("\n", " ").strip()
            lines.append(f"- [{repo['name']}]({repo['url']}) - {desc}")
        lines.append("")
    return "\n".join(lines)

def main():
    repos = get_starred_repos()
    lang_map = categorize_by_language(repos)
    readme_content = generate_readme(lang_map)
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(readme_content)
    print(f"Generated README.md with {len(repos)} starred repos")

if __name__ == "__main__":
    main()
