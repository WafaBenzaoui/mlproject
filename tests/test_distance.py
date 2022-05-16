# tests/test_lib.py
from distance import haversine

def test_distance():
    lat1, lon1 = 48.865070, 2.380009
    lat2, lon2 = 48.864440, 2.3800

    distance = haversine(lon1, lat1, lon2, lat2)
    assert type(distance) ==float
