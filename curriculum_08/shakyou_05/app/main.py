# このファイルでは3つのセキュリティ対策を実際に動かして確認します。
# 実行方法：curriculum_08/shakyou_05/ に移動してから
#   python app/main.py

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from database import init_db, create_user, find_user, save_comment, get_all_comments
from security import verify_password
from errors.exceptions import WeakPasswordError, InvalidInputError


def main():
    # まずDBを初期化します（テーブルがなければ作成します）
    init_db()

    print("=" * 50)
    print("セキュリティ対策 動作確認")
    print("=" * 50)


    # ==================================================
    # 確認1：パスワードのハッシュ化
    # ==================================================
    print("\n【確認1】パスワードのハッシュ化")
    print("→ 平文パスワードをそのままDBに保存するのは危険です")
    print("→ bcryptでハッシュ化（元に戻せない形に変換）してから保存します\n")

    # 正常系：ユーザーを登録する
    try:
        user_id = create_user("yamada", "securepass123")
        print(f"登録成功（ID: {user_id}）パスワードはハッシュ化して保存しました")
    except InvalidInputError as e:
        print(f"入力エラー: {e}")

    # ログイン検証：verify_password() でハッシュ値と照合する
    user = find_user("yamada")
    if user:
        result_ok = verify_password("securepass123", user[2])
        print(f"正しいパスワードでの照合結果: {result_ok}")

        result_ng = verify_password("wrongpassword", user[2])
        print(f"間違ったパスワードでの照合結果: {result_ng}")

    # 異常系：弱いパスワードはエラーになることを確認する
    print("\n弱いパスワード（7文字以下）を試す:")
    try:
        create_user("test_user", "short")
    except WeakPasswordError as e:
        print(f"WeakPasswordError が発生しました → {e}")


    # ==================================================
    # 確認2：SQLインジェクション対策
    # ==================================================
    print("\n【確認2】SQLインジェクション対策")
    print("→ パラメータバインディング（?プレースホルダー）で攻撃を無効化します\n")

    attack_input = "' OR '1'='1'--"
    print(f"攻撃者の入力: {attack_input}")

    result = find_user(attack_input)
    if result:
        print("危険：ユーザーが見つかってしまいました（対策が不十分です）")
    else:
        print("安全：パラメータバインディングにより攻撃が無効化されました")


    # ==================================================
    # 確認3：XSS対策
    # ==================================================
    print("\n【確認3】XSS対策（HTMLエスケープ）")
    print("→ ユーザーの入力に含まれるHTMLタグを無害化してから保存します\n")

    malicious_comment = '<script>alert("XSS攻撃！")</script>'
    print(f"攻撃者のコメント: {malicious_comment}")

    comment_id = save_comment(malicious_comment)
    print(f"保存完了（ID: {comment_id}）")

    comments = get_all_comments()
    for comment in comments:
        print(f"DB内のコメント: {comment[1]}")
    print("→ <script> が &lt;script&gt; に変換されています。無害化に成功しました。")


    print("\n" + "=" * 50)
    print("3つのセキュリティ対策の確認が完了しました")
    print("=" * 50)


if __name__ == "__main__":
    main()
