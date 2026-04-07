def guardrails_check(user_input: str):
    banned_words = ["hack", "exploit", "steal"]
    warning_words = ["bypass", "crack", "leak"]

    risk_score = 0
    triggered = []

    text = user_input.lower()

    # Hard block
    for word in banned_words:
        if word in text:
            risk_score += 2
            triggered.append(word)

    # Soft warning
    for word in warning_words:
        if word in text:
            risk_score += 1
            triggered.append(word)

    # Decision logic
    if risk_score >= 2:
        return {
            "status": "blocked",
            "risk_score": risk_score,
            "reason": triggered
        }

    elif risk_score == 1:
        return {
            "status": "warning",
            "risk_score": risk_score,
            "reason": triggered
        }

    return {
        "status": "safe",
        "risk_score": 0,
        "reason": []
    }