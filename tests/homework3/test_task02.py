from datetime import datetime

from homework3.task02 import slow_calculate, sum_parallel_slow_calculation


def test_time_wth_50_workers():
    start = datetime.now()
    sum_parallel_slow_calculation(slow_calculate, range(500), 50)
    end = datetime.now() - start
    assert end.total_seconds() < 60
