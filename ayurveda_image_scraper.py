import os
from icrawler.builtin import GoogleImageCrawler

traits = {
    "tongue": ["normal", "pale", "coated", "red"],
    "lips": ["normal", "cracked_dry", "reddish"],
    "nails": ["normal", "bluish", "reddish", "pale"],
    "face": ["normal", "vata", "pitta", "kapha"]
}

base_dir = "data"

# Make directories
def create_folders():
    for trait, classes in traits.items():
        for cls in classes:
            folder = os.path.join(base_dir, trait, cls)
            os.makedirs(folder, exist_ok=True)

# Download images only
def download_images():
    for trait, classes in traits.items():
        for cls in classes:
            folder = os.path.join(base_dir, trait, cls)
            print(f"\n▶ Downloading for: {trait} - {cls}")
            keywords = [
                f"close up {cls.replace('_', ' ')} {trait} ayurveda",
                f"{cls.replace('_', ' ')} {trait} ayurvedic diagnosis",
                f"{cls.replace('_', ' ')} {trait} medical photo",
                f"{cls.replace('_', ' ')} {trait} macro photo",
                f"{cls.replace('_', ' ')} {trait} clinical image"
            ]
            for keyword in keywords:
                print(f"  → Searching: {keyword}")
                crawler = GoogleImageCrawler(storage={'root_dir': folder})
                crawler.crawl(keyword=keyword, max_num=30)

# Main
if __name__ == "__main__":
    create_folders()
    download_images()
