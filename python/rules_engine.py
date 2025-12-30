def evaluate_rules(data, rules):
    violations = []
    for rule in rules:
        try:
            if eval(rule["condition"], {}, data):
                violations.append(rule)
        except Exception as e:
            violations.append({
                "id": rule["id"],
                "severity": "error",
                "message": f"Rule failed: {str(e)}"
            })
    return violations
