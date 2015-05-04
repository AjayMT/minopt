
from pyvows import Vows, expect
from minopt import minopt


@Vows.batch
class Minopt(Vows.Context):
    def topic(self):
        return minopt(['--baz', 'hello', '--foo', 'bar', '-baz',
                       '--riff=wobble', '--hey', '-ho', 'world'],
                      {'string': ['a', 'hey', 'w'],
                       'boolean': ['baz', 'h', 'o', 'q']})

    def should_parse_long_arguments(self, topic):
        expect(topic['foo']).to_equal('bar')
        expect(topic['riff']).to_equal('wobble')

    def should_parse_short_arguments(self, topic):
        expected = (True, True)
        expect((topic['b'], topic['z'])).to_equal(expected)

    def should_parse_booleans(self, topic):
        expect(topic['baz']).to_be_true()
        expect(topic['h']).to_be_true()
        expect(topic['o']).to_be_true()

    def should_parse_strings(self, topic):
        expect(topic['a']).to_be_empty()
        expect(topic['hey']).to_be_empty()

    def should_parse_unnamed_args(self, topic):
        expect(topic['_']).to_equal(['hello', 'world'])

    def should_set_all_args(self, topic):
        expected = ('', False)
        expect((topic['w'], topic['q'])).to_equal(expected)
