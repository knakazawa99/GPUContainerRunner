from gpu_container_runner.lib.completer import Completer


def test_complete():
    completer = Completer(['test', 'continuous'])
    words = completer.complete('te', 0)
    assert words == 'test'


def test_complete_index_error():
    completer = Completer(['test', 'continuous'])
    words = completer.complete('te', 1)
    if words is None:
        assert True
    else:
        assert False
