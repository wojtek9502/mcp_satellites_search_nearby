# Fetch MCP Server
A Model Context Protocol server with satellites passes near your location search capabilities. This server enables LLMs to run satellites searcher with proper parameters based on your input.  
It is an MCP Server version of the project: [satellites_search_nearby](https://github.com/wojtek9502/satellites_search_nearby)

### Available objects to track with the default TLE
- ISS (ZARYA)  
- CSS (TIANHE)  
- FREGAT DEB  
- CSS (WENTIAN)  
- CSS (MENGTIAN)  
- PROGRESS-MS 30  
- SOYUZ-MS 27  
- SHENZHOU-20 (SZ-20)  
- PROGRESS-MS 31  
- TIANZHOU-9  
- CREW DRAGON 11

### Requirements
- Minimal LLM: gpt-4.1-mini

### MCP Config

uv config example
```json
 {"command": "uv", "args": ["run", "satellites_search_server.py"]}
```

### Available tool and params
- `get_satellite_passes` - Calculate satellite passes near your location.
  - `lat` **(string, required)**: Latitude of the observer. Plain string coordinates (e.g., '50.0647')
  - `lon` **(string, required)**: Longitude of the observer. Plain string coordinates (e.g., '19.9450')
  - `satellite_name` (str, optional): Name of the satellite to track (default: 'ISS (ZARYA)')
  - `range_days` (integer, optional): Number of days to search for satellite passes (default: 10)
  - `tle_url` (str, optional): URL of the TLE file to download Default: 'https://celestrak.org/NORAD/elements/stations.txt'
  - `timezone_name` (str, optional): Timezone for the observer (default: UTC)
  - `elevation_m` (int, optional): Observer's elevation in meters (default: 200)
  - `min_culmination_altitude_deg` (str, optional): Minimum satellite altitude above horizon, in culmination, in degrees (default: 15)

### Example usage with an Agent
1. Install requirements (Python 3.11+):
    ```shell
    pip install -r requirements.txt
    ```

2. Create .env file. See .env_example for the details

3. Run script example_run.py
    ```shell
    python example_run.py
    ```

### Prompts examples

---  
***Context: Minimal prompt with required params only. Coordinates are passed, no satellite name provided***   
Prompt:My coordinates are 50.06143 19.93658.  
Expected Response: 'ISS (ZARYA)' satellite passes for the next 10 days
<details>
<summary>AI response</summary>

```text
Passes of satellite 'ISS (ZARYA)' over location (50.06143, 19.93658) during the next 10 days:

| Satellite   | Start (UTC)                | Altitude   | Azimuth   | Culmination (UTC)          | Altitude   | Azimuth   | End (UTC)                  | Altitude   | Azimuth   |
|-------------|----------------------------|------------|-----------|----------------------------|------------|-----------|----------------------------|------------|-----------|
| ISS (ZARYA) | 2025-08-19 02:55:23 +00:00 | 0.0°       | 201.3°    | 2025-08-19 03:00:10 +00:00 | 16.1°      | 139.2°    | 2025-08-19 03:04:59 +00:00 | -0.0°      | 77.3°     |
| ISS (ZARYA) | 2025-08-21 02:54:29 +00:00 | 0.0°       | 222.6°    | 2025-08-21 02:59:44 +00:00 | 32.4°      | 147.8°    | 2025-08-21 03:05:00 +00:00 | -0.0°      | 73.2°     |
| ISS (ZARYA) | 2025-08-22 02:06:22 +00:00 | 0.0°       | 211.6°    | 2025-08-22 02:11:25 +00:00 | 22.4°      | 143.1°    | 2025-08-22 02:16:29 +00:00 | -0.0°      | 74.8°     |
| ISS (ZARYA) | 2025-08-23 01:18:23 +00:00 | 0.0°       | 199.5°    | 2025-08-23 01:23:07 +00:00 | 15.2°      | 138.5°    | 2025-08-23 01:27:52 +00:00 | -0.0°      | 77.8°     |
| ISS (ZARYA) | 2025-08-23 02:53:56 +00:00 | 0.0°       | 240.8°    | 2025-08-23 02:59:22 +00:00 | 62.4°      | 156.8°    | 2025-08-23 03:04:49 +00:00 | -0.0°      | 72.9°     |
| ISS (ZARYA) | 2025-08-24 02:05:33 +00:00 | 0.0°       | 231.3°    | 2025-08-24 02:10:55 +00:00 | 44.2°      | 151.8°    | 2025-08-24 02:16:17 +00:00 | -0.0°      | 72.6°     |
| ISS (ZARYA) | 2025-08-25 01:17:15 +00:00 | 0.0°       | 221.0°    | 2025-08-25 01:22:29 +00:00 | 30.7°      | 147.0°    | 2025-08-25 01:27:44 +00:00 | -0.0°      | 73.4°     |
| ISS (ZARYA) | 2025-08-25 02:53:34 +00:00 | 0.0°       | 256.4°    | 2025-08-25 02:59:01 +00:00 | 82.6°      | 345.7°    | 2025-08-25 03:04:30 +00:00 | -0.0°      | 76.0°     |
| ISS (ZARYA) | 2025-08-26 00:29:04 +00:00 | 0.0°       | 209.8°    | 2025-08-26 00:34:04 +00:00 | 21.2°      | 142.4°    | 2025-08-26 00:39:06 +00:00 | -0.0°      | 75.2°     |
| ISS (ZARYA) | 2025-08-26 02:05:01 +00:00 | 0.0°       | 248.3°    | 2025-08-26 02:10:28 +00:00 | 79.6°      | 161.2°    | 2025-08-26 02:15:56 +00:00 | -0.0°      | 73.9°     |
```
</details>

---

***Context: There are no the satellite passes with these parameters***  
Prompt: My coordinates are 50.06143 19.93658. Show me ISS (ZARYA) passes  in the next 1 day but only if the minimum culmination altitude is 50
Expected Response: 'ISS (ZARYA)' satellite passes for the next 10 days
<details>
<summary>AI response</summary>

```text
PYA) | 2025-08-26 02:05:01 +00:00 | 0.0°       | 248.3°    | 2025-08-26 02:10:28 +00:00 | 79.6°      | 161.2°    | 2025-08-26 02:15:56 +00:00 | -0.0°      | 73.9°     |
```
</details>
--- 

--- 
***Context: No user's location in the prompt. Required params are not passed***  
Prompt: Show me the satellite passes.  
Expected Response:*** AI will ask about your location  

<details>
<summary>AI response</summary>

```text
There are no ISS (ZARYA) passes over your location (50.06143, 19.93658) in the next 1 day with a minimum culmination altitude of 50 degrees.
```
</details>
--- 

--- 
***Context: Coordinates are passed, the satellite's name passed***  
Prompt: My coordinates are 50.06143 19.93658. Show me ISS (ZARYA) passes.  
Expected Response: 'ISS (ZARYA)' satellite passes for the next 10 days  
<details>
<summary>AI response</summary>

```text
Passes of satellite 'ISS (ZARYA)' over location (50.06143, 19.93658) during the next 10 days.

| Satellite   | Start (UTC)                | Altitude   | Azimuth   | Culmination (UTC)          | Altitude   | Azimuth   | End (UTC)                  | Altitude   | Azimuth   |
|-------------|----------------------------|------------|-----------|----------------------------|------------|-----------|----------------------------|------------|-----------|
| ISS (ZARYA) | 2025-08-19 02:55:23 +00:00 | 0.0°       | 201.3°    | 2025-08-19 03:00:10 +00:00 | 16.1°      | 139.2°    | 2025-08-19 03:04:59 +00:00 | -0.0°      | 77.3°     |
| ISS (ZARYA) | 2025-08-21 02:54:29 +00:00 | 0.0°       | 222.6°    | 2025-08-21 02:59:44 +00:00 | 32.4°      | 147.8°    | 2025-08-21 03:05:00 +00:00 | -0.0°      | 73.2°     |
| ISS (ZARYA) | 2025-08-22 02:06:22 +00:00 | 0.0°       | 211.6°    | 2025-08-22 02:11:24 +00:00 | 22.4°      | 143.1°    | 2025-08-22 02:16:29 +00:00 | -0.0°      | 74.8°     |
| ISS (ZARYA) | 2025-08-23 01:18:23 +00:00 | 0.0°       | 199.5°    | 2025-08-23 01:23:07 +00:00 | 15.2°      | 138.6°    | 2025-08-23 01:27:52 +00:00 | -0.0°      | 77.8°     |
| ISS (ZARYA) | 2025-08-23 02:53:56 +00:00 | 0.0°       | 240.8°    | 2025-08-23 02:59:22 +00:00 | 62.4°      | 156.6°    | 2025-08-23 03:04:49 +00:00 | -0.0°      | 72.9°     |
| ISS (ZARYA) | 2025-08-24 02:05:33 +00:00 | 0.0°       | 231.3°    | 2025-08-24 02:10:54 +00:00 | 44.2°      | 151.9°    | 2025-08-24 02:16:17 +00:00 | -0.0°      | 72.6°     |
| ISS (ZARYA) | 2025-08-25 01:17:15 +00:00 | 0.0°       | 221.0°    | 2025-08-25 01:22:29 +00:00 | 30.7°      | 147.1°    | 2025-08-25 01:27:44 +00:00 | -0.0°      | 73.4°     |
| ISS (ZARYA) | 2025-08-25 02:53:34 +00:00 | 0.0°       | 256.4°    | 2025-08-25 02:59:01 +00:00 | 82.6°      | 346.4°    | 2025-08-25 03:04:30 +00:00 | -0.0°      | 76.0°     |
| ISS (ZARYA) | 2025-08-26 00:29:04 +00:00 | 0.0°       | 209.8°    | 2025-08-26 00:34:05 +00:00 | 21.2°      | 142.3°    | 2025-08-26 00:39:06 +00:00 | -0.0°      | 75.2°     |
| ISS (ZARYA) | 2025-08-26 02:05:01 +00:00 | 0.0°       | 248.3°    | 2025-08-26 02:10:28 +00:00 | 79.6°      | 160.7°    | 2025-08-26 02:15:56 +00:00 | -0.0°      | 73.9°     |
```
</details>
--- 



--- 
***Context: Coordinates are passed, the satellite's name passed, number of days, other than default, passed***  
Prompt: My coordinates are 50.06143 19.93658. Show me CREW DRAGON 11 passes for the next 5 days.
Expected Response: 'CREW DRAGON 11' satellite passes for the next 5 days
<details>
<summary>AI Response</summary>

```text
Passes of satellite 'CREW DRAGON 11' over location (50.06143, 19.93658) during the next 5 days:

| Satellite      | Start (UTC)                | Altitude   | Azimuth   | Culmination (UTC)          | Altitude   | Azimuth   | End (UTC)                  | Altitude   | Azimuth   |
|----------------|----------------------------|------------|-----------|----------------------------|------------|-----------|----------------------------|------------|-----------|
| CREW DRAGON 11 | 2025-08-19 02:55:25 +00:00 | 0.0°       | 201.3°    | 2025-08-19 03:00:12 +00:00 | 16.2°      | 139.2°    | 2025-08-19 03:05:01 +00:00 | -0.0°      | 77.3°     |
| CREW DRAGON 11 | 2025-08-21 02:54:33 +00:00 | 0.0°       | 222.6°    | 2025-08-21 02:59:48 +00:00 | 32.5°      | 147.8°    | 2025-08-21 03:05:05 +00:00 | -0.0°      | 73.2°     |
```
</details>
--- 

--- 
***Context: Coordinates are passed, Wrong name of the satellite***  
Prompt: My coordinates are 50.06143 19.93658. Show me My satellite passes.  
Expected Response: 'ISS (ZARYA)' satellite passes for the next 10 days  

<details>
<summary>AI response</summary>

```text
Passes of satellite 'ISS (ZARYA)' over location (50.06143, 19.93658) during the next 10 days.

| Satellite   | Start (UTC)                | Altitude   | Azimuth   | Culmination (UTC)          | Altitude   | Azimuth   | End (UTC)                  | Altitude   | Azimuth   |
|-------------|----------------------------|------------|-----------|----------------------------|------------|-----------|----------------------------|------------|-----------|
| ISS (ZARYA) | 2025-08-19 02:55:23 +00:00 | 0.0°       | 201.3°    | 2025-08-19 03:00:10 +00:00 | 16.1°      | 139.2°    | 2025-08-19 03:04:59 +00:00 | -0.0°      | 77.3°     |
| ISS (ZARYA) | 2025-08-21 02:54:29 +00:00 | 0.0°       | 222.6°    | 2025-08-21 02:59:44 +00:00 | 32.4°      | 147.8°    | 2025-08-21 03:05:00 +00:00 | -0.0°      | 73.2°     |
| ISS (ZARYA) | 2025-08-22 02:06:22 +00:00 | 0.0°       | 211.6°    | 2025-08-22 02:11:24 +00:00 | 22.4°      | 143.1°    | 2025-08-22 02:16:29 +00:00 | -0.0°      | 74.8°     |
| ISS (ZARYA) | 2025-08-23 01:18:23 +00:00 | 0.0°       | 199.5°    | 2025-08-23 01:23:07 +00:00 | 15.2°      | 138.6°    | 2025-08-23 01:27:52 +00:00 | -0.0°      | 77.8°     |
| ISS (ZARYA) | 2025-08-23 02:53:56 +00:00 | 0.0°       | 240.8°    | 2025-08-23 02:59:22 +00:00 | 62.4°      | 156.6°    | 2025-08-23 03:04:49 +00:00 | -0.0°      | 72.9°     |
| ISS (ZARYA) | 2025-08-24 02:05:33 +00:00 | 0.0°       | 231.3°    | 2025-08-24 02:10:54 +00:00 | 44.2°      | 151.9°    | 2025-08-24 02:16:17 +00:00 | -0.0°      | 72.6°     |
| ISS (ZARYA) | 2025-08-25 01:17:15 +00:00 | 0.0°       | 221.0°    | 2025-08-25 01:22:29 +00:00 | 30.7°      | 147.1°    | 2025-08-25 01:27:44 +00:00 | -0.0°      | 73.4°     |
| ISS (ZARYA) | 2025-08-25 02:53:34 +00:00 | 0.0°       | 256.4°    | 2025-08-25 02:59:01 +00:00 | 82.6°      | 346.4°    | 2025-08-25 03:04:30 +00:00 | -0.0°      | 76.0°     |
| ISS (ZARYA) | 2025-08-26 00:29:04 +00:00 | 0.0°       | 209.8°    | 2025-08-26 00:34:05 +00:00 | 21.2°      | 142.3°    | 2025-08-26 00:39:06 +00:00 | -0.0°      | 75.2°     |
| ISS (ZARYA) | 2025-08-26 02:05:01 +00:00 | 0.0°       | 248.3°    | 2025-08-26 02:10:28 +00:00 | 79.6°      | 160.7°    | 2025-08-26 02:15:56 +00:00 | -0.0°      | 73.9°     |
```
</details>
--- 

--- 
***Context: Coordinates are passed, the satellite's name passed, number of days, other than default, passed, timezone parameter used***  
Prompt: My coordinates are 50.06143 19.93658. Show me CREW DRAGON 11 passes for the next 5 days. Use timezone Europe/Warsaw 
Expected Response: 'CREW DRAGON 11' satellite passes for the next 5 days, Data is calculated from default UTC into Europe/Warsaw
<details>
<summary>AI Response</summary>

```text
Passes of satellite 'CREW DRAGON 11' over location (50.06143, 19.93658) during the next 5 days:

| Satellite      | Start (Europe/Warsaw)      | Altitude   | Azimuth   | Culmination (Europe/Warsaw)   | Altitude   | Azimuth   | End (Europe/Warsaw)        | Altitude   | Azimuth   |
|----------------|----------------------------|------------|-----------|-------------------------------|------------|-----------|----------------------------|------------|-----------|
| CREW DRAGON 11 | 2025-08-19 04:55:25 +02:00 | 0.0°       | 201.3°    | 2025-08-19 05:00:12 +02:00    | 16.2°      | 139.2°    | 2025-08-19 05:05:01 +02:00 | -0.0°      | 77.3°     |
| CREW DRAGON 11 | 2025-08-21 04:54:33 +02:00 | 0.0°       | 222.6°    | 2025-08-21 04:59:48 +02:00    | 32.5°      | 147.8°    | 2025-08-21 05:05:05 +02:00 | -0.0°      | 73.2°     |
```
</details>
--- 

--- 
**Context: Coordinates are passed, the satellite's name passed, number of days, other than default, passed, min altitude param passed**  
Prompt: My coordinates are 50.06143 19.93658. Show me CREW DRAGON 11 passes for the next 5 days. Search for the passes with minimum culmination altitude 20 deg  
Expected Response: 'CREW DRAGON 11' satellite passes for the next 5 days, but only if satellite pass minimum culmination altitude >= 20 deg  
<details>
<summary>AI Response</summary>

```text
Passes of satellite 'CREW DRAGON 11' over location (50.06143, 19.93658) during the next 5 days:

| Satellite      | Start (UTC)                | Altitude   | Azimuth   | Culmination (UTC)          | Altitude   | Azimuth   | End (UTC)                  | Altitude   | Azimuth   |
|----------------|----------------------------|------------|-----------|----------------------------|------------|-----------|----------------------------|------------|-----------|
| CREW DRAGON 11 | 2025-08-21 02:54:33 +00:00 | 0.0°       | 222.6°    | 2025-08-21 02:59:48 +00:00 | 32.5°      | 147.8°    | 2025-08-21 03:05:05 +00:00 | -0.0°      | 73.2°     |
```
</details>
--- 