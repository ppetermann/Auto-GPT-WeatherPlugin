# Auto-GPT-WeatherPlugin

Simple plugin to add weather functionality to Auto-GPT by using python-weather

USE AT YOUR OWN RISK

## Plugin Installation Steps

1. **Clone or download the plugin repository:**
   Clone the plugin repository, or download the repository as a zip file.

2. **Install the plugin's dependencies (if any):**
   Note: If you run auto-gpt in docker, you will have to rebuild the container with the plugins requirements (python-weather) added to the requirements.txt file.  (or run a custom more complex setup)

   Navigate to the plugin's folder in your terminal, and run the following command to install any required dependencies:

   ``` shell
      pip install -r requirements.txt
   ```

3. **Package the plugin as a Zip file:**
   If you cloned the repository, compress the plugin folder as a Zip file.

4. **Copy the plugin's Zip file:**
   Place the plugin's Zip file in the `plugins` folder of the Auto-GPT repository.

5. **Allow-list the plugin (optional):**
   Add the plugin's class name to the `ALLOWLISTED_PLUGINS` in the `.env` file to avoid being prompted with a warning when loading the plugin: (remove ,OtherPlugin from example ;)

   ``` shell
   ALLOWLISTED_PLUGINS=AutoGPTWeatherPlugin,OtherPlugin
   ```
   If the plugin is not allow-listed, you will be warned before it's loaded.

6. **More Config**
in your .env file you can set the following variables
`WEATHER_PLUGIN_UNITS=` can be set to `metric` or `imperial` to change the units used by the weather plugin, defaults to `metric`

## the commands for your agent to use are
`get_weather_for` best asked as `get weather for <location>` will return the current weather for the location/city specified