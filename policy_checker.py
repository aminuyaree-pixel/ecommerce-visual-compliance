
POLICY_RULES = {
    "Unsupported medical claim": [
        "cures diabetes",
        "cures cancer",
        "guaranteed weight loss",
        "treats all diseases"
    ],
    "Misleading guarantee": [
        "100% guaranteed results",
        "works for everyone",
        "risk-free guaranteed"
    ],
    "Potentially misleading superlative": [
        "best product in the world",
        "number one in the world"
    ]
}


def check_product_description(description):

    findings = []

    text = description.lower()

    for category, phrases in POLICY_RULES.items():

        for phrase in phrases:

            if phrase in text:
                findings.append({
                    "category": category,
                    "matched_phrase": phrase,
                    "recommendation": (
                        "Review this claim and provide "
                        "appropriate supporting evidence."
                    )
                })

    return {
        "risk_level": (
            "REVIEW REQUIRED" if findings else "NO MATCH FOUND"
        ),
        "findings": findings
    }
