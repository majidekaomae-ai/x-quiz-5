from flask import Flask, render_template, request, url_for

app = Flask(__name__)

# ←ここを書き換えるだけで問題を差し替えできます
QUIZ = {
    "q": "ウイルス予防で正しいのはどれ？",
    "choices": ["抗生物質", "ワクチン", "鎮痛剤"],
    "answer": 1,
    "explain": "予防はワクチン。治療は抗ウイルス薬が選ばれます。"
}

@app.route("/", methods=["GET", "POST"])
def index():
    selected = request.form.get("a")
    answered = selected is not None
    is_correct = None
    if answered:
        try:
            is_correct = (int(selected) == QUIZ["answer"])
        except ValueError:
            answered = False  # 想定外入力は未回答扱い

    # Twitterカード用：絶対URLで画像パスを作る
    absolute_url = request.url_root.rstrip("/")
    card_image_url = absolute_url + url_for("static", filename="card.jpg")

    return render_template(
        "index.html",
        quiz=QUIZ,
        answered=answered,
        selected=int(selected) if answered else None,
        is_correct=is_correct,
        card_image_url=card_image_url,
        page_url=absolute_url
    )

if __name__ == "__main__":
    app.run(debug=True)
