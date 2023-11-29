from flask import render_template, request
from app import app


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/recommend', methods=['POST'])
def recommend():
    # Get user input from the quiz
    q1 = request.form.get('q1', '')
    q2 = request.form.get('q2', '')
    q3 = request.form.get('q3', '')
    q4 = request.form.get('q4', '')
    q5 = request.form.get('q5', '')

    # Determine personality based on quiz
    # personality = determine_personality(q1, q2, q3, q4, q5)
    # Simple logic to determine personality based on quiz answers
    score = 0
    question = [q1, q2, q3, q4, q5]
    for x in question:
        qx = x
        if qx == 'Tea':
            score += 1
        elif qx == 'Coffee':
            score += 2
        elif qx == 'Wine':
            score += 3
        elif qx == 'Whiskey':
            score += 4
        elif qx == 'Beer':
            score += 5
    # Categorize personality based on total score
    p = ""
    if score <= 8:
        p = 'The Contemplative Thinker'
    elif score <= 12:
        p = 'The Energetic Go-Getter'
    elif score <= 16:
        p = 'The Sophisticated Connoisseur'
    elif score <= 20:
        p = 'The Mysterious Maverick'
    else:
        p = 'The Easygoing Socialite'

    b = recommend_beverage(p)

    return render_template('index.html', personality1=p, beverage1=b)


def recommend_beverage(personality):
    # Logic to determine the beverage based on personality
    if 'Contemplative' in personality:
        return 'Tea'
    elif 'Energetic' in personality:
        return 'Coffee'
    elif 'Sophisticated' in personality:
        return 'Wine'
    elif 'Mysterious' in personality:
        return 'Whiskey'
    elif 'Easygoing' in personality:
        return 'Beer'
    else:
        return 'Unknown'

