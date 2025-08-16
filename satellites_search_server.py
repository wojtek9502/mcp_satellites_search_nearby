from typing import Annotated

from mcp.server.fastmcp import FastMCP
from pydantic import Field, BaseModel

from satellites_search.satellite_search import SatelliteSearch

mcp = FastMCP("satellites_searcher")
DEFAULT_TLE = 'https://celestrak.org/NORAD/elements/stations.txt'


# tip: do not try to pass pydantic class here, it will cause errors
# provide parameters directly like below
@mcp.tool()
async def get_satellite_passes(
    lat: Annotated[str, Field(description="Latitude of the observer. Plain decimal coordinates (e.g., '50.0647')")],
    lon: Annotated[str, Field(description="Longitude of the observer. Plain decimal coordinates (e.g., '19.9450')")],
    satellite_name: Annotated[str, Field(description="Name of the satellite to track (default: ISS (ZARYA))")] = 'ISS (ZARYA)',
    range_days: Annotated[int, Field(description="Number of days to search for satellite passes (default: 10)")] = 10,
    tle_url: Annotated[str, Field(description="URL of the TLE file to download")] = DEFAULT_TLE,
    timezone_name: Annotated[str, Field(description="Timezone for the observer (default: UTC)")] = 'UTC',
    elevation_m: Annotated[int, Field(description="Observer's elevation in meters (default: 200)")] = 200,
    min_culmination_altitude_deg: Annotated[int, Field(description="Minimum satellite altitude above horizon in degrees (default: 15)")] = 15,
) -> str:
    """
        Get the satellite passes. Use this tool to calculate the satellite passes.
    """
    print(f'Searching satellite passes. Timezone: {timezone_name}')
    satellite_search = SatelliteSearch(
        tle_url=tle_url,
        satellite_name=satellite_name,
        lat=float(lat),
        lon=float(lon),
        range_days=range_days,
        timezone_param=timezone_name,
        elev=elevation_m,
        min_culmination_altitude_deg=min_culmination_altitude_deg
    )
    search_results_text = await satellite_search.calculate_satellites_nearby()
    return search_results_text

if __name__ == "__main__":
    mcp.run(transport='stdio')