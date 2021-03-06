# coding=utf-8
""" Tests for the abstract class and sensor classes """
import pytest
from collections import Iterator
from testfixtures import LogCapture

from mycodo.inputs.base_input import AbstractInput

from mycodo.inputs.am2315 import InputModule as AM2315Sensor
from mycodo.inputs.atlas_ph import InputModule as AtlaspHSensor
from mycodo.inputs.atlas_pt1000 import InputModule as AtlasPT1000Sensor
from mycodo.inputs.bh1750 import InputModule as BH1750Sensor
from mycodo.inputs.bme280 import InputModule as BME280Sensor
from mycodo.inputs.bmp180 import InputModule as BMP180Sensor
from mycodo.inputs.bmp280 import InputModule as BMP280Sensor
from mycodo.inputs.chirp import InputModule as ChirpSensor
from mycodo.inputs.dht11 import InputModule as DHT11Sensor
from mycodo.inputs.dht22 import InputModule as DHT22Sensor
from mycodo.inputs.ds18b20 import InputModule as DS18B20Sensor
from mycodo.inputs.htu21d import InputModule as HTU21DSensor
from mycodo.inputs.k30 import InputModule as K30Sensor
from mycodo.inputs.linux_command import InputModule as LinuxCommand
from mycodo.inputs.mh_z16 import InputModule as MHZ16Sensor
from mycodo.inputs.mh_z19 import InputModule as MHZ19Sensor
from mycodo.inputs.mycodo_ram import InputModule as MycodoRam
from mycodo.inputs.raspi import InputModule as RaspberryPiCPUTemp
from mycodo.inputs.raspi_cpuload import InputModule as RaspberryPiCPULoad
from mycodo.inputs.raspi_freespace import InputModule as RaspberryPiFreeSpace
from mycodo.inputs.sht1x_7x import InputModule as SHT1x7xSensor
from mycodo.inputs.sht2x import InputModule as SHT2xSensor
from mycodo.inputs.signal_pwm import InputModule as SignalPWMInput
from mycodo.inputs.signal_revolutions import InputModule as SignalRPMInput
from mycodo.inputs.tmp006 import InputModule as TMP006Sensor
from mycodo.inputs.tsl2561 import InputModule as TSL2561Sensor
from mycodo.inputs.tsl2591_sensor import InputModule as TSL2591Sensor


input_classes = [
    AM2315Sensor(None, testing=True),
    AtlaspHSensor(None, testing=True),
    AtlasPT1000Sensor(None, testing=True),
    BH1750Sensor(None, testing=True),
    BME280Sensor(None, testing=True),
    BMP180Sensor(None, testing=True),
    BMP280Sensor(None, testing=True),
    ChirpSensor(None, testing=True),
    DHT11Sensor(None, testing=True),
    DHT22Sensor(None, testing=True),
    DS18B20Sensor(None, testing=True),
    HTU21DSensor(None, testing=True),
    K30Sensor(None, testing=True),
    LinuxCommand(None, testing=True),
    MHZ16Sensor(None, testing=True),
    MHZ19Sensor(None, testing=True),
    MycodoRam(None, testing=True),
    RaspberryPiCPUTemp(None, testing=True),
    RaspberryPiCPULoad(None, testing=True),
    RaspberryPiFreeSpace(None, testing=True),
    SHT1x7xSensor(None, testing=True),
    SHT2xSensor(None, testing=True),
    SignalPWMInput(None, testing=True),
    SignalRPMInput(None, testing=True),
    TMP006Sensor(None, testing=True),
    TSL2561Sensor(None, testing=True),
    TSL2591Sensor(None, testing=True)
]


# ----------------------------
#   AbstractInput
# ----------------------------
def test_abstract_input_read_method_logs_when_not_implemented():
    """  verify that methods that are not overwritten log as errors"""
    with LogCapture() as log_cap:
        with pytest.raises(NotImplementedError):
            AbstractInput().read()
    expected_error = ('mycodo.inputs.base_input', 'ERROR', ('AbstractInput did not overwrite the read() '
                                                            'method.  All subclasses of the AbstractInput '
                                                            'class are required to overwrite this method'))
    assert expected_error in log_cap.actual()


def test_abstract_input_next_method_logs_when_not_implemented():
    """ verify that methods that are not overwritten log as errors"""
    with LogCapture() as log_cap:
        with pytest.raises(NotImplementedError):
            AbstractInput().next()
    expected_error = ('mycodo.inputs.base_input', 'ERROR', ('AbstractInput did not overwrite the next() '
                                                            'method.  All subclasses of the AbstractInput '
                                                            'class are required to overwrite this method'))
    assert expected_error in log_cap.actual()


# ----------------------------
#   General class tests
# ----------------------------
def test_inputs_have_depreciated_stop_sensor():
    """ Verify that the input objects have the stop_sensor() method """
    for each_class in input_classes:
        assert hasattr(each_class, 'stop_sensor')


def test_inputs_are_iterator_instance():
    """ Verify that the input objects are and behave like an iterator """
    for each_class in input_classes:
        assert isinstance(each_class, Iterator), "{cls} is not an iterator instance".format(cls=each_class.__class__.__name__)
