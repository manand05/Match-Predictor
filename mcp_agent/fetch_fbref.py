from playwright.sync_api import sync_playwright
import os

# All your season URLs
season_urls = {
    # "15-16": "https://fbref.com/en/comps/9/2015-2016/schedule/2015-2016-Premier-League-Scores-and-Fixtures",
    # "16-17": "https://fbref.com/en/comps/9/2016-2017/schedule/2016-2017-Premier-League-Scores-and-Fixtures",
    # "17-18": "https://fbref.com/en/comps/9/2017-2018/schedule/2017-2018-Premier-League-Scores-and-Fixtures",
    # "18-19": "https://fbref.com/en/comps/9/2018-2019/schedule/2018-2019-Premier-League-Scores-and-Fixtures",
    # "19-20": "https://fbref.com/en/comps/9/2019-2020/schedule/2019-2020-Premier-League-Scores-and-Fixtures",
    # "20-21": "https://fbref.com/en/comps/9/2020-2021/schedule/2020-2021-Premier-League-Scores-and-Fixtures",
    # "21-22": "https://fbref.com/en/comps/9/2021-2022/schedule/2021-2022-Premier-League-Scores-and-Fixtures",
    # "22-23": "https://fbref.com/en/comps/9/2022-2023/schedule/2022-2023-Premier-League-Scores-and-Fixtures",
    "23-24": "https://fbref.com/en/comps/9/2023-2024/schedule/2023-2024-Premier-League-Scores-and-Fixtures"
}

# Folder to save HTML files
os.makedirs("raw_data", exist_ok=True)

with sync_playwright() as p:
    # Launch browser with persistent profile
    browser_context = p.chromium.launch_persistent_context(
        user_data_dir="user_data",  # <- folder where cookies/session will be stored
        headless=False
    )
    page = browser_context.new_page()

    for url in season_urls.values():
        page.goto(url)
        print(f"Opened {url}")
        input("Press Enter after solving Turnstile if required...")

        html = page.content()
        season = url.split("/")[-1].replace("/", "_")
        filename = f"raw_data/{season}.html"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"Saved {filename}")

