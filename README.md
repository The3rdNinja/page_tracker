Page Tracker
page_tracker is a lightweight Python script designed to monitor social media pages and verify whether they are still active or have been blocked/suspended.

Purpose & Context
This script is a core component of a larger, automated system dedicated to combating antisemitism online. The complete tool identifies accounts posting antisemitic content, coordinates mass reporting campaigns to trigger platform moderation, and uses this script to track whether those reports successfully led to the account being blocked.

Prerequisites
Ensure you have Python 3 installed on your system.

Usage
You can run the script from your terminal by passing the target social media URL as an argument:

```bash
python3 page_tracker.py <social_media_url>
```
Example
To check the status of a specific YouTube video or channel:

```bash
python3 page_tracker.py https://youtu.be/gHzuabZUd6d
