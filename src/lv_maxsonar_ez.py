from typing import ClassVar, Mapping, Any, Dict, Optional
from typing_extensions import Self

from viam.module.types import Reconfigurable
from viam.components.component_base import ValueTypes
from viam.proto.app.robot import ComponentConfig
from viam.proto.common import ResourceName
from viam.resource.base import ResourceBase
from viam.resource.types import Model, ModelFamily

from viam.components.sensor import Sensor
from viam.logging import getLogger

import time

from periphery import GPIO

LOGGER = getLogger(__name__)


class LVMAXSONAREZ(Sensor, Reconfigurable):
    MODEL: ClassVar[Model] = Model(
        ModelFamily("emery", "sensor"), "lv-maxsonar-ez"
    )

    rx_pin: int
    pw_pin: int

    @classmethod
    def new(
        cls,
        config: ComponentConfig,
        dependencies: Mapping[ResourceName, ResourceBase],
    ) -> Self:
        """Contructor."""
        sensor = cls(config.name)
        sensor.reconfigure(config, dependencies)
        return sensor

    @classmethod
    def validate(cls, config: ComponentConfig):
        """Validates JSON Configuration."""
        rx_pin = config.attributes.fields["rx_pin"].number_value
        if rx_pin is None or rx_pin == "":
            raise Exception("A rx_pin must be defined")
        pw_pin = config.attributes.fields["pw_pin"].number_value
        if pw_pin is None or pw_pin == "":
            raise Exception("A pw_pin must be defined")
        return

    def reconfigure(
        self,
        config: ComponentConfig,
        dependencies: Mapping[ResourceName, ResourceBase],
    ):
        """Handles attribute reconfiguration."""
        self.rx_pin = int(config.attributes.fields["rx_pin"].number_value)
        self.pw_pin = int(config.attributes.fields["pw_pin"].number_value)
        # set both pins to low state
        rx = GPIO(self.rx_pin, "out")
        rx.write(False)

        return

    # Implement the methods the Viam RDK defines for the sensor API
    # (rdk:component:sensor)

    async def get_readings(
        self, extra: Optional[Dict[str, Any]] = None, **kwargs
    ):
        """Get sensor reading in centimeters."""
        trigger_pulse_duration = 0.00002
        pulse_width_cm_scale = 147

        rx = GPIO(self.rx_pin, "out")
        pw = GPIO(self.pw_pin, "in")

        rx.write(True)
        time.sleep(trigger_pulse_duration)
        rx.write(False)

        while pw.read() is False:
            pulse_start = time.time()

        while pw.read() is True:
            pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start

        distance = pulse_duration * pulse_width_cm_scale
        distance = round(distance, 2)

        rx.close()
        pw.close()

        return {"distance": distance}

    async def do_command(
        self,
        command: Mapping[str, ValueTypes],
        *,
        timeout: Optional[float] = None,
        **kwargs
    ):
        pass
