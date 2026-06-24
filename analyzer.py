from keywords import SUSPICIOUS_PHRASES

def analyze_email(email_text):
    email_text = email_text.lower()
    
    total_score = 0
    found_phrases = []
    
    for phrase, points in SUSPICIOUS_PHRASES.items():
        if phrase in email_text:
            total_score += points
            found_phrases.append((phrase, points))
    
    return total_score, found_phrases


def get_risk_level(score):
    if score >= 60:
        return "🔴 HIGH RISK — This is likely a Phishing Email!"
    elif score >= 30:
        return "🟡 MEDIUM RISK — Be careful with this Email!"
    else:
        return "🟢 LOW RISK — This Email looks Safe!"