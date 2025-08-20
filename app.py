from flask import Flask, render_template, request, url_for

app = Flask(__name__)

# ←ここを書き換えるだけで問題を差し替えできます
QUIZ = {
    "q": "便潜血検査を1000人が受けると、だいたい何人が陽性になる？？",
    "choices": ["10人", "100人", "500人"],
    "answer": 1,
    "explain": "便潜血検査では1000人中およそ100人が陽性となります。ただし陽性＝大腸がんではなく、その中から精密検査を行い、実際に大腸がんと診断されるのは 2〜3人程度です。"
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
