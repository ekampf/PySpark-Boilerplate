from mock import MagicMock
from jobs.wordcount import to_pairs

def test_to_pairs():
    context = MagicMock()
    result = to_pairs(context, 'foo')
    context.inc_counter.assert_called_with('words')
    assert result[0] == 'foo'
    assert result[1] == 1
