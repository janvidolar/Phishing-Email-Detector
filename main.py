# main.py
from analyzer import analyze_email, get_risk_level

print("=" * 50)
print("   PHISHING EMAIL RISK ANALYZER")
print("   Cybersecurity Project")
print("=" * 50)

print("\nPast the email text(multi-line, Write the END of the email):")

lines = []
while True:
    line = input()
    if line.strip().upper() == "END":
        break
    lines.append(line)

email_text = " ".join(lines)

score, found_phrases = analyze_email(email_text)
risk_level = get_risk_level(score)

print("\n" + "=" * 50)
print("RESULT")
print("=" * 50)

print("\nSuspicious patterns found:")
if found_phrases:
    for phrase, points in found_phrases:
        print(f"  - '{phrase}' (+{points} points)")
else:
    print("  None found")

print(f"\nTotal Risk Score: {score}/100")
print(f"Risk Level: {risk_level}")