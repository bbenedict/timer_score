import pytest  # noqa: F401
import time
from timer_score.ts_timer import TSTimer


def test_timer_score_perf():
    start = time.time()
    t = TSTimer(3)
    t.stop()
    finish = time.time()
    assert finish - start < 0.01


def test_timer_score_perf_score():
    start = time.time()
    t = TSTimer(3)
    t.stop()
    _, _, _ = t.score()
    finish = time.time()
    assert finish - start < 0.01


def test_timer_score_perf_checkpoints():
    start = time.time()
    t = TSTimer(3)
    t.checkpoint("one")
    t.checkpoint("two")
    t.stop()
    finish = time.time()
    assert finish - start < 0.01


def test_timer_score_perf_full():
    start = time.time()
    t = TSTimer(3)
    t.checkpoint("one")
    t.sleep(2)
    t.checkpoint("two")
    t.sleep(2)
    t.stop()
    _, _, _ = t.score("one")
    _, _, _ = t.score("two")
    _, _, _ = t.score()
    finish = time.time()
    assert finish - start - 4 < 0.01  # remove sleeps for 4 total seconds
