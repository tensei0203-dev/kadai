import random

class Hero:
    def __init__(self, name, hp, quote, min_dmg, max_dmg):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.quote = quote
        self.min_dmg = min_dmg
        self.max_dmg = max_dmg

    def is_alive(self):
        return self.hp > 0

    # 【追加】全員共通のコマンド入力メソッド
    def decide_action(self, party, d_hp):
        print(f"\n--- {self.name}のターン (HP:{max(0, self.hp)}) ---")
        print(f"1: 攻撃する / 2: 特殊行動（回復など）")
        choice = input("行動を選択してください。> ")

        if choice == "1":
            # 攻撃処理
            print(f"「{self.quote}」")
            damage = random.randint(self.min_dmg, self.max_dmg)
            d_hp -= damage
            print(f"{self.name}の攻撃！ ドラゴンに {damage} のダメージ！")
        elif choice == "2":
            # キャラごとの特殊行動
            d_hp = self.special_move(party, d_hp)
        else:
            print(f"{self.name}は操作を誤って、動けない！")
        
        return d_hp

    # 【追加】キャラごとの個別の技
    def special_move(self, party, d_hp):
        if self.name == "僧侶":
            print(f"「{self.quote}」")
            for m in party:
                if m.is_alive():
                    heal = random.randint(10, 15)
                    m.hp = min(m.max_hp, m.hp + heal)
                    print(f"{m.name}のHPが {heal} 回復した！")
        elif self.name == "魔法使い":
            print(f"「{self.quote}」")
            damage = random.randint(30, 50) # 魔力を溜めて大ダメージ！
            d_hp -= damage
            print(f"上級魔法！ ドラゴンに {damage} の大ダメージ！！")
        elif self.name == "勇者":
            print("勇者は盾を構えた！ 防御力が上がった気がする！（演出）")
        elif self.name == "戦士":
            print("戦士は雄叫びを上げた！ ドラゴンが少し怯んだ気がする！（演出）")
        
        return d_hp

# --- 初期設定 ---
party = [
    Hero("勇者", 40, "聖なる光よ、我が剣に宿れ！", 10, 15),
    Hero("魔法使い", 25, "燃え尽きよ！", 5, 10), # 通常攻撃は弱め
    Hero("戦士", 50, "粉砕してくれる！", 12, 18),
    Hero("僧侶", 30, "聖なる祈りを…", 2, 5) # 通常攻撃は弱め
]

d_hp = 150

print("=== ドラゴン戦闘開始！ ===")

# --- ゲームループ ---
while d_hp > 0 and any(m.is_alive() for m in party):
    # 味方のターン
    for member in party:
        if member.is_alive() and d_hp > 0:
            # ここで全員に入力を求める
            d_hp = member.decide_action(party, d_hp)

    if d_hp <= 0: break

    # ドラゴンのターン
    print("\n--- ドラゴンの攻撃！ ---")
    target = random.choice([m for m in party if m.is_alive()])
    dmg = random.randint(12, 25)
    target.hp -= dmg
    print(f"ドラゴンの爪が {target.name} を襲う！ {dmg} のダメージ！")

    # 状況表示
    status = " | ".join([f"{m.name}:{max(0, m.hp)}" for m in party])
    print(f"\n【状況】{status} | ドラゴン:{max(0, d_hp)}")

if d_hp <= 0:
    print("\n【勝利】見事な連携でドラゴンを撃破した！")
else:
    print("\n【敗北】勇者一行は全滅した…")
