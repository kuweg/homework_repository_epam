from homework4.task_3_get_print_output import my_precious_logger


def test_read_stderr(capsys):
    my_precious_logger('error : alert')
    captured_output = capsys.readouterr()
    assert captured_output.err == 'error : alert'


def test_read_stdout(capsys):
    my_precious_logger('Three tuples')
    captured_output = capsys.readouterr()
    assert captured_output.out == 'Three tuples'
