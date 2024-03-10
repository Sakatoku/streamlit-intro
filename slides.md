# Streamlitの紹介

---

## Streamlitとは

Pythonオンリーで簡単にWebアプリを構築できるPython Web UIフレームワーク

---

## Streamlitの特徴

- ユーザ入力を取得する
- グラフを描画する

などを非常に短いコードで実現できる

---

## Streamlitのコード

```
import streamlit as st
import pandas as pd
import numpy as np

level = st.slider('Set level', 0, 50, 1)
chart_data = pd.DataFrame(np.random.randn(10, 3) + level, columns=["a", "b", "c"])

st.line_chart(chart_data)
```

---

## Streamlitの使いどころ

データ加工や機械学習の分野で特に使いやすい。  
例えば機械学習するとき、可視化する部分を省力化できる！

---

## Streamlitの最近の新機能

- st.popover
  - ポップアップダイアログで入力させる
  - 1.32.0で実装

---

## Streamlitの最近の新機能

- st.page_link
  - MPA対応の強化。他のページに遷移するリンクテキスト
  - 1.31.0で実装

---

## Streamlitの最近の新機能

- st.write_stream
  - タイプライター風の出力エフェクト
  - 1.31.0で実装

---

## Streamlitの最近の新機能

- st.switch_page
  - MPA対応の強化。サイドバーを使わなくても他のページに遷移できるようになった
  - 1.30.0で実装

---

## Streamlitの最近の新機能

- st.query_params
  - URLパラメータをアプリで取得できるようになった
  - 1.30.0で実装

---

## Streamlitの今後

[Streamlit roadmap](https://roadmap.streamlit.app/)

- 動画プレイヤーの機能強化
- partial reruns
  - 今は入力が変わるたびに画面全体が更新されているが、一部のグラフだけを更新する、ということができるようになる
- st.dialog：モーダルダイアログの実装
- MPA対応のさらなる強化
  - 今は他のページへの遷移に色々と制限がある。徐々に改善する見込み
