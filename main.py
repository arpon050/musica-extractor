import yt_dlp
import os

def download_music():
    link_file = ''
    
    # Check if links.txt exists
    if not os.path.exists(link_file):
        print(f"❌ File '{link_file}' not found. Please create it and add links.")
        return

    # Modern yt-dlp options for high-quality MP3
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        # This saves files in a 'downloads' folder inside your current directory
        'outtmpl': './downloads/%(title)s.%(ext)s', 
    }

    with open(link_file, 'r') as f:
        links = [line.strip() for line in f if line.strip()]

    if not links:
        print("📭 The links.txt file is empty.")
        return

    print(f"🎵 Found {len(links)} links. Starting download...\n")

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        for index, link in enumerate(links, 1):
            try:
                print(f"[{index}/{len(links)}] Downloading: {link}")
                ydl.download([link])
            except Exception as e:
                print(f"⚠️ Error with {link}: {e}")

    print("\n✅ All done! Check the 'downloads' folder.")

if __name__ == "__main__":
    download_music()
