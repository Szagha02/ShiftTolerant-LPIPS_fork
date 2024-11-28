from setuptools import setup, find_packages

setup(
    name="shift_tolerant_lpips",
    version="0.1.0",
    description="Shift-Tolerant LPIPS Implementation",
    author="Abhijay Ghidyal",
    license="MIT", 
    packages=find_packages(include=["*", "util.*", "stlpips.*"]),
    install_requires=[
        "numpy", 
        "torch",
        "scipy",
        "Pillow",
        "torchvision",
        "numpy",
        "scipy",
        "scikit-image", ],
)
