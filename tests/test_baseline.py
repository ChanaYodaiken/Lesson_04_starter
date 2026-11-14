# ("pytest.mark.req("BASELINE-04@
# @
import pytest
import baseline.tasks as tasks

@pytest.mark.req("BASELINE-04")
# def test_first_missing(required: list[str], present: list[str]):
    with pytest.raises(tasks.FirstMissingError) as e:
        tasks.first_missing(required, present)
    assert e.value.code == "FIRST_MISSING"
