#!/usr/bin/env python
# -*- coding: utf-8 -*-

class log:
    def __init__(self):
        self.log_counter = {}
        self.priority_status = {
            0: 'LOG',
            1: 'CRITICAL'
        }
        for status in self.priority_status.keys():
            self.log_counter[int(status)] = 0

    def write(self, *message, TYPE=None):
        text_message = ''
        for element in message:
            text_message += str(element)
        if TYPE is None:
            print('{text}'.format(text=text_message))
        elif type(TYPE) is int:
            print('[{type}-{counter}]: {text}'.format(type = self.priority_status[TYPE],
                                                    counter = self.log_counter[TYPE],
                                                    text = text_message))
            self.log_counter[TYPE] += 1
        else:
            print("[LOG-ERROR]: {text}". format(text = text_message))