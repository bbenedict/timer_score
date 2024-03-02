import pytest  # noqa: F401
from timer_score.ts_timer import TSTimer


def test_timer_score_start():
    t = TSTimer(3)
    assert t.start is not None
    t.stop()


def test_timer_score_stop():
    t = TSTimer(3)
    t.stop()
    t.checkpoint()
    assert len(t.checkpoints) == 1


def test_timer_score_reset():
    t = TSTimer(3)
    t.stop()
    t.reset()
    assert len(t.checkpoints) == 0
    t.checkpoint()
    assert len(t.checkpoints) == 1
    t.stop()


def test_timer_score_finish():
    t = TSTimer(3)
    t.sleep(1)
    t.stop()
    assert t.finish is not None
    assert t.finish > 1


def test_timer_score_finish_not_finished():
    t = TSTimer(3)
    t.sleep(1)
    assert t.finish is None
    t.stop()
    assert t.finish > 1


def test_timer_score_sleep():
    t = TSTimer(3)
    t.sleep(3.1)
    t.stop()
    score, duration, target = t.score()
    assert score < 0.5
    assert duration > 3
    assert duration < 3.5
    assert target == 3


def test_timer_score_duration():
    t = TSTimer(3)
    t.sleep(3.1)
    t.stop()
    duration = t.duration()
    assert duration > 3
    assert duration < 3.5


def test_timer_score_duration_with_name():
    t = TSTimer(3)
    t.sleep(3.1)
    t.checkpoint(name="checkpoint")
    t.sleep(3.1)
    t.stop()
    duration = t.duration(name="checkpoint")
    assert duration > 3
    assert duration < 3.5


def test_timer_score_duration_invalid_name_error():
    t = TSTimer(1)
    t.sleep(1)
    t.checkpoint()
    try:
        t.duration(name="bogus")
    except Exception as error:
        assert str(error).find("Invalid checkpoint name") != -1
        t.stop()
    assert len(t.checkpoints) == 2


def test_timer_score_duration_timer_not_stopped():
    t = TSTimer(1)
    t.sleep(1)
    duration = t.duration()
    assert duration < 1.5
    t.stop()
    assert duration < t.duration()


def test_timer_score_no_target():
    t = TSTimer()
    t.sleep(1)
    t.stop()
    try:
        t.score()
    except Exception as error:
        assert str(error).find("No target provided") != -1
    assert len(t.checkpoints) == 1


def test_timer_score_invalid_name_error():
    t = TSTimer()
    t.sleep(1)
    t.checkpoint()
    t.stop()
    try:
        t.score(name="bogus")
    except Exception as error:
        assert str(error).find("Invalid checkpoint name") != -1
    assert len(t.checkpoints) == 2


def test_timer_score_name_no_checkpoint():
    t = TSTimer()
    t.sleep(1)
    t.stop()
    try:
        t.score(name="bogus")
    except Exception as error:
        assert str(error).find("Invalid checkpoint name") != -1
    assert len(t.checkpoints) == 1


def test_timer_score_func():
    def double_it(y):
        return 2*y
    t = TSTimer(1)
    score, duration, target = t.execute(double_it, 2)

    assert score > 0.5
    assert duration < 1
    assert target == 1
