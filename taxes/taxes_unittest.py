#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Nayden
"""

from unittest import TestCase, main
from taxes import Item, Receipt

class TaxesTest(TestCase):
    def test_item_exempt_1(self):
        '''Test price is not updated for exempt items'''
        item = Item('book', 10.00, False, 'dummy item')
        self.assertEqual(item.get_price()[0], 10.00)
        
    def test_item_exempt_2(self):
        '''Test price is not updated for exempt items'''
        item = Item('med', 10.00, False, 'dummy item')
        self.assertEqual(item.get_price()[0], 10.00)
        
    def test_item_exempt_3(self):
        '''Test price is not updated for exempt items'''
        item = Item('food', 10.00, False, 'dummy item')
        self.assertEqual(item.get_price()[0], 10.00)
        
    def test_item_exempt_imported_3(self):
        '''Test price is updated only with import tax for imported exempt items'''
        item = Item('food', 10.00, True, 'dummy item')
        self.assertEqual(item.get_price()[0], 10.50)
    
    def test_item_non_exempt_4(self):
        '''Test price is updated correctly for non exempt items'''
        item = Item('-', 10.00, False, 'dummy item')
        self.assertEqual(item.get_price()[0], 11.00)
    
    def test_item_non_exempt_imported_5(self):
        '''Test price is updated correctly for imported non exempt items'''
        item = Item('-', 10.00, True, 'dummy item')
        self.assertEqual(item.get_price()[0], 11.50)
        
    def test_item_rounded_taxes_6(self):
        '''Test taxes are rounded up to the closest multiple of 0.05 above'''
        item = Item('-', 10.3, True, 'dummy item')
        self.assertEqual(item.get_price()[1], 1.55)
        
    def test_item_rounded_taxes_7(self):
        '''Test taxes are not rounded up for tax equal to multiple of 0.05'''
        item = Item('-', 10.35, True, 'dummy item')
        self.assertEqual(item.get_price()[1], 1.60)
    
    def test_receipt_1(self):
        '''Test correct receipt'''
        receipt = Receipt([[1, 'book' , 12.49, False, 'book'],
                           [1, 'music CD', 14.99, False, 'music CD'],
                           [1, 'food', 0.85, False, 'chocolate bar']])
        self.assertEqual(receipt.get_receipt(), 
                         '1 book: 12.49\n' +
                         '1 music CD: 16.49\n' +
                         '1 chocolate bar: 0.85\n' +
                         'Sales Taxes: 1.50\n' +
                         'Total: 29.83')
    
    def test_receipt_2(self):
        '''Test correct receipt'''
        receipt = Receipt([[1, 'food' , 10.00, True, 'imported box of chocolates'],
                           [1, 'perfume', 47.50, True, 'imported bottle of perfume']])
        self.assertEqual(receipt.get_receipt(), 
                         '1 imported box of chocolates: 10.50\n' +
                         '1 imported bottle of perfume: 54.65\n' +
                         'Sales Taxes: 7.65\n' +
                         'Total: 65.15')
    
    def test_receipt_3(self):
        '''Test correct receipt'''
        receipt = Receipt([[1, 'perfume', 27.99, True, 'imported bottle of perfume'],
                           [1, 'perfume', 18.99, False, 'bottle of perfume'],
                           [1, 'med', 9.75, False, 'packet of headache pills'],
                           [1, 'food' , 11.25, True, 'imported box of chocolates']])
        self.assertEqual(receipt.get_receipt(), 
                         '1 imported bottle of perfume: 32.19\n' +
                         '1 bottle of perfume: 20.89\n' +
                         '1 packet of headache pills: 9.75\n' +
                         '1 imported box of chocolates: 11.85\n' +
                         'Sales Taxes: 6.70\n' +
                         'Total: 74.68')
        
if __name__ == '__main__':
    main()