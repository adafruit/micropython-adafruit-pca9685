from distutils.core import setup


setup(
    name='micropython-adafruit-pca9685',
    py_modules=['pca9685', 'servo', 'motor'],
    version="1.0",
    description="Driver for MicroPython for the PCA9685 PWM driver.",
    long_description="""\
This library lets you control the motor and servo drivers based on PCA9685.""",
    author='Radomir Dopieralski',
    author_email='micropython@sheep.art.pl',
    classifiers = [
        'Development Status :: 6 - Mature',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
)
