import numpy as np
import pytest
from scipy.io import wavfile
from ligotools.utils import whiten, reqshift, write_wavfile

def test_reqshift_preserves_energy():
    fs = 4096
    t = np.linspace(0, 1, fs)
    sig = np.sin(2 * np.pi * 100 * t)
    shifted = reqshift(sig, 1.1)
    assert np.isclose(np.sum(sig**2), np.sum(shifted**2), rtol=0.1)


def test_write_wavfile(tmp_path):
    fs = 4096
    data = np.random.randn(fs).astype(np.float32)
    filename = tmp_path / "test.wav"

    write_wavfile(str(filename), fs, data)
    rate, read_data = wavfile.read(filename)
    assert rate == fs
    assert read_data.shape == data.shape