# -*- coding: utf-8 -*-
# (c) Copyright 2021 Sensirion AG, Switzerland

from __future__ import absolute_import, division, print_function
import pytest
import time


@pytest.mark.needs_device
def test(device):
    """
    Test if start_measurement() and stop_measurement() work as expected.
    """

    # start continuous measurement and make sure it worked
    device.start_measurement()
    time.sleep(1.1)
    humidity, temperature, voc_index, nox_index = device.read_measured_values()
    assert humidity.percent_rh > 0

    # stop and restart measurement
    device.stop_measurement()
    humidity, temperature, voc_index, nox_index = device.read_measured_values()
    assert humidity.percent_rh == 0
    device.start_measurement()
    time.sleep(1.1)
    humidity, temperature, voc_index, nox_index = device.read_measured_values()
    assert humidity.percent_rh > 0
