from hypothesis import given
from hypothesis import strategies as st

def propose_optimizations(issues):

    optimizations = []

    for location, count in issues.items():

        if count > 5:
            optimizations.append(
                f"Aumentar frecuencia de buses en {location}"
            )

    return optimizations

@given(st.dictionaries(
    st.text(),
    st.integers()
))
def test_propose_optimizations(issues):

    result = propose_optimizations(
        issues
    )

    assert isinstance(
        result,
        list
    )