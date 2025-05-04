# 帝愛地下人生ゲーム Ver.1.5
import random

pelica = 0
hp = 100
day = 1
target_pelica = 500000

companions = [
    {"name": "佐原", "effect": "heal", "description": "一緒にいると、たまに体力が回復する。"},
    {"name": "石田", "effect": "chinchiro_boost", "description": "チンチロ勝率が10%上がる。"},
    {"name": "大槻班長", "effect": "steal", "description": "突然現れてペリカを奪っていく。"}
]
current_companion = None

print("🎮 帝愛地下人生ゲーム：目指せ…外出券！！（50万ペリカ）")
print("スタート：所持ペリカ0 / 体力100\n")

while pelica < target_pelica and hp > 0:
    print(f"===== Day {day} =====")
    print(f"💴 ペリカ：{pelica} / 🩸 体力：{hp}")

    # 理不尽イベント
    if random.random() < 0.1:
        event = random.choice([
            "ペリカ没収（班長の気まぐれ）",
            "体力半減（謎の食中毒）",
            "強制労働（体力-20、ペリカ+0）"
        ])
        print(f"⚠️ 【理不尽イベント発生】→ {event}")
        if event == "ペリカ没収（班長の気まぐれ）":
            pelica = max(0, pelica - random.randint(3000, 10000))
        elif event == "体力半減（謎の食中毒）":
            hp = max(0, hp // 2)
        elif event == "強制労働（体力-20、ペリカ+0）":
            hp = max(0, hp - 20)

    # 仲間の効果
    if current_companion:
        if current_companion["effect"] == "heal" and random.random() < 0.3:
            hp = min(100, hp + 5)
            print(f"💖 {current_companion['name']}が励ましてくれた！体力+5")
        elif current_companion["effect"] == "steal" and random.random() < 0.1:
            loss = random.randint(1000, 5000)
            pelica = max(0, pelica - loss)
            print(f"💢 {current_companion['name']}にペリカを盗まれた！-{loss}")

    # 仲間出現イベント
    if random.random() < 0.1 and current_companion is None:
        new_friend = random.choice(companions)
        print(f"👥 地下仲間「{new_friend['name']}」が現れた！")
        print(f"📜 効果：{new_friend['description']}")
        friend_choice = input("仲間にしますか？ (y/n): ")
        if friend_choice.lower() == "y":
            current_companion = new_friend
            print(f"{new_friend['name']}が同行するようになった！")

    # 行動選択
    print("何をする？")
    print("[1] 労働（+1000ペリカ / -10体力）")
    print("[2] チンチロ（賭け：-1000ペリカ）")
    print("[3] 休憩（+10体力 / -500ペリカ）")
    print("[4] 班長に賄賂（5000ペリカ / ランダムで恩恵）")

    choice = input(">> 選択（1-4）: ")

    if choice == "1":
        pelica += 1000
        hp -= 10
        print("💪 肉体労働……ペリカを得たが、体力が削られた……")

    elif choice == "2":
        if pelica >= 1000:
            pelica -= 1000
            win_chance = 0.4
            if current_companion and current_companion["effect"] == "chinchiro_boost":
                win_chance += 0.1
            win = random.random() < win_chance
            if win:
                gain = random.randint(2000, 5000)
                pelica += gain
                print(f"🎲 チンチロ勝利ッ！ +{gain}ペリカ！！")
            else:
                print("🎲 負けた……金も時間も消えた……")
        else:
            print("💸 ペリカが足りない……賭けに出られない！")

    elif choice == "3":
        if pelica >= 500:
            pelica -= 500
            hp = min(100, hp + 10)
            print("🛌 少し休めた……回復だ……")
        else:
            print("💸 ペリカが足りない……弁当も買えない……")

    elif choice == "4":
        if pelica >= 5000:
            pelica -= 5000
            effect = random.choice(["体力回復", "ペリカ+5000", "何も起きない"])
            if effect == "体力回復":
                hp = min(100, hp + 20)
                print("👴 班長「特別にだ……休憩時間を増やしてやる」")
            elif effect == "ペリカ+5000":
                pelica += 5000
                print("👴 班長「倍返ししてやるよ……今日は運がいいな」")
            else:
                print("👴 班長「フン……騙されたな」")
        else:
            print("💸 ペリカが足りない……袖の下にも届かない……")

    else:
        print("❌ 無効な選択")

    day += 1
    print()

# ゲームエンド
if pelica >= target_pelica:
    print("🏆 外出券GETッ！！君は地上に戻ったッ！！")
    print("""
    ┌────────────────────────────┐
    │ 🎉 君はついに地上へ戻った…！              │
    │  金の光、青い空、自由な世界…           │
    │  もう班長の顔も見なくていいッ！！        │
    │  しかし——自由とは、常に孤独だ…         │
    └────────────────────────────┘
    """)
else:
    print("💀 体力が尽きた……永遠に地下だ……")

