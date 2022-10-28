import pytest
import sys
from clingo_output_support import *

class TestOutputParser:
    def setup_class(self):    
        with open("clingo-output-sat.txt") as f:
            raw = f.read()
            answers_list = parse_input(raw)
            self.sat_answers = []
            for a in answers_list:
                sched = make_sched(a)
                head,body = make_table(sched)
                self.sat_answers.append((head,body))

    def test_header(self):
        head = self.sat_answers[0][0]
        correct_head = ['Horário', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta']
        assert head == correct_head

    def test_sat1(self):
        body = self.sat_answers[0][1]
        correct_body = [['08:00-09:40', '', '', '', 'macBBB-45\n', 'macAAA-45\nmacBBB-45\n'], ['10:00-11:40', '', '', '', '', ''], ['14:00-15:40', '', '', '', 'macAAA-45\nmacBBB-45\n', ''], ['16:00-17:40', '', '', '', '', '']]
        for b, cb in tuple(zip(body, correct_body)):
            assert b == cb
    
    def test_sat2(self):
        body = self.sat_answers[1][1]
        correct_body = [['08:00-09:40', '', '', '', 'macAAA-45\nmacBBB-45\n', 'macAAA-45\nmacBBB-45\n'], ['10:00-11:40', '', '', '', '', ''], ['14:00-15:40', '', '', '', 'macBBB-45\n', ''], ['16:00-17:40', '', '', '', '', '']]
        for b, cb in tuple(zip(body, correct_body)):
            assert b == cb
    
    def test_sat3(self):
        body = self.sat_answers[2][1]
        correct_body = [['08:00-09:40', '', '', '', 'macAAA-45\nmacBBB-45\n', 'macBBB-45\n'], ['10:00-11:40', '', '', '', '', ''], ['14:00-15:40', '', '', '', 'macAAA-45\nmacBBB-45\n', ''], ['16:00-17:40', '', '', '', '', '']]
        for b, cb in tuple(zip(body, correct_body)):
            assert b == cb
    
    def test_unsat(self):
        with open("clingo-output-unsat.txt") as f:
            raw = f.read()
            answers_list = parse_input(raw)
            assert answers_list == False

