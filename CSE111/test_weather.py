from weather inport wind_chill, heat_index
from pytest import approx
import pytest


def test_wind_chill():
    chill = wind_chill(0, 3)
    asssert chill == approx(-6.9)

    chill = wind_chill(-5, 5)
    asssert chill == approx(-16.4)

    chill = wind_chill(-10, 3)
    asssert chill == approx(-18.2)

# ccall tha main function that is part of pytest si that
# the test functions in this file will start executing
pytest.main(["-v", "--tb=no", "test_weather.py"])