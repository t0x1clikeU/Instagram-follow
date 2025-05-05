from instagrapi import Client
import time
import os
from datetime import datetime


def log(msg):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_line = f"{now} | {msg}"
    print(log_line)
    with open("follow_log.log", "a", encoding="utf-8") as log_file:
        log_file.write(log_line + "\n")

print("Instagram Auto Follows Tools \n\nDev: t0x1c")

target_username = input("Target ID:").strip()
print("\n")

if not os.path.exists("acc.txt"):
    with open("acc.txt", "w") as f:
        f.write("# ID:PASS を記入してください ※改行で複数アカウント記入可能\n")
    log("acc.txt が存在しないため、新しく作成しました。")
    log("記入後に再実行してください...")
    input("続行するには何かキーを押してください...")
    exit()

if not os.path.exists("Session"):
    os.makedirs("Session")
    log("Session フォルダを作成しました。")

with open("acc.txt", "r", encoding="utf-8") as f:
    accounts = [line.strip().split(":") for line in f if ":" in line]

def is_account_banned(client, username):
    try:
        client.user_info_by_username(username)
        return False
    except Exception as e:
        return True


for username, password in accounts:
    session_path = f"Session/{username}.session"
    cl = Client()

    try:
        if os.path.exists(session_path):
            cl.load_settings(session_path)
            cl.login(username, password)
            log(f"{username} → セッションからログイン成功")
        else:
            cl.login(username, password)
            cl.dump_settings(session_path)
            log(f"{username} → 新規ログイン成功（セッション保存）")
    except Exception as e:
        log(f"{username} → ログイン失敗: {str(e)}")
        continue

    if is_account_banned(cl, username):
        log(f"{username} → ロックされている可能性があります")
        continue

    try:
        
        user_id = cl.user_id_from_username(target_username)

        try:
            following_ids = cl.user_following(cl.user_id)
            if user_id in following_ids:
                log(f"{username} → @{target_username} フォロー済み")
                continue
        except Exception as e:
            log(f"{username} → フォロー済みチェック失敗: {str(e)}")
            continue

        cl.user_follow(user_id)
        log(f"{username} → @{target_username} フォロー")

    except Exception as e:
        log(f"{username} → フォロー失敗: {str(e)}")

    time.sleep(5)


print("\n")
log("すべてのアカウントで処理が完了しました。")
input("続行するには何かのキーを押してください...")
