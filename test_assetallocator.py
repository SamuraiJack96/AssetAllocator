# test_assetallocator.py
"""
Tests for AssetAllocator module.
"""

import unittest
from assetallocator import AssetAllocator

class TestAssetAllocator(unittest.TestCase):
    """Test cases for AssetAllocator class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = AssetAllocator()
        self.assertIsInstance(instance, AssetAllocator)
        
    def test_run_method(self):
        """Test the run method."""
        instance = AssetAllocator()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
