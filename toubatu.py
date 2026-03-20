import random

# --- 関数の定義 ---

# プレイヤーの行動（攻撃か回復）を決める関数
def player_turn(player_hp, dragon_hp):
    print("\n--- 勇者のターン ---")
    print("1: 攻撃 / 2: 回復")
    choice = input("行動を選んでください（1 or 2）: ")

    if choice == "1":
        # 攻撃：5〜10のダメージ
        damage = random.randint(5, 10)
        dragon_hp -= damage
        print(f"勇者の攻撃！ドラゴンに {damage} のダメージを与えた！")
    elif choice == "2":
        # 回復：HPを5回復
        player_hp += 5
        print(f"勇者は呪文を唱えた！HPが 5 回復した！")
    else:
        print("勇者は逃げれなかった！（1か2以外を入力したため）")
    
    return player_hp, dragon_hp

# ドラゴンの行動を処理する関数
def dragon_turn(player_hp):
    print("\n--- ドラゴンのターン ---")
    damage = random.randint(4, 12)
    player_hp -= damage
    print(f"ドラゴンの攻撃！勇者は {damage} のダメージを受けた！")
    return player_hp

# --- メイン処理 ---

# 初期設定
p_hp = 30  # 勇者のHP
d_hp = 30  # ドラゴンのHP

print("ドラゴンが現れた！")

# 繰り返し処理（どちらかのHPが0より大きい間、戦い続ける）
while p_hp > 0 and d_hp > 0:
    # 勇者のターン
    p_hp, d_hp = player_turn(p_hp, d_hp)
    
    # 勇者の攻撃でドラゴンが倒れたかチェック
    if d_hp <= 0:
        break

    # ドラゴンのターン
    p_hp = dragon_turn(p_hp)

    # 現在のHPを表示
    print(f"【現在の状態】勇者HP: {max(0, p_hp)} / ドラゴンHP: {max(0, d_hp)}")

# 勝敗の判定
print("\n====================")
if d_hp <= 0:
    print("ドラゴンを倒した！世界に平和が訪れた！")
else:
    print("勇者は倒れた…")
print("====================")
