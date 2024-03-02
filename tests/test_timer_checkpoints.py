import pytest  # noqa: F401
from timer_score.ts_timer import TSTimer


def test_timer_score_checkpoint():
    t = TSTimer(5)
    t.sleep(1.1)
    t.checkpoint(name="first target")
    t.sleep(5)
    t.stop()

    score, duration, _ = t.score(name="first target")
    assert duration > 1
    assert score > 0.5
    score, duration, _ = t.score()
    assert duration > 5
    assert score < 0.5


def test_timer_score_checkpoints_two_targets():
    t = TSTimer(3)
    t.checkpoint(name="first score", target=1)
    t.sleep(3)
    t.checkpoint(name="second score")
    t.sleep(2)
    t.stop()

    score, duration, target = t.score(name="first score")
    assert duration < 1
    assert score > 0.5
    assert target == 1
    score, duration, target = t.score(name="second score")
    assert duration < 4
    assert score < 0.6
    assert score > 0.4
    assert target == 3
    score, duration, target = t.score()
    assert duration > 5
    assert score < 0.2
    assert target == 3
    assert len(t.checkpoints) == 3


def test_timer_score_checkpoints_generated_name():
    t = TSTimer(3)
    t.checkpoint()
    t.stop()

    assert len(t.checkpoints) == 2
    assert len(t.checkpoints[0].name) > 0
    assert t.checkpoints[1].name == "finish"


def test_timer_score_dupplicate_name_error():
    t = TSTimer(3)
    t.checkpoint(name="name")
    t.sleep(1)
    try:
        t.checkpoint(name="name")
    except Exception as error:
        assert str(error).find("Duplicate checkpoint name") != -1
        t.stop()
    assert len(t.checkpoints) == 2
