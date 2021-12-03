API Reference
=============


Svm41I2cDevice
--------------

.. automodule:: sensirion_i2c_svm41.device


Response Data Types
-------------------

Air Quality VOC
^^^^^^^^^^^^^^^

.. autoclass:: sensirion_i2c_svm41.response_types.AirQualityVoc

Air Quality NOx
^^^^^^^^^^^^^^^

.. autoclass:: sensirion_i2c_svm41.response_types.AirQualityNox

Humidity
^^^^^^^^

.. autoclass:: sensirion_i2c_svm41.response_types.Humidity

Temperature
^^^^^^^^^^^

.. autoclass:: sensirion_i2c_svm41.response_types.Temperature

Version
^^^^^^^

.. automodule:: sensirion_i2c_svm41.version_types


Commands
--------

.. autoclass:: sensirion_i2c_svm41.commands.generated.Svm41I2cCmdGetSerialNumber
.. autoclass:: sensirion_i2c_svm41.commands.generated.Svm41I2cCmdDeviceReset
.. autoclass:: sensirion_i2c_svm41.commands.generated.Svm41I2cCmdStartMeasurement
.. autoclass:: sensirion_i2c_svm41.commands.generated.Svm41I2cCmdStopMeasurement
.. autoclass:: sensirion_i2c_svm41.commands.generated.Svm41I2cCmdGetVocAlgorithmTuningParameters
.. autoclass:: sensirion_i2c_svm41.commands.generated.Svm41I2cCmdSetVocAlgorithmTuningParameters
.. autoclass:: sensirion_i2c_svm41.commands.generated.Svm41I2cCmdGetVocAlgorithmState
.. autoclass:: sensirion_i2c_svm41.commands.generated.Svm41I2cCmdSetVocAlgorithmState
.. autoclass:: sensirion_i2c_svm41.commands.generated.Svm41I2cCmdGetNoxAlgorithmTuningParameters
.. autoclass:: sensirion_i2c_svm41.commands.generated.Svm41I2cCmdSetNoxAlgorithmTuningParameters
.. autoclass:: sensirion_i2c_svm41.commands.generated.Svm41I2cCmdStoreNvData
.. autoclass:: sensirion_i2c_svm41.commands.wrapped.Svm41I2cCmdGetVersion
.. autoclass:: sensirion_i2c_svm41.commands.wrapped.Svm41I2cCmdReadMeasuredValues
.. autoclass:: sensirion_i2c_svm41.commands.wrapped.Svm41I2cCmdReadMeasuredValuesRaw
.. autoclass:: sensirion_i2c_svm41.commands.wrapped.Svm41I2cCmdGetTemperatureOffsetForRhtMeasurements
.. autoclass:: sensirion_i2c_svm41.commands.wrapped.Svm41I2cCmdSetTemperatureOffsetForRhtMeasurements
