import os
import sys
import instaloader
from instaloader import Instaloader

def banner():
    print("""
\033[32m██\033[0m╗ \033[32m██████\033[0m╗      \033[32m██████\033[0m╗ \033[32m███████\033[0m╗\033[32m██\033[0m╗\033[32m███\033[0m╗   \033[32m██\033[0m╗\033[32m████████\033[0m╗
\033[32m██\033[0m║\033[32m██\033[0m╔════╝     \033[32m██\033[0m╔═══\033[32m██\033[0m╗\033[32m██\033[0m╔════╝\033[32m██\033[0m║\033[32m████\033[0m╗  \033[32m██\033[0m║╚══\033[32m██\033[0m╔══╝
\033[32m██\033[0m║\033[32m██\033[0m║  \033[32m███\033[0m╗    \033[32m██\033[0m║   \033[32m██\033[0m║\033[32m███████\033[0m╗\033[32m██\033[0m║\033[32m██\033[0m╔\033[32m██\033[0m╗ \033[32m██\033[0m║   \033[32m██\033[0m║
\033[32m██\033[0m║\033[32m██\033[0m║   \033[32m██\033[0m║    \033[32m██\033[0m║   \033[32m██\033[0m║╚════\033[32m██\033[0m║\033[32m██\033[0m║\033[32m██\033[0m║╚\033[32m██\033[0m╗\033[32m██\033[0m║   \033[32m██\033[0m║
\033[32m██\033[0m║╚\033[32m██████\033[0m╔╝    ╚\033[32m██████\033[0m╔╝\033[32m███████\033[0m║\033[32m██\033[0m║\033[32m██\033[0m║ ╚\033[32m████\033[0m║   \033[32m██\033[0m║
\033[0m╚═╝ ╚═════╝      ╚═════╝ ╚══════╝╚═╝╚═╝  ╚═══╝   ╚═╝\033[0m\033[41mV2\033[0m
\033[41mCoded By Achik | www.termuxcommands.com\033[0m

""")

def profile_information(username):
    try:
        print("\033[33mProfile Informations...\033[0m\n")
        x = Instaloader()
        f = instaloader.Profile.from_username(x.context, username)

        print("\033[32mUsername\033[0m :", f.username)
        print("\033[32mID\033[0m :", f.userid)
        print("\033[32mFull Name\033[0m :", f.full_name)
        print("\033[32mBiography\033[0m :", f.biography)
        print("\033[32mBusiness Category Name\033[0m :", f.business_category_name)
        print("\033[32mExternal URL\033[0m :", f.external_url)
        print("\033[32mFollowed By Viewer\033[0m :", f.followed_by_viewer)
        print("\033[32mFollowees\033[0m :", f.followees)
        print("\033[32mFollowers\033[0m :", f.followers)
        print("\033[32mFollows Viewer\033[0m :", f.follows_viewer)
        print("\033[32mBlocked By Viewer\033[0m :", f.blocked_by_viewer)
        print("\033[32mHas Blocked Viewer\033[0m :", f.has_blocked_viewer)
        print("\033[32mHas Highlight Reels\033[0m :", f.has_highlight_reels)
        print("\033[32mHas Public Story\033[0m :", f.has_public_story)
        print("\033[32mHas Requested Viewer\033[0m :", f.has_requested_viewer)
        print("\033[32mRequested By Viewer\033[0m :", f.requested_by_viewer)
        print("\033[32mHas Viewable Story\033[0m :", f.has_viewable_story)
        print("\033[32mIGTV\033[0m :", f.igtvcount)
        print("\033[32mIs Business Account\033[0m :", f.is_business_account)
        print("\033[32mIs Private\033[0m :", f.is_private)
        print("\033[32mIs Verified\033[0m :", f.is_verified)
        print("\033[32mMedia Count\033[0m :", f.mediacount)
        print("\033[32mProfile Picture URL\033[0m :", f.profile_pic_url)

    except KeyboardInterrupt:
        print("\033[33mI understand!")
    except EOFError:
        print("\033[33mWhy?")

def fetch_post_info(username):
    print("\n\033[33mPost Informations...\033[0m\n")
    L = instaloader.Instaloader()

    try:
        profile = instaloader.Profile.from_username(L.context, username)
        posts = profile.get_posts()

        post_info = []

        for i, post in enumerate(posts, start=1):
            caption = post.caption
            if caption is None:
                caption = "No caption provided"
            post_date = post.date.strftime("%Y-%m-%d")
            post_time = post.date.strftime("%I:%M %p")  # Fetch post time in 12-hour format
            post_info.append((f"\033[41mPOST {i}\033[0m", post_date, post_time, caption, post.url))

        return post_info

    except instaloader.exceptions.ProfileNotExistsException:
        print("Profile does not exist.")
        return []

    except Exception as e:
        print("An error occurred:", e)
        return []

