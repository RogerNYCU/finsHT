from abc import abstractmethod
from math import floor, sqrt, log, tanh, exp,sin, tan, cosh, cos, pi
class FinBase:
    """Base class for fins."""

    def __init__(self, k=None, pitch=None, thickness=None):
        self.k = k
        self.F_p = pitch
        self.delta = thickness
        

    @abstractmethod
    def __post_init__(self):
        pass

    @abstractmethod
    def calc_areas(self):
        pass

    @abstractmethod
    def calc_pressure_drop(self):
        pass

    @abstractmethod
    def calc_efficiency(self):
        pass

    @abstractmethod
    def calc_heat_transfer_coefficient(self):
        pass

class LouverFinFlatTube(FinBase):
    """
    LouverFinFlatTube is a class representing a louver fin used in heat exchangers.
    Attributes:
        L_p (float): Louver pitch.
        L_h (float): Louver height.
        theta (float): Louver angle.
        L_l (float): Louver length.
        F_d (float): Depth of the fin.
        D_c (float): Outer diameter of the tube.
        N (int): Number of fins.
        Re_L_p (float): Reynolds number based on louver pitch.
        D_h (float): Hydraulic diameter.
        h_c (float): Heat transfer coefficient.
        eta (float): Efficiency of the fin.
        eta_overall (float): Overall efficiency of the fin.
        pressure_drop (float): Pressure drop across the fin.
        A_frontal (float): Frontal area of the fin.
        A_c (float): Effective cooling area.
        sigma (float): Area ratio.
        F_L (float): Length of the fin.
        N_L (int): Number of louver fins.
        A_fin (float): Area of the fin.
        _A_tube (float): Area of the tube.
        A_total (float): Total area of the fin and tube.
        A_total_per_unit_length (float): Total area per unit length.
    Methods:
        __post_init__(outside_tube_diameter, mu_air, rho_air, cp_air, Pr_air, air_velocity, coil_length, P_t, P_l, tube_depth):
            Initializes the fin properties and calculates various parameters.
        calc_pressure_drop(outside_tube_diameter, rho, velocity, P_t, tube_depth):
            Calculates the pressure drop across the fin.
        calc_efficiency(P_t, P_l):
            Calculates the efficiency of the fin.
        calc_heat_transfer_coefficient(rho, cp, Pr, velocity, P_t, tube_depth):
            Calculates the heat transfer coefficient.
        calc_areas(coil_length, P_t, tube_depth):
            Calculates the areas related to the fin and tube.
        calc_j(tube_depth, P_t):
            Calculates the j-factor for heat transfer.
    """
    """Louver fin."""

    def __init__(
        self,
        k=None,
        pitch=None,
        thickness=None,
        
    ):
        super().__init__(k, pitch, thickness)
        print("You have created a LouverFinFlatTube")
        