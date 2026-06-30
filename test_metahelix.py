# test_metahelix.py
"""
Tests for MetaHelix module.
"""

import unittest
from metahelix import MetaHelix

class TestMetaHelix(unittest.TestCase):
    """Test cases for MetaHelix class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = MetaHelix()
        self.assertIsInstance(instance, MetaHelix)
        
    def test_run_method(self):
        """Test the run method."""
        instance = MetaHelix()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
