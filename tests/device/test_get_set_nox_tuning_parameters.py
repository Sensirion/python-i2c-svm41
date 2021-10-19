# -*- coding: utf-8 -*-
# (c) Copyright 2021 Sensirion AG, Switzerland

from __future__ import absolute_import, division, print_function
import pytest


@pytest.mark.needs_device
def test(device):
    """
    Test if set_nox_tuning_parameters() and get_nox_tuning_parameters() work
    as expected.
    """
    device.set_nox_tuning_parameters(10, 12, 16, 80, 60, 210)
    nox_index_offset, learning_time_offset_hours, learning_time_gain_hours, \
        gating_max_duration_minutes, std_initial, gain_factor \
        = device.get_nox_tuning_parameters()
    assert nox_index_offset == 10
    assert learning_time_offset_hours == 12
    assert learning_time_gain_hours == 16
    assert gating_max_duration_minutes == 80
    assert std_initial == 60
    assert gain_factor == 210
