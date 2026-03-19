import pytest

from pyvrp_v12 import solve
from pyvrp_v12.stop import MaxIterations


@pytest.mark.parametrize("instance", ["vrptw", "mdvrp", "vrpb", "mtvrptwr"])
def test_solve(instance, benchmark, request):
    """
    Tests performance of solving various instances.
    """
    data = request.getfixturevalue(instance)
    benchmark(solve, data, stop=MaxIterations(1), seed=0)
