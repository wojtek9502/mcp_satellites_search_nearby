from typing import Annotated

from agents import function_tool
from pydantic import Field, BaseModel

from satellites_search.satellite_search import SatelliteSearch

DEFAULT_TLE = 'https://celestrak.org/NORAD/elements/stations.txt'

class SatelliteSearchQueryParams(BaseModel):
    lat: Annotated[str, Field(description="Latitude of the observer. Plain decimal coordinates (e.g., '50.0647')")]
    lon: Annotated[str, Field(description="Longitude of the observer. Plain decimal coordinates (e.g., '19.9450')")]
    satellite_name: Annotated[str, Field(description="Name of the satellite to track (default: ISS (ZARYA))")] = 'ISS (ZARYA)'
    range_days: Annotated[int, Field(description="Number of days to search for satellite passes (default: 10)")] = 10
    tle_url: Annotated[str, Field(description="URL of the TLE file to download")] = DEFAULT_TLE
    timezone_name: Annotated[str, Field(description="Timezone for the observer (default: UTC)")] = 'UTC'
    elevation_m: Annotated[int, Field(description="Observer's elevation in meters (default: 200)")] = 200
    min_above_horizon_deg: Annotated[int, Field(description="Minimum satellite altitude above horizon in degrees (default: 1)")] = 1

@function_tool
async def get_satellite_passes(query_params: SatelliteSearchQueryParams) -> str:
    """
        Get satellite passes.
    """

    print(f'Searching satellite passes. Timezone: {query_params.timezone_name}')
    satellite_search = SatelliteSearch(
        tle_url=query_params.tle_url,
        satellite_name=query_params.satellite_name,
        lat=float(query_params.lat),
        lon=float(query_params.lon),
        range_days=query_params.range_days,
        calc_resolution_min=1,
        timezone_param=query_params.timezone_name,
        elev=query_params.elevation_m,
        min_above_horizon_deg=query_params.min_above_horizon_deg
    )
    search_results_text = await satellite_search.calculate_satellites_nearby()
    return search_results_text