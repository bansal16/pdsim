import motor # To force cx_freeze to import motor.py

from PDSim.flow.flow_models import IsentropicNozzleWrapper
from PDSim.flow.flow import FlowPath
from PDSim.core.core import PDSimCore, struct
from PDSim.core.containers import Tube, ControlVolume
from PDSim.core.motor import Motor
from PDSim.plot.plots import debug_plots