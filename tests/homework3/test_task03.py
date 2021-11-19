from homework3.task03 import make_filter, sample_data


def test_return_first_entry():
    kwargs = {"name": "Bill", "type": "person"}
    assert make_filter(**kwargs).apply(sample_data) == [sample_data[0]]


def test_return_second_entry():
    kwargs = {"name": "polly", "type": "bird"}
    assert make_filter(**kwargs).apply(sample_data) == [sample_data[1]]


def test_empty_kwargs():
    assert make_filter().apply(sample_data) == sample_data


def test_non_existing_kwargs():
    assert make_filter(name="Alex").apply(sample_data) == []
