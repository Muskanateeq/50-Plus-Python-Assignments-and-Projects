import requests
from bs4 import BeautifulSoup

def get_profile_image_link(github_url):
    headers = {"User-Agent": "Mozilla/5.0"}  # to mimic a browser request
    response = requests.get(github_url, headers=headers)
    
    if response.status_code != 200:
        print("Failed to retrieve the webpage. Status code:", response.status_code)
        return None

    soup = BeautifulSoup(response.text, "html.parser")
    
    # Look for an <img> tag with class that contains 'avatar-user'
    img_tag = soup.find("img", class_="avatar avatar-user width-full border color-bg-default")
    
    # If not found, try a more general search for class 'avatar-user'
    if not img_tag:
        img_tag = soup.find("img", class_="avatar-user")
    
    if img_tag and "src" in img_tag.attrs:
        return img_tag["src"]
    else:
        return None

def main():
    # Ask user for a GitHub profile URL
    github_url = input("Enter a GitHub profile URL (e.g., https://github.com/username): ").strip()
    
    # Get the profile image link through web scraping
    profile_img_link = get_profile_image_link(github_url)
    
    if profile_img_link:
        print("\nThe profile image link is:")
        print(profile_img_link)
    else:
        print("Could not find the profile image on this page.")

if __name__ == "__main__":
    main()
