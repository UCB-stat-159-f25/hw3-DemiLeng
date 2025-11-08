import os
import pytest
import numpy as np
import ligotools.readligo as rl


def test_import_module():
    assert hasattr(rl, "loaddata"), "readligo should define loaddata()"

def test_loaddata_file_not_found():
    result = rl.loaddata("data/nonexistent_file.hdf5", "H1")
    assert result is None or isinstance(result, tuple)
