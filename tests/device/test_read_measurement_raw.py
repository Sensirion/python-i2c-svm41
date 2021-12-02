# -*- coding: utf-8 -*-
# (c) Copyright 2021 Sensirion AG, Switzerland

from __future__ import absolute_import, division, print_function
from sensirion_i2c_svm41.response_types import Humidity, Temperature
import pytest
import time


@pytest.mark.needs_device
def test(device):
    """
    Test if read_measured_values_raw() returns the expected values.
    """
    device.start_measurement()
    time.sleep(1.1)

    # check the read values
    raw_humidity, raw_temperature, raw_voc_ticks, raw_nox_ticks = \
        device.read_measured_values_raw()
    # raw types
    assert type(raw_humidity) is Humidity
    assert type(raw_humidity.ticks) is int
    assert type(raw_humidity.percent_rh) is float
    assert type(raw_temperature) is Temperature
    assert type(raw_temperature.ticks) is int
    assert type(raw_temperature.degrees_celsius) is float
    assert type(raw_temperature.degrees_fahrenheit) is float
    assert type(raw_voc_ticks) is int
    assert type(raw_nox_ticks) is int
