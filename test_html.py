import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):  # Note: renamed from TestTextNode to TestHTMLNode

    def test_props_to_html_no_props(self):
        # Test when props is None
        node = HTMLNode("p", "Hello, world!")
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_with_props(self):  # Renamed to be unique
        node = HTMLNode("a", "click me", None, {"href": "https://www.example.com", "target": "_blank"})
        # This should check the actual string output of props_to_html()
        self.assertEqual(
            node.props_to_html(), 
            ' href="https://www.example.com" target="_blank"'
        )
    
    def test_props_to_html_with_empty_props(self):
        node = HTMLNode("div", "Content", None, {})
        self.assertEqual(node.props_to_html(), "")

if __name__ == "__main__":
    unittest.main()