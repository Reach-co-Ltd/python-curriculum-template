# このファイルでは、このアプリ専用のエラーを定義します。
# Pythonには最初からValueErrorやTypeErrorなどのエラーが用意されていますが、
# 「パスワードが弱すぎる」「入力値がおかしい」といった
# アプリ固有のエラーは自分で作る必要があります。

# Exceptionを継承することで、Pythonのエラーとして扱えるようになります。
class WeakPasswordError(Exception):
    pass

class InvalidInputError(Exception):
    pass
