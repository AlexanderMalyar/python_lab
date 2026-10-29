def audit_journal(full_name: str) ->str:
    parts = full_name.strip().split()
    name = parts[0].capitalize()
    fam = parts[1][0].upper()
    otec = parts[2][0].upper() if len(parts) > 2 else ""
    if otec:
        return f"{name} {fam}.{otec}."
    else:
        return f"{name} {fam}."

user = input("введите фио:  ")
print(audit_journal(user))
