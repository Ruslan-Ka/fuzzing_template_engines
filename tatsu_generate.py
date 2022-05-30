import io
import tatsu
from tatsurd import TatSuRDG


class ExampleRandomDerivation:

    def __init__(self, grammar_name, max_length_regex, max_counter, recursion_limit, override_placeholders):
        self.max_length_regex = max_length_regex
        self.max_counter = max_counter
        self.recursion_limit = recursion_limit
        path_to_grammar = grammar_name
        with io.open(path_to_grammar, 'r', encoding="utf-8") as file:
            grammar = file.read()
        self.parser = tatsu.compile(grammar)
        self.rg = TatSuRDG(self.parser, max_length_regex=self.max_length_regex, max_counter=self.max_counter,
                           recursion_limit=self.recursion_limit, override_placeholders=override_placeholders)

    def derive(self, rule_name, stack):
        return self.rg.random_derivation(rule_name, stack)


def generate_template(grammar, max_length_regex, max_counter, recursion_limit):
    ex = ExampleRandomDerivation(grammar, max_length_regex, max_counter, recursion_limit, {})
    ex.rg.init_rules()
    stack = []
    result = ex.derive("start", stack)
    return result, stack
