#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Nayden
"""

import math

class Item:
    _exempt = {'book', 'food', 'med'}
    def __init__(self, typ, price, imported, desc):
        self._typ = typ
        self._price = price
        self._imported = imported
        self._desc = desc
        self._total_price = self._price
        self._taxes = 0
        if self._imported:
            self._taxes += 0.05*self._price
        if self._typ not in self._exempt:
            self._taxes += 0.1*self._price
        self._taxes = (math.ceil(self._taxes*20))/20
        self._total_price += self._taxes
            
    def get_price(self):
        return self._total_price, self._taxes
    
    def get_desc(self):
        return self._desc
        
class Receipt:
    def __init__(self, item_params):
        self._ietm_params = item_params
        self._items = []
        for par in self._ietm_params:
            item_cnt = par[0]
            item = Item(*par[1:])
            self._items.append((item_cnt, item))
    
    def get_receipt(self):
        total = 0
        tax = 0
        to_be_printed = []
        for item in self._items:
            item_cnt = item[0]
            price = item[1].get_price()
            desc = item[1].get_desc()
            to_be_printed.append('{} {}: {:.2f}'.format(item_cnt, desc, price[0]))
            total += price[0]
            tax += price[1]
        to_be_printed.append('Sales Taxes: {:.2f}'.format(tax))
        to_be_printed.append('Total: {:.2f}'.format(total))
        
        return '\n'.join(to_be_printed)
            
    def print_receipt(self):
        rec = self.get_receipt()
        for r in rec:
            print(r)