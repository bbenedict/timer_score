import pytest  # noqa: F401
from timer_score.ts_timer import TSTimer


def test_timer_score():
    t = TSTimer(3)
    t.sleep(2)
    t.stop()

    score, duration, target = t.score()
    assert duration < 3
    assert score > 0.5
    assert target == 3
    assert len(t.checkpoints) == 1


def test_timer_score_low_target():
    t = TSTimer(1)
    t.checkpoint(name="good score")
    t.sleep(1.5)
    t.checkpoint(name="average score")
    t.sleep(1.5)
    t.stop()

    score, duration, target = t.score(name="good score")
    assert duration < 1
    assert score > 0.6
    assert target == 1
    score, duration, target = t.score(name="average score")
    assert duration < 2
    assert score < 0.6
    assert score > 0.2
    assert target == 1
    score, duration, target = t.score()
    assert duration > 3
    assert score < 0.2
    assert target == 1
    assert len(t.checkpoints) == 3


def test_timer_score_high_target():
    t = TSTimer(6)
    t.checkpoint(name="good score")
    t.sleep(6)
    t.checkpoint(name="average score")
    t.sleep(6)
    t.stop()

    score, duration, target = t.score(name="good score")
    assert duration < 1
    assert score > 0.6
    assert target == 6
    score, duration, target = t.score(name="average score")
    assert duration < 7
    assert score < 0.6
    assert score > 0.2
    assert target == 6
    score, duration, target = t.score()
    assert duration > 12
    assert score < 0.2
    assert target == 6
    assert len(t.checkpoints) == 3
