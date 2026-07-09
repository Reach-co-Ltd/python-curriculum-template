# curriculum_10 / テスト（pytest）

## 提出ファイル構成

```
curriculum_10/
├── target_functions.py      ← 変更不要・テスト対象の関数
├── shakyou_01/              ← 01. pytest基本
│   └── shakyou_01.py
├── shakyou_02/              ← 02. 正常系・異常系テスト
│   └── shakyou_01.py
├── shakyou_03/              ← 03. parametrize
│   └── shakyou_01.py
├── shakyou_04/              ← 04. fixture
│   └── shakyou_01.py
├── test_05/                 ← 05. 制作課題テスト
│   └── test_production.py
└── test_06/                 ← 06. 単元総合テスト（記述）
    └── test_unit.txt
```

## 実行方法
```bash
cd curriculum_10
pip install pytest
pytest shakyou_01/shakyou_01.py -v
pytest test_05/test_production.py -v
```
