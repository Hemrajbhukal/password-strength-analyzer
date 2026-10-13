"""Educational Password Strength Analyzer. Input is processed locally only."""
from dataclasses import dataclass, asdict
import math, re, string
from typing import List

COMMON_PASSWORDS = {"password", "password123", "123456", "123456789", "qwerty",
"qwerty123", "admin", "letmein", "welcome", "iloveyou", "abc123", "111111",
"123123", "000000"}

@dataclass
class AnalysisResult:
    score: int
    rating: str
    length: int
    checks: dict
    estimated_pool_size: int
    estimated_entropy_bits: float
    feedback: List[str]
    def to_dict(self): return asdict(self)

def estimate_character_pool(password: str) -> int:
    pool = 0
    if any(c.islower() for c in password): pool += 26
    if any(c.isupper() for c in password): pool += 26
    if any(c.isdigit() for c in password): pool += 10
    if any(not c.isalnum() and not c.isspace() for c in password): pool += len(string.punctuation)
    if any(c.isspace() for c in password): pool += 1
    return pool

def analyze_password(password: str) -> AnalysisResult:
    n = len(password)
    checks = {
        "at_least_8_characters": n >= 8, "at_least_12_characters": n >= 12,
        "lowercase": any(c.islower() for c in password),
        "uppercase": any(c.isupper() for c in password),
        "digits": any(c.isdigit() for c in password),
        "symbols": any(not c.isalnum() and not c.isspace() for c in password),
        "no_whitespace": not any(c.isspace() for c in password),
        "not_common_password": password.lower() not in COMMON_PASSWORDS,
        "not_simple_repeat": not (n >= 3 and len(set(password)) == 1),
        "not_simple_sequence": not bool(re.search(
            r"(0123|1234|2345|3456|4567|5678|6789|abcd|bcde|cdef|qwer|asdf)", password.lower()))
    }
    score = 0
    for condition, points in [
        (n >= 8,20),(n >= 12,15),(n >= 16,10),(checks["lowercase"],8),
        (checks["uppercase"],8),(checks["digits"],8),(checks["symbols"],10),
        (checks["no_whitespace"],4),(checks["not_common_password"],10),
        (checks["not_simple_repeat"],4),(checks["not_simple_sequence"],3)]:
        if condition: score += points
    score = min(score,100)
    if score < 30: rating = "Very Weak"
    elif score < 50: rating = "Weak"
    elif score < 70: rating = "Moderate"
    elif score < 85: rating = "Strong"
    else: rating = "Very Strong"
    feedback = []
    if n < 12: feedback.append("Use at least 12 characters; a longer passphrase can be easier to remember.")
    if not checks["lowercase"]: feedback.append("Add lowercase letters.")
    if not checks["uppercase"]: feedback.append("Add uppercase letters.")
    if not checks["digits"]: feedback.append("Consider adding digits.")
    if not checks["symbols"]: feedback.append("Consider adding symbols if the service permits them.")
    if not checks["not_common_password"]: feedback.append("Avoid common or widely guessed passwords.")
    if not checks["not_simple_repeat"]: feedback.append("Avoid repeating the same character many times.")
    if not checks["not_simple_sequence"]: feedback.append("Avoid predictable sequences such as 1234, abcd, or qwer.")
    if not feedback: feedback.append("Good result for this simple checker. Use a unique password and password manager.")
    pool = estimate_character_pool(password)
    entropy = round(n * math.log2(pool),2) if pool else 0.0
    return AnalysisResult(score,rating,n,checks,pool,entropy,feedback)

def print_report(result: AnalysisResult) -> None:
    print("\\n=== Password Strength Analyzer ===")
    print(f"Length: {result.length}\\nScore: {result.score}/100\\nRating: {result.rating}")
    print(f"Estimated character pool: {result.estimated_pool_size}")
    print(f"Rough entropy estimate: {result.estimated_entropy_bits} bits\\n\\nChecks:")
    for name, passed in result.checks.items():
        print(f"  [{'PASS' if passed else 'FAIL'}] {name.replace('_',' ')}")
    print("\\nSuggestions:")
    for suggestion in result.feedback: print("  - " + suggestion)
    print("\\nPrivacy note: input is processed locally and is not stored.")

def main():
    print("Password Strength Analyzer (educational)")
    print("Use a sample password, not your real account password.")
    try: password = input("Enter a sample password to analyze: ")
    except (EOFError, KeyboardInterrupt):
        print("\\nCancelled."); return
    print_report(analyze_password(password))

if __name__ == "__main__": main()
