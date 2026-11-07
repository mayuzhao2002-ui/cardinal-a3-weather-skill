# Cardinal A3 weather skill tap

Original CSCI 599 course-project skill for current weather questions and two-day forecasts with Open-Meteo. No API key is required. The standalone helper returns forecast data using only the Python standard library.

## Install through a Hermes skill tap

```sh
hermes skills tap add mayuzhao2002-ui/cardinal-a3-weather-skill
hermes skills install mayuzhao2002-ui/cardinal-a3-weather-skill/skills/a3-weather
python ~/.hermes/skills/a3-weather/scripts/weather.py --latitude 34.05 --longitude -118.24
```

Use your configured `HERMES_HOME` in place of `~/.hermes` if you use a custom home. Keep the normal skill scanner enabled and review its verdict. The full GitHub skill identifier installs the complete skill directory, including its helper; it is not a direct SKILL.md URL installation.

Inside Cardinal, the skill instructions call the restricted `a3_weather` tool. A fresh Hermes installation can run the installed helper directly. Coordinates represent the fictional Los Angeles test profile, not a user's precise location. Output includes forecast dates, Celsius minimum/maximum temperature and precipitation probability. The helper does not fetch current-condition fields.

The assignment evidence records the public commit and an actual installation/run transcript from a clean Hermes installation. Do not treat this README alone as proof that an installation ran.

## Attribution

AI assistance: Codex drafted the skill and helper. The helper uses documented forecast parameters from [Open-Meteo](https://open-meteo.com/en/docs). MIT license; see LICENSE.
