"""Tests for the URL Shortener utility."""

import sys
from pathlib import Path
import pytest
from unittest.mock import patch, MagicMock

# Add src directory to path to import python_examples
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from python_examples.shorten_url import shorten_url


class TestShortenUrl:
    """Test suite for the shorten_url function."""

    @patch('python_examples.shorten_url.requests.get')
    def test_shorten_url_success(self, mock_get):
        """Test successful URL shortening."""
        # Arrange
        test_url = "https://example.com/very/long/url/path"
        expected_short_url = "https://tinyurl.com/abc123xyz"
        
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = expected_short_url
        mock_get.return_value = mock_response
        
        # Act
        result = shorten_url(test_url)
        
        # Assert
        assert result == expected_short_url
        mock_get.assert_called_once()
        call_args = mock_get.call_args
        assert call_args[0][0] == "http://tinyurl.com/api-create.php"
        assert call_args[1]['params'] == {'url': test_url}

    @patch('python_examples.shorten_url.requests.get')
    def test_shorten_url_with_github_url(self, mock_get):
        """Test shortening a GitHub repository URL."""
        # Arrange
        github_url = "https://github.com/vikasgautam18/python-examples"
        short_url = "https://tinyurl.com/xyz789"
        
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = short_url
        mock_get.return_value = mock_response
        
        # Act
        result = shorten_url(github_url)
        
        # Assert
        assert result == short_url

    @patch('python_examples.shorten_url.requests.get')
    def test_shorten_url_with_special_characters(self, mock_get):
        """Test shortening a URL with special characters."""
        # Arrange
        complex_url = "https://example.com/search?q=python&lang=en&sort=stars"
        short_url = "https://tinyurl.com/param123"
        
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = short_url
        mock_get.return_value = mock_response
        
        # Act
        result = shorten_url(complex_url)
        
        # Assert
        assert result == short_url
        call_args = mock_get.call_args
        assert call_args[1]['params']['url'] == complex_url

    @patch('python_examples.shorten_url.requests.get')
    def test_shorten_url_api_error(self, mock_get):
        """Test error handling when API returns non-200 status."""
        # Arrange
        test_url = "https://example.com"
        
        mock_response = MagicMock()
        mock_response.status_code = 500
        mock_get.return_value = mock_response
        
        # Act & Assert
        with pytest.raises(Exception) as exc_info:
            shorten_url(test_url)
        
        assert "Error shortening URL" in str(exc_info.value)

    @patch('python_examples.shorten_url.requests.get')
    def test_shorten_url_bad_request(self, mock_get):
        """Test error handling for bad request (400)."""
        # Arrange
        test_url = "https://example.com"
        
        mock_response = MagicMock()
        mock_response.status_code = 400
        mock_get.return_value = mock_response
        
        # Act & Assert
        with pytest.raises(Exception) as exc_info:
            shorten_url(test_url)
        
        assert "Error shortening URL" in str(exc_info.value)

    @patch('python_examples.shorten_url.requests.get')
    def test_shorten_url_service_unavailable(self, mock_get):
        """Test error handling when service is unavailable (503)."""
        # Arrange
        test_url = "https://example.com"
        
        mock_response = MagicMock()
        mock_response.status_code = 503
        mock_get.return_value = mock_response
        
        # Act & Assert
        with pytest.raises(Exception):
            shorten_url(test_url)

    @patch('python_examples.shorten_url.requests.get')
    def test_shorten_url_with_long_url(self, mock_get):
        """Test shortening a very long URL."""
        # Arrange
        long_url = "https://example.com/" + "a" * 1000
        short_url = "https://tinyurl.com/lng123"
        
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = short_url
        mock_get.return_value = mock_response
        
        # Act
        result = shorten_url(long_url)
        
        # Assert
        assert result == short_url
        assert len(result) < len(long_url)

    @patch('python_examples.shorten_url.requests.get')
    def test_shorten_url_network_error(self, mock_get):
        """Test error handling when network request fails."""
        # Arrange
        test_url = "https://example.com"
        mock_get.side_effect = Exception("Network error")
        
        # Act & Assert
        with pytest.raises(Exception):
            shorten_url(test_url)

    @patch('python_examples.shorten_url.requests.get')
    def test_shorten_url_response_whitespace(self, mock_get):
        """Test that response with whitespace is handled correctly."""
        # Arrange
        test_url = "https://example.com"
        short_url_with_newline = "https://tinyurl.com/abc123\n"
        
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = short_url_with_newline
        mock_get.return_value = mock_response
        
        # Act
        result = shorten_url(test_url)
        
        # Assert
        assert result == short_url_with_newline  # Returns as-is

    @patch('python_examples.shorten_url.requests.get')
    def test_shorten_url_empty_response(self, mock_get):
        """Test handling of empty response text."""
        # Arrange
        test_url = "https://example.com"
        
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = ""
        mock_get.return_value = mock_response
        
        # Act
        result = shorten_url(test_url)
        
        # Assert
        assert result == ""

    @patch('python_examples.shorten_url.requests.get')
    def test_shorten_url_multiple_calls(self, mock_get):
        """Test that the function works correctly across multiple calls."""
        # Arrange
        urls = [
            "https://example1.com",
            "https://example2.com",
            "https://example3.com"
        ]
        short_urls = [
            "https://tinyurl.com/url1",
            "https://tinyurl.com/url2",
            "https://tinyurl.com/url3"
        ]
        
        mock_response = MagicMock()
        mock_response.status_code = 200
        
        # Set up side effects for multiple calls
        mock_get.side_effect = [
            MagicMock(status_code=200, text=short_urls[0]),
            MagicMock(status_code=200, text=short_urls[1]),
            MagicMock(status_code=200, text=short_urls[2])
        ]
        
        # Act & Assert
        for original, expected_short in zip(urls, short_urls):
            result = shorten_url(original)
            assert result == expected_short
        
        assert mock_get.call_count == 3
