"""
 Module Name: conftest.py
 Author: thibault2705 
 Date: 2025-11-16
 Description: conftest.py a special configuration file of pytest.
 """

import pytest
from loguru import logger
import io

@pytest.fixture
def log_capture_fixture():
    # Use an in-memory buffer to capture logs
    log_output = io.StringIO()
    handler_id = logger.add(log_output, format="{message}")

    yield log_output

    # Clean up the handler after the test is done
    logger.remove(handler_id)