from setuptools import setup, find_packages

setup(
    name="sales-forecasting-prophet",
    version="1.0.0",
    author="Iftakhar Ahmad",
    author_email="iftakharahmad1458@gmail.com",
    url="https://github.com/Iftakharahmad17/sales-forecasting-prophet.git"
    description="Sales forecasting with Facebook Prophet",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[
        "pandas>=2.1.4",
        "numpy>=1.24.3",
        "prophet>=1.1.5",
        "scikit-learn>=1.3.2",
        "matplotlib>=3.8.2",
        "seaborn>=0.13.0",
        "loguru>=0.7.2",
        "pyyaml>=6.0.1",
    ],
)
