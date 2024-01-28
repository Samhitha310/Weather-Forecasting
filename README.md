**HTML Opening Tag:**

Marks the beginning of the HTML document.
**Head Section:**

Contains metadata for the document:
Character set is set to UTF-8.
Viewport settings are configured for responsiveness.
The title of the document is set to "Weather Forecast."
Links an external stylesheet named 'style.css.'
Body Section:

**Contains the main content of the document.
The content is organized within a <div> with the class "container."
Includes a heading (<h1>) with the text "Weather Forecast" and a weather information container (<div> with the class "weather-info").
Inside the weather information container, there are various paragraphs (<p>) and heading (<h2>) elements with spans (<span>) that will be dynamically populated with data.
The weather data is received from the server in JSON format using a template engine ({{ weather_data|tojson }}).
The inline JavaScript block parses the JSON data and dynamically updates the content of HTML elements with the fetched weather data:
Updates the city name (<span id="city-name">).
Updates the temperature (<span id="temperature">).
Updates the humidity (<span id="humidity">).
Updates the weather description (<span id="description">).**
