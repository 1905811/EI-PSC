import sys
from pathlib import Path

# Add the backend folder to Python's path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from models.paper import Paper
from models.material import Material
from models.device import Device
from models.layer import Layer
from models.experiment import Experiment
from models.sample import Sample
from models.measurement import Measurement
from models.evidence import Evidence
from models.performance import Performance
from models.layer import Layer


def run_tests():
    print("Testing Paper...")
    paper = Paper(title="Test Paper")
    print("✓ Passed")

    print("Testing Material...")
    material = Material(name="PbI2")
    print("✓ Passed")

    print("Testing Device...")
    device = Device(name="Device A")
    device.layers.append(Layer(order=1, material_name="ITO"))
    print("✓ Passed")

    print("Testing Experiment...")
    experiment = Experiment(name="Experiment A")
    print("✓ Passed")

    print("Testing Sample...")
    sample = Sample(name="Sample A")
    print("✓ Passed")

    print("Testing Measurement...")
    measurement = Measurement(
        name="Temperature",
        value=100,
        unit="°C",
        si_value=373.15,
        si_unit="K"
    )
    print("✓ Passed")

    print("Testing Evidence...")
    evidence = Evidence(source_text="Annealed at 100 °C")
    print("✓ Passed")

    print("Testing Performance...")
    performance = Performance(technique="J-V Curve", value=20.5, unit="mA/cm²", si_value=0.0205, si_unit="A/m²")
    print("✓ Passed")

    print("Testing Layer...")
    layer = Layer(material_name="PbI2",role="Active Layer", thickness=500, thickness_unit="nm", deposition_method="Spin Coating")
    print("✓ Passed")

    print("\n🎉 All tests passed!")


if __name__ == "__main__":
    run_tests()