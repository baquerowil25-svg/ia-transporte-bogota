def propose_optimizations(issues):

    optimizations = []

    for location, count in issues.items():

        if count > 1:

            optimizations.append(
                f"Aumentar frecuencia de buses en {location}"
            )

    return optimizations

if __name__ == "__main__":

    issues = {
        "Suba": 7,
        "Kennedy": 3,
        "Usme": 1
    }

    print(
        propose_optimizations(
            issues
        )
    )