def download_posts(username, download_path):
    print("\n\033[33mDownloading all posts...\033[0m\n")
    os.chdir('/sdcard')
    L = instaloader.Instaloader()
    try:
        profile = instaloader.Profile.from_username(L.context, username)
        posts = profile.get_posts()
        for i, post in enumerate(posts, start=1):
            L.download_post(post, target=download_path)
            print(f"\033[41mPOST {i}\033[0m downloaded successfully.")
    except instaloader.exceptions.ProfileNotExistsException:
        print("Profile does not exist.")
    except Exception as e:
        print("An error occurred:", e)

def open_help():
    os.system("termux-open-url https://termuxcommands.com")

def print_post_info(post_info):
    if post_info:
        for info in post_info:
            post_heading = f"{info[0]}"
            post_date = f"Posted Date: {info[1]}"
            post_time = f"Posted Time: {info[2]}"
            post_caption = f"Caption: {info[3]}"
            post_url = f"Post URL: \033[32m{info[4]}\033[0m"
            print(f"{post_heading:<15s}\033[41m \033[0m")
            print(f"{post_date:<15s}")
            print(f"{post_time:<15s}")
            print(f"{post_caption:<15s}")
            print(f"{post_url:<15s}")
            print("-" * 50)  # Separator line
            print()  # Add a space between post infos
    else:
        print("No post URLs fetched.")

def options_menu(username):
    print("\033[36mEnter Instagram username: \033[0m \033[37m{}\033[0m \n".format(username))
    print("\033[1;34mOptions:\033[0m")
    print("\033[1;33m[1]\033[0m \033[1;32mProfile Information\033[0m")
    print("\033[1;33m[2]\033[0m \033[1;32mPost Information\033[0m")
    print("\033[1;33m[3]\033[0m \033[1;32mDownload all posts\033[0m")
    print("\033[1;33m[4]\033[0m \033[1;32mChange Username\033[0m")
    print("\033[1;33m[5]\033[0m \033[1;32mGet Help\033[0m")
    print("\033[1;33m[6]\033[0m \033[1;32mExit\033[0m")
    choice = input("\n\033[36mEnter your choice: \033[0m")

    if choice == "1":
        os.system('cls' if os.name == 'nt' else 'clear')  # Clean the screen
        banner()
        profile_information(username)
        input("\n\033[36mPress Enter to go back to the menu...\033[0m")
        os.system('cls' if os.name == 'nt' else 'clear')  # Clean the screen
        banner()
        options_menu(username)
    elif choice == "2":
        os.system('cls' if os.name == 'nt' else 'clear')  # Clean the screen
        banner()
        post_info = fetch_post_info(username)
        print_post_info(post_info)
        input("\n\033[36mPress Enter to go back to the menu...\033[0m")
        os.system('cls' if os.name == 'nt' else 'clear')  # Clean the screen
        banner()
        options_menu(username)
    elif choice == "3":
        os.system('cls' if os.name == 'nt' else 'clear')  # Clean the screen
        banner()
        download_path = "IG OSINT"
        download_posts(username, download_path)
        input("\n\033[36mPress Enter to go back to the menu...\033[0m")
        os.system('cls' if os.name == 'nt' else 'clear')  # Clean the screen
        banner()
        options_menu(username)
    elif choice == "4":
        os.system('cls' if os.name == 'nt' else 'clear')  # Clean the screen
        banner()
        username = input("\n\033[36mEnter new Instagram username: \033[0m")
        input("\n\033[36mUsername changed successfully. Press Enter to go back to the menu...\033[0m")
        os.system('cls' if os.name == 'nt' else 'clear')  # Clean the screen
        banner()
        options_menu(username)
    elif choice == "5":
        os.system('cls' if os.name == 'nt' else 'clear')  # Clean the screen
        banner()
        open_help()
        input("\n\033[36mPress Enter to go back to the menu...\033[0m")
        os.system('cls' if os.name == 'nt' else 'clear')  # Clean the screen
        banner()
        options_menu(username)
    elif choice == "6":
        print("\033[1;31mExiting...\033[0m")
        sys.exit()
    else:
        print("Invalid choice.")

def main():
    os.system('cls' if os.name == 'nt' else 'clear')  # Clean the screen
    banner()
    username = input("\n\033[36mEnter Instagram username: \033[0m")
    os.system('cls' if os.name == 'nt' else 'clear')  # Clean the screen
    banner()
    options_menu(username)

if __name__ == "__main__":
    main()
