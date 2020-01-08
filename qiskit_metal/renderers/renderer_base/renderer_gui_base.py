# -*- coding: utf-8 -*-

# This code is part of Qiskit.
#
# (C) Copyright IBM 2019.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

"""
@auhtor: Zlatko Minev, ... (IBM)
@date: 2019
"""

from ...designs import DesignBase, is_design
from ...elements import ElementTables

from . import RendererBase

__all__ = ['RendererGuiBase']

class RendererGuiBase(RendererBase):
    """Abstract base class for the GUI rendering. Extends RendererBase.
    An interface class.
    """

    name = 'guibase'  # overwrite this!

    def __init__(self, gui, design: DesignBase, initiate=True, fig=None, ax=None):
        super().__init__(design=design, initiate=initiate)

        self.gui=gui
        self.fig=None # current figure
        self.ax=None # current ax

    def set_fig(self, fig):
        self.fig=fig

    def set_ax(self,ax):
        self.ax=ax

    def setup_fig(self, fig):
        raise NotImplementedError()

    def style_axis(self, ax):
        raise NotImplementedError()

    def render_design(self):
        for name, component in self.design.components.items():
            self.plot_component(component)

    def render_component(self):
        raise NotImplementedError()

    def render_shapely(self):
        raise NotImplementedError()

    def render_connectors(self):
        raise NotImplementedError()

    def clear_axis(self):
        raise NotImplementedError()

    def clear_figure(self):
        raise NotImplementedError()
