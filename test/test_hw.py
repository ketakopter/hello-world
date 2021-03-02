import sys
import os
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))

import hw.hw

def test_hw():
  assert hw.hw.data_to_str() == '43.5'
